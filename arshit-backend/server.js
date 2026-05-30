const express = require('express');
const mysql = require('mysql2');
const cors = require('cors');
const multer = require('multer');

const app = express();

// Middleware
app.use(cors());
app.use(express.json()); // Parses JSON data
app.use(express.urlencoded({ extended: true }));
app.use('/uploads', express.static('uploads')); // Serves uploaded resumes publicly

// Database Connection Setup
const db = mysql.createConnection({
    host: 'localhost',
    user: 'root', // Replace with your MySQL username
    password: 'Rahasya99@', // Replace with your MySQL password
    database: 'arshit_group_db'
});

db.connect((err) => {
    if (err) throw err;
    console.log('Successfully connected to MySQL database!');
});

// Configure File Uploads (Multer) - Only allow PDFs and keep extension
const storage = multer.diskStorage({
    destination: function (req, file, cb) {
        cb(null, 'uploads/');
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
    db.query(query, [name, email, subject, message], (err, result) => {
        if (err) return res.status(500).json({ error: err.message });
        res.status(200).json({ message: 'Contact message saved successfully!' });
    });
});

// 2. Endpoint for Internship Application (with Resume Upload)
app.post('/api/apply', upload.single('resumeUpload'), (req, res) => {
    const { fullName, email, phone, internshipRole, coverLetter } = req.body;
    const resumePath = req.file ? req.file.path.replace(/\\/g, '/') : null; 
    
    // Step 1: Find the role_id from internship_roles table using the key from frontend
    const findRoleQuery = 'SELECT id FROM internship_roles WHERE role_key = ?';
    
    db.query(findRoleQuery, [internshipRole], (err, roleResult) => {
        if (err) return res.status(500).json({ error: err.message });
        
        if (roleResult.length === 0) {
            return res.status(400).json({ error: 'Invalid internship role selected.' });
        }
        
        const roleId = roleResult[0].id;
        
        // Step 2: Insert application using the roleId (Normalizing with Join capability)
        const query = 'INSERT INTO applications (full_name, email, phone, role_id, resume_path, why_join) VALUES (?, ?, ?, ?, ?, ?)';
        
        db.query(query, [fullName, email, phone, roleId, resumePath, coverLetter], (err, result) => {
            if (err) {
                if (err.code === 'ER_DUP_ENTRY') {
                    return res.status(400).json({ error: 'Email or Phone number already registered!' });
                }
                return res.status(500).json({ error: err.message });
            }
            res.status(200).json({ message: 'Application submitted successfully!' });
        });
    });
});

// Start the server
// --- ADMIN & DASHBOARD ENDPOINTS ---

// 3. Admin Login
app.post('/api/login', (req, res) => {
    const { username, password } = req.body;
    
    const query = 'SELECT * FROM admins WHERE username = ? AND password = ?';
    db.query(query, [username, password], (err, results) => {
        if (err) return res.status(500).json({ error: err.message });
        
        if (results.length > 0) {
            // In a real app, you'd use JWT tokens. For now, we'll return success.
            res.status(200).json({ message: 'Login successful', adminId: results[0].id });
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
        
    db.query(query, (err, results) => {
        if (err) return res.status(500).json({ error: err.message });
        res.status(200).json(results);
    });
});

const PORT = 3000;
app.listen(PORT, () => console.log(`Server running on http://localhost:${PORT}`));
