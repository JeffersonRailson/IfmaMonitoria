const http = require('http')

http.createServer((req,res) => {
    res.end('Olá Mundo!');
  }).listen(3000);