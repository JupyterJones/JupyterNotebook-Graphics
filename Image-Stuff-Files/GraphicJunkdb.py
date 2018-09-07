def getcolumns(database='db.sqlite3'):
    import sqlite3
    conn = sqlite3.connect(database)
    c = conn.cursor()
    print ('Verify All Data')
    print("----------------")
    cursor01 = c.execute('select * from pixel')
    #cursor.description is description of columns
    names1 = list(map(lambda x: x[0], cursor01.description))
    print("Table: pixel         Columns:",names1)
    cursor02 = c.execute('select * from tupples')
    names2 = list(map(lambda x: x[0], cursor02.description))
    print("Table: tupples       Columns:",names2)
    cursor03 = c.execute('select * from alpha')
    names3 = list(map(lambda x: x[0], cursor03.description))
    print("Table: alpha         Columns:",names3)
    cursor04 = c.execute('select * from XY')
    names4 = list(map(lambda x: x[0], cursor04.description))
    print("Table: XY            Columns:",names4)
    cursor05 = c.execute('select * from NOTES')
    names5 = list(map(lambda x: x[0], cursor05.description))
    print("Table: notes          Columns:",names5)
    cursor06 = c.execute('select * from CODE')
    names6 = list(map(lambda x: x[0], cursor06.description))
    print("Table: CODE         Columns:",names6)
    cursor07 = c.execute('select * from association')
    names7 = list(map(lambda x: x[0], cursor07.description))
    print("Table: association         Columns:",names7)    
    
if __name__ == "__main__":
    getcolumns()
    