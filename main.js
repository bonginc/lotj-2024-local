const { createServer } = require('node:http');

const hostname = '127.0.0.1';
const port = '8000';

const sqlite3 = require('sqlite3');
const db = new sqlite3.Database('./shipDatabase.db');

const server = createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
});

server.listen(port, hostname, () => {
    console.log('Server running at http://${hostname}:${port}/');
});

db.all("SELECT * FROM coords", (error, rows) => {
    rows.forEach((row) => {
        console.log(row.x + " " + row.y);
    })
});
