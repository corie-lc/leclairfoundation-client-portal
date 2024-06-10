import mysql
import mysql.connector
from datetime import datetime


import os

def get_access_id_server():
    return os.environ['access_id']

def get_secret_key():
    return os.environ['secret_key']

def get_server_password():
    return os.environ['password']

def get_server_name():
    return os.environ['server_name']

def get_photo_server_name():
    return os.environ['photo_server_name']

def get_database():
    return mysql.connector.connect(
        host=get_server_name(),
        # localhost or 192.168.0.26 for remote in home
        user="doadmin",
        password=get_server_password(),
        database="collec",
        port=25060
    )


def login(username, password):
    mydb = get_database()

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM leclairfoundationlogins")

    for user in cursor:
        if username == user[1] and password == user[2]:
            return True
        
    return False




def get_user_requests(username):
    mydb = get_database()
    
    list = []

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM leclairfoundation_requests")

    for request in cursor:
        if request[3] == username:
            list.append(request)
    
    print(list)     
    return list



def create_request(request, username):
    mydb = get_database()
    mycursor = mydb.cursor()
    mycursor.execute('''

            INSERT INTO leclairfoundation_requests
            VALUES (%s, %s, %s, %s, %s, %s);

        ''', (
        "000", "not-started", request, username, "none", datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    
    mydb.commit()