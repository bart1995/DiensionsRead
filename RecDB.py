import sqlite3
from tkinter.filedialog import askopenfilename, askdirectory
from tkinter import *

def path_window_DB():
    root = Tk()
    root.withdraw()
    PathSave = askdirectory()
    root.destroy()
    return PathSave


def db_read(Dimensions, Path):

    sqlite_connection = sqlite3.connect(Path + "/BookDimensions.db")
    cursor = sqlite_connection.cursor()
    try:
        cursor.execute('DROP TABLE sqlitedb_developers;')
        sqlite_connection.commit()
    except:
        pass



    sqlite_create_table_query = '''CREATE TABLE sqlitedb_developers (
                                id INTEGER PRIMARY KEY,
                                Name size TEXT NOT NULL,
                                Nominal size text NOT NULL UNIQUE,
                                Max size text NOT NULL UNIQUE,
                                Min size text NOT NULL UNIQUE);'''

    cursor.execute(sqlite_create_table_query)
    sqlite_connection.commit()

    for Dimension in Dimensions:
         cursor.execute('INSERT INTO sqlitedb_developers VALUES {};'.format(str(Dimension)))
    sqlite_connection.commit()

    cursor.close()

