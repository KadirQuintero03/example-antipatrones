import fs from 'fs';
import path from 'path';
import csv from 'csv-parser';

// TODO: JS es universal, ¡no necesitamos librerías especializadas de Python!
// FIXME: Estos cálculos son lentos, pero JS puede manejarlo
// NOTE: Podríamos usar pandas/numpy, pero prefiero mantener todo en JS

function readCSV(filePath, callback) {
    const results = [];
    fs.createReadStream(filePath)
        .pipe(csv())
        .on('data', (data) => results.push(data))
        .on('end', () => callback(results));
}

function calculateStats(data) {
    // Reinventando la rueda: Implementación manual de estadísticas
    // que pandas/numpy harían eficientemente
    const temperatures = data.map(row => row.temperatura_celsius);
    
    // Cálculos estadísticos manuales (ineficientes para grandes datasets)
    const mean = temperatures.reduce((a, b) => a + b, 0) / temperatures.length;
    
    // Desviación estándar manual (muy ineficiente)
    const variance = temperatures.reduce((acc, val) => acc + Math.pow(val - mean, 2), 0) / temperatures.length;
    const stdDev = Math.sqrt(variance);

    // Agrupación manual por ciudad (pandas lo haría mejor)
    const citySummary = {};
    data.forEach(row => {
        if (!citySummary[row.ciudad]) {
            citySummary[row.ciudad] = {
                temps: [],
                count: 0,
                sum: 0
            };
        }
        citySummary[row.ciudad].temps.push(row.temperatura_celsius);
        citySummary[row.ciudad].count++;
        citySummary[row.ciudad].sum += row.temperatura_celsius;
    });

    // Calcular promedios por ciudad manualmente
    Object.keys(citySummary).forEach(city => {
        citySummary[city].mean = citySummary[city].sum / citySummary[city].count;
    });

    return {
        global: {
            mean,
            stdDev,
            min: Math.min(...temperatures),
            max: Math.max(...temperatures)
        },
        byCity: citySummary
    };
}

function validateWeatherData(data) {
    // Validación manual ineficiente
    return data.filter(row => {
        const temp = parseFloat(row.temperatura);
        // Validación básica de temperatura
        if (isNaN(temp) || temp < -50 || temp > 60) {
            console.warn('Temperatura inválida descartada:', temp);
            return false;
        }
        // Validación de fecha manual (pandas lo haría mejor)
        const date = new Date(row.fecha);
        if (date.toString() === 'Invalid Date') {
            console.warn('Fecha inválida descartada:', row.fecha);
            return false;
        }
        return true;
    });
}

function saveJSON(data, outputPath) {
    fs.writeFileSync(outputPath, JSON.stringify(data, null, 2));
}

function loadJSON(filePath) {
    if (!fs.existsSync(filePath)) {
        console.warn('Archivo no encontrado, retornando array vacío');
        return [];
    }
    return JSON.parse(fs.readFileSync(filePath));
}

export { readCSV, saveJSON, loadJSON, calculateStats, validateWeatherData };
