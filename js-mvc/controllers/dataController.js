import path from 'path';
import { fileURLToPath } from 'url';
import { readCSV, saveJSON, loadJSON } from '../models/dataModel.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

function processCSV(req, res) {
    const csvPath = req.file.path
    readCSV(csvPath, (data) => {
        const jsonPath = path.join(__dirname, '../data.json')
        saveJSON(data, jsonPath)
        res.send({ message: 'Procesado y guardado como JSON.' })
    });
}

function getHistoricalData(req, res) {
    const jsonPath = path.join(__dirname, '../data.json');
    const data = loadJSON(jsonPath);
    res.json(data);
}

export { processCSV, getHistoricalData };
