from sqlite3 import Cursor
import mysql.connector
import os
import environ

env = environ.Env()
environ.Env()
environ.Env.read_env()
ENVIROMENT = env
token = str(os.environ.get('DBHOST'))

def conection():
    try:
        connection = mysql.connector.connect(
            host=str(os.environ.get('DBHOST')),
            user=str(os.environ.get('DBUSER')),
            passwd=str(os.environ.get('DBPASSWORD')),
            database=str(os.environ.get('DBNAME'))
        )
        return connection
    except OSError:
        return OSError

def registerStat(chat_id, message_id, user_id, user_name):
    connection = conection()
    try:
        cursor = connection.cursor()
        cursor.execute("insert into im_stats(chat_id, message_id, user_name_requested, user_id_requested,   request_date) values('{}', '{}', '{}', '{}', current_timestamp());".format(chat_id, message_id, user_name, user_id ))
        connection.commit()
        cursor.close()
    except OSError:
        return OSError


def updateStatusStat(chat_id, message_id, user_id, user_name):
    connection = conection()
    try:
        cursor = connection.cursor()
        cursor.execute("update bot_attendence.im_stats set user_id_procesed = '{}', user_name_procesed = '{}', date_procesed = current_timestamp() where chat_id = '{}' and message_id ='{}' and date_procesed is null ;" .format(user_id, user_name, chat_id, message_id ))       
        connection.commit()
        cursor.close()
    except OSError:
        return OSError

def doneStatusStat(chat_id, message_id, user_id, user_name):
    connection = conection()
    try:
        cursor = connection.cursor()
        cursor.execute("update bot_attendence.im_stats set  date_done = current_timestamp() where chat_id = '{}' and message_id ='{}' and user_id_procesed = '{}' and user_name_procesed = '{}' and date_done is null ;" .format(chat_id, message_id, user_id, user_name))       
        connection.commit()
        cursor.close()
    except OSError:
        return OSError


def checkStats():

    connection = conection()
    try:
        cursor = connection.cursor()
        cursor.execute('select chat_id, user_name_requested, user_id_requested from im_stats where date_procesed is null')
        select = cursor.fetchall()
        if len(select) > 0:
            return select
        else:
            select = None
    except OSError:
        return OSError


def checkProcessedStats():

    connection = conection()
    try:
        cursor = connection.cursor()
        cursor.execute('select TIMESTAMPDIFF(minute, date_procesed, current_timestamp()),chat_id, user_name_requested, user_id_requested, user_id_procesed, user_name_procesed from im_stats where date_done is null')
        select = cursor.fetchall()
        if len(select) > 0:
            return select                    
        else:
            select = None
    except OSError:
        return OSError





   


