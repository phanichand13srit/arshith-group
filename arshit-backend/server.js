const express = require('express');
const cors = require('cors');
const multer = require('multer');
const path = require('path');
const fs = require('fs');

const app = express();

// Middleware
app.use(cors());
app.use(express.json()); // Parses JSON data
app.use(express.urlencoded({ extended: true }));

// Ensure uploads folder exists (dynamically configured for local and Vercel)
let uploadsDir = path.join(__dirname, 'uploads');
if (process.env.VERCEL) {
    uploadsDir = path.join('/tmp', 'uploads');
}

if (!fs.existsSync(uploadsDir)) {
    fs.mkdirSync(uploadsDir, { recursive: true });
}

app.use('/uploads', express.static(uploadsDir)); // Serves uploaded resumes publicly
app.use('/api/uploads', express.static(uploadsDir)); // Serves uploaded resumes under Vercel API routing

// JSON-based Portable Database connection setup (optimized for serverless environment)
let dbPath = path.join(__dirname, 'arshith_group_db.json');
if (process.env.VERCEL) {
    dbPath = path.join('/tmp', 'arshith_group_db.json');
}

// Helper to read database
function readDb() {
    try {
        if (!fs.existsSync(dbPath)) {
            const initialData = {
                contacts: [],
                internship_roles: [
                    { id: 1, role_key: "software-dev-intern-3", role_display_name: "Software & Web Development Intern - 3 Months" },
                    { id: 2, role_key: "software-dev-intern-6", role_display_name: "Software & Web Development Intern - 6 Months" },
                    { id: 3, role_key: "ecommerce-ops-intern-3", role_display_name: "E-Commerce Operations Intern - 3 Months" },
                    { id: 4, role_key: "ecommerce-ops-intern-6", role_display_name: "E-Commerce Operations Intern - 6 Months" }
                ],
                applications: [],
                admins: [
                    { id: 1, username: "admin", password: "admin123" }
                ]
            };
            fs.writeFileSync(dbPath, JSON.stringify(initialData, null, 4));
            return initialData;
        }
        const content = fs.readFileSync(dbPath, 'utf8');
        return JSON.parse(content);
    } catch (err) {
        console.error("Error reading JSON database:", err);
        return { contacts: [], internship_roles: [], applications: [], admins: [] };
    }
}

// Helper to write database
function writeDb(data) {
    try {
        fs.writeFileSync(dbPath, JSON.stringify(data, null, 4));
    } catch (err) {
        console.error("Error writing JSON database:", err);
    }
}

// Auto-initialize DB on server start
readDb();

// Configure File Uploads (Multer) - Only allow PDFs and keep extension
const storage = multer.diskStorage({
    destination: function (req, file, cb) {
        cb(null, uploadsDir);
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
    
    try {
        const dbData = readDb();
        const newContact = {
            id: Date.now(),
            name: name || '',
            email: email || '',
            subject: subject || '',
            message: message || '',
            created_at: new Date().toISOString()
        };
        dbData.contacts.push(newContact);
        writeDb(dbData);
        res.status(200).json({ message: 'Contact message saved successfully!' });
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

// 2. Endpoint for Internship Application (with Resume Upload)
app.post('/api/apply', upload.single('resumeUpload'), (req, res) => {
    const { fullName, email, phone, internshipRole, coverLetter } = req.body;
    const resumePath = req.file ? 'api/uploads/' + req.file.filename : null; 
    
    try {
        const dbData = readDb();
        
        // Find internship role display name based on key
        const role = dbData.internship_roles.find(r => r.role_key === internshipRole);
        if (!role) {
            return res.status(400).json({ error: 'Invalid internship role selected.' });
        }
        
        // Check unique constraints for email or phone
        const exists = dbData.applications.some(app => app.email === email || app.phone === phone);
        if (exists) {
            return res.status(400).json({ error: 'Email or Phone number already registered!' });
        }
        
        const newApplication = {
            id: Date.now(),
            full_name: fullName,
            email: email,
            phone: phone,
            role_id: role.id,
            resume_path: resumePath,
            why_join: coverLetter || '',
            created_at: new Date().toISOString()
        };
        
        dbData.applications.push(newApplication);
        writeDb(dbData);
        res.status(200).json({ message: 'Application submitted successfully!' });
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

// 3. Admin Login
app.post('/api/login', (req, res) => {
    const { username, password } = req.body;
    
    try {
        const dbData = readDb();
        const admin = dbData.admins.find(a => a.username === username && a.password === password);
        
        if (admin) {
            res.status(200).json({ message: 'Login successful', adminId: admin.id });
        } else {
            res.status(401).json({ error: 'Invalid username or password' });
        }
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

// 4. Fetch All Applications (For Dashboard)
app.get('/api/admin/applications', (req, res) => {
    try {
        const dbData = readDb();
        const enriched = dbData.applications.map(app => {
            const role = dbData.internship_roles.find(r => r.id === app.role_id);
            return {
                id: app.id,
                full_name: app.full_name,
                email: app.email,
                phone: app.phone,
                role: role ? role.role_display_name : 'Unknown',
                resume_path: app.resume_path,
                why_join: app.why_join,
                created_at: app.created_at
            };
        });
        res.status(200).json(enriched);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
