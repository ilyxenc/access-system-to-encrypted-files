import protocol.protocol as pr
import sqlite3

# DB connect / create
conn = sqlite3.connect("db/database.db")
cursor = conn.cursor()

# Service records
accessed = '\nACCESSED\n'
accessDenied = '\nACCESS DENIED\n'

# Users table creation
def createTableUsers():
    pr.add('users table creation')
    sql = '''CREATE TABLE users(login text, password text);'''
    cursor.execute(sql)
    conn.commit()

# Create a new user
def insertUser(username, password):
    pr.add('adding user `' + username + '`')
    values = (username, password)
    sql = '''INSERT INTO users(login, password) VALUES(?,?);'''
    cursor.execute(sql, values)
    conn.commit()

# Access check
def isThereAUserOrNot(username, password):
    values = (username, password)
    sql = '''SELECT * FROM users WHERE login = ? AND password = ?;'''
    cursor.execute(sql, values)
    conn.commit()
    data = cursor.fetchall()
    if len(data) == 1 and data[0] == values:
        pr.add('successful login by `' + username + '`')
        return(accessed)
    else:
        pr.add('failed login by `' + username + '`')
        return(accessDenied)
