const sqlite3 = require('sqlite3').verbose();
const Calc = require('./calc.js');
const a = new Calc();


// open the database
let db = new sqlite3.Database('./shipDatabase.db', sqlite3.OPEN_READWRITE, (err) => {
    if (err) {
        console.error(err.message);
    }
    console.log('Connected to the database.');
});

db.serialize(() => {
    db.each(`SELECT x_coords, y_coords FROM coords`, (err, row) => {
        if (err) {
            console.error(err.message);
        }
        var coord = "(" + row.X_COORDS + "," + row.Y_COORDS + ")";
        console.log(coord)
        
	a.graphit(coord);    
    });
});


db.close((err) => {
    if (err) {
        console.error(err.message);
    }
    console.log('Close the database connection.');
});
