import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { processCSV } from './controllers/dataController.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Generar datos de prueba
function generateTestData(numRecords) {
    const data = [];
    for (let i = 0; i < numRecords; i++) {
        data.push({
            fecha: new Date(2023, Math.floor(Math.random() * 12), Math.floor(Math.random() * 28) + 1).toISOString(),
            ciudad: ['Medellín', 'Bogotá', 'Cali', 'Barranquilla'][Math.floor(Math.random() * 4)],
            temperatura: (Math.random() * 35 + 5).toFixed(1),
            humedad: (Math.random() * 100).toFixed(1)
        });
    }
    return data;
}

// Crear archivo CSV de prueba
function createTestCSV(numRecords) {
    const data = generateTestData(numRecords);
    const csvContent = ['fecha,ciudad,temperatura,humedad'];
    data.forEach(row => {
        csvContent.push(`${row.fecha},${row.ciudad},${row.temperatura},${row.humedad}`);
    });
    
    const testFile = path.join(__dirname, 'test_data.csv');
    fs.writeFileSync(testFile, csvContent.join('\n'));
    return testFile;
}

// Ejecutar prueba de rendimiento
async function runPerformanceTest() {
    const sizes = [100, 1000, 10000];
    
    for (const size of sizes) {
        console.log(`\nProbando con ${size} registros:`);
        const testFile = createTestCSV(size);
        
        console.time(`JS Processing ${size} records`);
        // Simular req y res
        const req = { file: { path: testFile } };
        const res = {
            send: (data) => {
                console.timeEnd(`JS Processing ${size} records`);
                console.log(`Registros procesados: ${data.recordsProcessed}`);
                console.log(`Estadísticas calculadas: ${Object.keys(data.statistics).length} métricas`);
            }
        };
        
        processCSV(req, res);
    }
}

// Ejecutar las pruebas
runPerformanceTest();
