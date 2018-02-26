import MySQLdb

def ConnectDatabase(dbHost,userName,passWord,dataBase):
    try:
        db = MySQLdb.connect(dbHost,userName,passWord,dataBase)
        cursor = db.cursor()
        return cursor,db
    except Exception as e:
        print(e)
        return False,False

def CloseDatabase(cursor,db):
    if cursor is not None and cursor is not False:
        cursor.close()
    if db is not None and db is not False:
        db.close()



def ExecuteQuery(sql,conf):
    cursor, db = ConnectDatabase(conf['DbHost'], conf['UserName'], conf['Password'], conf['Database'])
    if cursor is False:  # if connnection failed
        print("hi")
        return False
    try:
        count=cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
        #print('Entered ')
        return True
    except Exception as e:
        # Rollback in case there is any error
        #print(e)
        db.rollback()
        return False
    finally:
        CloseDatabase(cursor,db)# disconnect from server


def QueryResult(sql,conf):
    cursor, db =  ConnectDatabase(conf['DbHost'], conf['UserName'], conf['Password'], conf['Database'])
    if cursor is False:  # if connnection failed
        return False
    # Execute the SQL command
    try:
        cursor.execute(sql)
        return cursor.fetchall()
    except:
        return False
        # disconnect from server
    finally:
        CloseDatabase(cursor, db)


def ExecuteQueryCatchException(sql,conf):
    cursor, db = ConnectDatabase(conf['DbHost'], conf['UserName'], conf['Password'], conf['Database'])
    if cursor is False:  # if connnection failed
        return False
    try:
        count=cursor.execute(sql)
        db.commit()
        return True
    finally:
        CloseDatabase(cursor,db)