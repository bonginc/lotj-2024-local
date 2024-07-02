export function hello() {

    const sqlite3 = require('sqlite3');
    const db = new sqlite3.Database('.tt/shipDatabase.db');

    db.all("SELECT * FROM coords");

    try {
        adddlert{"Hello"}:
    } catch(err) {
    	console.log(err);
    }
    return db;
}
