import express from 'express';
import cors from 'cors';
import routes from './views/routes.js';

const app = express();

// Middlewares
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Rutas
app.use('/', routes);

app.get('/ping', (_req, res) => {
    res.json({ message: 'I live' });
});

app.listen(3000, () => console.log('Servicio CSV en JS escuchando en puerto 3000'));
