import mysql.connector

def DataFetch(queryid):
    mydb = mysql.connector.connect( 
    host="localhost",
    user="root",
    password="iEnable@123",
    database="ConnectorSampleDatabase"
    ) #gives an error if your database doesn't exist

    mycursor = mydb.cursor() 
    sql = 'SELECT id, name, address from ConnectorSampleDatabase.customers where id="{0}";'.format(queryid)

    try:
        #Execute the SQL Query
        mycursor.execute(sql) 
        results = mycursor.fetchall()

        name = results[0][1]
        address = results[0][2]

        #Now return fetched data
        return f"User Name: {name}, Address: {address}"

    except:
        return "Error : Unable to fetch data."