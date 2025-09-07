const path = require('path');
const { readCSV, saveJSON, loadJSON } = require('../models/dataModel');

function processCSV(req, res) {
    const csvPath = req.file.path;
    readCSV(csvPath, (data) => {
        const jsonPath = path.join(__dirname, '../data.json');
        saveJSON(data, jsonPath);
        res.send({ message: 'Procesado y guardado como JSON.' });
    });
}

function getHistoricalData(req, res) {
    const jsonPath = path.join(__dirname, '../data.json');
    const data = loadJSON(jsonPath);
    res.json(data);
}

module.exports = { processCSV, getHistoricalData };
