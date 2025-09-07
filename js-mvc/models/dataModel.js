const fs = require('fs');
const path = require('path');
const csv = require('csv-parser');

function readCSV(filePath, callback) {
    const results = [];
    fs.createReadStream(filePath)
        .pipe(csv())
        .on('data', (data) => results.push(data))
        .on('end', () => callback(results));
}

function saveJSON(data, outputPath) {
    fs.writeFileSync(outputPath, JSON.stringify(data, null, 2));
}

function loadJSON(filePath) {
    return JSON.parse(fs.readFileSync(filePath));
}

module.exports = { readCSV, saveJSON, loadJSON };
