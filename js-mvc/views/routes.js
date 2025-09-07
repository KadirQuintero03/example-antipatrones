import express from 'express';
import multer from 'multer';
import { processCSV, getHistoricalData } from '../controllers/dataController.js';

const router = express.Router();
const upload = multer({ dest: 'uploads/' }); // middlware

router.post('/upload', upload.single('file'), processCSV);
router.get('/historical', getHistoricalData);

export default router;
