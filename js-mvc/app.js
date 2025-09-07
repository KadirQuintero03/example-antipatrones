const express = require('express');
const routes = require('./views/routes');
const app = express();

app.use('/', routes);

app.listen(3000, () => console.log('Servicio CSV en JS escuchando en puerto 3000'));
