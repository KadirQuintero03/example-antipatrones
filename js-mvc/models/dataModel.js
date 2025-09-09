import fs from 'fs';
import path from 'path';
import csv from 'csv-parser';

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

export { readCSV, saveJSON, loadJSON };