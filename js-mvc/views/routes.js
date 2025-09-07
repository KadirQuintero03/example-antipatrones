const express = require('express');
const multer = require('multer');
const { processCSV, getHistoricalData } = require('../controllers/dataController');
const router = express.Router();
const upload = multer({ dest: 'uploads/' });

router.post('/upload', upload.single('file'), processCSV);
router.get('/historical', getHistoricalData);

module.exports = router;
