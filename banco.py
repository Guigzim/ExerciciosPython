import fdb

def DbConnection(sql):
    connect = fdb.connect(dsn='C:/Users/guilh/Desktop/DKSOFT.fdb', user='SYSDBA', password='masterkey' );
    cursor = connect.cursor()
    cursor.execute(sql)
    list = cursor.fetchall()
    connect.close()
    return list