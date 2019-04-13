const express = require('express');

const api = express()

api.get('/', (req, resp) =>(
    resp.send("<h1>Olá Mundo</h1>")
)
)

api.get('/cadastro', (a, b) =>(
    b.send('<h1> Cadastro </h1>')

))

.listen(3000)