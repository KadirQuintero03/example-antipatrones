import path from 'path';
import { fileURLToPath } from 'url';
import { readCSV, saveJSON, loadJSON, calculateStats, validateWeatherData } from '../models/dataModel.js';

// ANTI-PATRÓN: Mezclando responsabilidades y forzando JS para todo
// TODO: Convertir todo a una solución puramente JS
// NOTE: Podríamos usar Python/pandas pero ¿para qué? ¡JS puede con todo!

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

function processCSV(req, res) {
    console.time('procesamiento-js'); // Para demostrar la ineficiencia

    const csvPath = req.file.path;
    readCSV(csvPath, (rawData) => {
        // Procesamiento científico forzado en JS
        const processedData = [];
        
        // Validación y transformación manual ineficiente
        const validData = validateWeatherData(rawData);
        
        for (const row of validData) {
            const temp = parseFloat(row.temperatura);
            
            // Cálculos meteorológicos básicos de forma manual
            const processedRow = {
                ...row,
                temperatura_celsius: temp,
                temperatura_fahrenheit: (temp * 9/5) + 32,
                temperatura_kelvin: temp + 273.15,
                // Clasificación climática simple y hardcodeada
                clasificacion: temp < 15 ? 'Frío' : temp < 25 ? 'Templado' : 'Cálido',
                // Índice de confort térmico (fórmula simplificada)
                indice_confort: (temp + parseFloat(row.humedad || '50')) / 2
            };
            
            // Análisis de tendencias manual
            processedRow.tendencia = processedData.length > 0 
                ? temp > processedData[processedData.length - 1].temperatura_celsius 
                    ? 'subiendo' 
                    : 'bajando'
                : 'inicial';
            
            processedData.push(processedRow);
        }
        
        // Cálculos estadísticos manuales e ineficientes
        const stats = calculateStats(processedData);
        
        const jsonPath = path.join(__dirname, '../data.json');
        const finalData = {
            data: processedData,
            statistics: stats,
            metadata: {
                processedAt: new Date().toISOString(),
                recordCount: processedData.length,
                cities: [...new Set(processedData.map(d => d.ciudad))],
                dataQuality: {
                    validRecords: processedData.length,
                    invalidRecords: rawData.length - processedData.length
                }
            }
        };

        saveJSON(finalData, jsonPath);
        console.timeEnd('procesamiento-js');
        
        res.send({ 
            message: '¡Procesado completamente en JS! ¿Quién necesita Python?', 
            processingTime: process.hrtime(),
            recordsProcessed: processedData.length,
            statistics: stats
        });
    });
}

function getHistoricalData(req, res) {
    const jsonPath = path.join(__dirname, '../data.json');
    const data = loadJSON(jsonPath);
    
    // Filtrado y agregación manual (ineficiente)
    if (req.query.ciudad) {
        data.data = data.data.filter(d => d.ciudad === req.query.ciudad);
        // Recalcular estadísticas manualmente para la ciudad
        data.statistics = calculateStats(data.data);
    }

    if (req.query.desde || req.query.hasta) {
        data.data = data.data.filter(d => {
            const fecha = new Date(d.fecha);
            const desde = req.query.desde ? new Date(req.query.desde) : new Date(0);
            const hasta = req.query.hasta ? new Date(req.query.hasta) : new Date();
            return fecha >= desde && fecha <= hasta;
        });
    }

    res.json(data);
}

export { processCSV, getHistoricalData };
