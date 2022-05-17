import psycopg2

def runquery(aql):
    try:
        connection=psycopg2.connect(user="nmmeugjzfnwdzg",
                                    password="39bb47222f963391dbb7d045da7cbe3d676eda4eaf1e21ecc47cf55a78239b6c",
                                    host="ec2-18-210-64-223.compute-1.amazonaws.com",
                                    database="dc9jg1dtdof51k")
        cur=connection.cursor()
        cur.execute(sql)
        record=cur.fetchall()
        return(record)
    except:
        print("error while fetching data")
    finally:
        cur.close()
        connection.close()
    
                                    
