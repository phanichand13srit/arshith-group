const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const cors = require('cors');
const multer = require('multer');
const path = require('path');
const fs = require('fs');

const app = express();

// Middleware
app.use(cors());
app.use(express.json()); // Parses JSON data
app.use(express.urlencoded({ extended: true }));
app.use('/uploads', express.static(path.join(__dirname, 'uploads'))); // Serves uploaded resumes publicly

// Ensure uploads folder exists
if (!fs.existsSync(path.join(__dirname, 'uploads'))) {
    fs.mkdirSync(path.join(__dirname, 'uploads'));
}

// Database Connection Setup (SQLite optimized for local and Vercel)
let dbPath = path.join(__dirname, 'arshith_group_db.db');
if (process.env.VERCEL) {
    dbPath = path.join('/tmp', 'arshith_group_db.db');
}

const db = new sqlite3.Database(dbPath, (err) => {
    if (err) {
        console.error('Error connecting to SQLite database:', err.message);
    } else {
        console.log('Connected to the SQLite database (arshith_group_db.db).');
        initializeDatabase();
    }
});

function initializeDatabase() {
    db.serialize(() => {
        // 1. Create contacts table
        db.run(`
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                subject TEXT NOT NULL,
                message TEXT NOT NULL,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        `);

        // 2. Create internship_roles table
        db.run(`
            CREATE TABLE IF NOT EXISTS internship_roles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                role_key TEXT NOT NULL UNIQUE,
                role_display_name TEXT NOT NULL
            )
        `, (err) => {
            if (!err) seedRoles();
        });

        // 3. Create applications table
        db.run(`
            CREATE TABLE IF NOT EXISTS applications (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT NOT NULL,
                role_id INTEGER NOT NULL,
                resume_path TEXT,
                why_join TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (role_id) REFERENCES internship_roles(id) ON DELETE CASCADE
            )
        `);

        // 4. Create admins table
        db.run(`
            CREATE TABLE IF NOT EXISTS admins (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
        `, (err) => {
            if (!err) seedAdmin();
        });
    });
}

function seedRoles() {
    db.get("SELECT COUNT(*) as count FROM internship_roles", [], (err, row) => {
        if (!err && row && row.count === 0) {
            const stmt = db.prepare("INSERT INTO internship_roles (role_key, role_display_name) VALUES (?, ?)");
            stmt.run("software-dev-intern-3", "Software & Web Development Intern - 3 Months");
            stmt.run("software-dev-intern-6", "Software & Web Development Intern - 6 Months");
            stmt.run("ecommerce-ops-intern-3", "E-Commerce Operations Intern - 3 Months");
            stmt.run("ecommerce-ops-intern-6", "E-Commerce Operations Intern - 6 Months");
            stmt.finalize();
            console.log("✓ Internship roles seeded successfully.");
        }
    });
}

function seedAdmin() {
    db.get("SELECT COUNT(*) as count FROM admins", [], (err, row) => {
        if (!err && row && row.count === 0) {
            db.run("INSERT INTO admins (username, password) VALUES (?, ?)", ["admin", "admin123"], (err) => {
                if (!err) console.log("✓ Default admin seeded (admin/admin123).");
            });
        }
    });
}

// Configure File Uploads (Multer) - Only allow PDFs and keep extension
const storage = multer.diskStorage({
    destination: function (req, file, cb) {
        cb(null, path.join(__dirname, 'uploads/'));
    },
    filename: function (req, file, cb) {
        const uniqueSuffix = Date.now() + '-' + Math.round(Math.random() * 1E9);
        cb(null, file.fieldname + '-' + uniqueSuffix + '.pdf');
    }
});

const upload = multer({ 
    storage: storage,
    fileFilter: (req, file, cb) => {
        if (file.mimetype === 'application/pdf') {
            cb(null, true);
        } else {
            cb(new Error('Only PDF files are allowed!'), false);
        }
    }
}); 

// Middleware to handle Multer errors
app.use((err, req, res, next) => {
    if (err instanceof multer.MulterError || err.message === 'Only PDF files are allowed!') {
        return res.status(400).json({ error: err.message });
    }
    next(err);
});

// --- API ENDPOINTS ---

// 1. Endpoint for Contact Form
app.post('/api/contact', (req, res) => {
    const { name, email, subject, message } = req.body;
    
    const query = 'INSERT INTO contacts (name, email, subject, message) VALUES (?, ?, ?, ?)';
    db.run(query, [name, email, subject, message], (err) => {
        if (err) return res.status(500).json({ error: err.message });
        res.status(200).json({ message: 'Contact message saved successfully!' });
    });
});

// 2. Endpoint for Internship Application (with Resume Upload)
app.post('/api/apply', upload.single('resumeUpload'), (req, res) => {
    const { fullName, email, phone, internshipRole, coverLetter } = req.body;
    const resumePath = req.file ? 'arshit-backend/uploads/' + req.file.filename : null; 
    
    // Find the role_id from internship_roles table using the key from frontend
    const findRoleQuery = 'SELECT id FROM internship_roles WHERE role_key = ?';
    
    db.get(findRoleQuery, [internshipRole], (err, roleRow) => {
        if (err) return res.status(500).json({ error: err.message });
        
        if (!roleRow) {
            return res.status(400).json({ error: 'Invalid internship role selected.' });
        }
        
        const roleId = roleRow.id;
        
        // Insert application using the roleId
        const query = 'INSERT INTO applications (full_name, email, phone, role_id, resume_path, why_join) VALUES (?, ?, ?, ?, ?, ?)';
        
        db.run(query, [fullName, email, phone, roleId, resumePath, coverLetter], function(err) {
            if (err) {
                if (err.message.includes('UNIQUE') || err.code === 'SQLITE_CONSTRAINT') {
                    return res.status(400).json({ error: 'Email or Phone number already registered!' });
                }
                return res.status(500).json({ error: err.message });
            }
            res.status(200).json({ message: 'Application submitted successfully!' });
        });
    });
});

// 3. Admin Login
app.post('/api/login', (req, res) => {
    const { username, password } = req.body;
    
    const query = 'SELECT * FROM admins WHERE username = ? AND password = ?';
    db.get(query, [username, password], (err, row) => {
        if (err) return res.status(500).json({ error: err.message });
        
        if (row) {
            res.status(200).json({ message: 'Login successful', adminId: row.id });
        } else {
            res.status(401).json({ error: 'Invalid username or password' });
        }
    });
});

// 4. Fetch All Applications (For Dashboard)
app.get('/api/admin/applications', (req, res) => {
    const query = `
        SELECT 
            a.id, 
            a.full_name, 
            a.email, 
            a.phone, 
            r.role_display_name AS role, 
            a.resume_path, 
            a.why_join, 
            a.created_at 
        FROM applications a 
        JOIN internship_roles r ON a.role_id = r.id 
        ORDER BY a.created_at DESC`;
        
    db.all(query, [], (err, rows) => {
        if (err) return res.status(500).json({ error: err.message });
        res.status(200).json(rows);
    });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server running on http://localhost:${PORT}`));
