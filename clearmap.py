import sqlite3

sqliteConnection = sqlite3.connect('.tt/shipDatabase.db');
def dropTables():
    
    try:
            
        cursor = sqliteConnection.cursor();
            
        print("#showme Connected to SQLite");

        cursor.execute("DROP TABLE coords");
        sqliteConnection.commit();
        print("#showme Successfully deleted table");

        cursor.close();

    except sqlite3.Error as error:

        print("#showme Failed to insert Python variable into sqlite table", error)
    
    finally:
        conn = sqlite3.connect('.tt/shipDatabase.db')

        curr = conn.cursor()

        coords = '''
        CREATE TABLE coords (
            id INTEGER (20),
            X_COORDS INTEGER (20),
            Y_COORDS INTEGER (20),
            color TEXT (20)
        )
        '''
    try:
        curr.execute(coords)
        print("#showme {table made}")
    except:
        print('error in table')
        
    conn.close()
    if sqliteConnection:
       sqliteConnection.close()
       print("#showme Connection closed")
dropTables()
