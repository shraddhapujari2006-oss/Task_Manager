import mysql.connector

def get_database_connection():
    connection = mysql.connector.connect(
        host = 'gateway01.ap-southeast-1.prod.aws.tidbcloud.com',
        user = '31LWFsRDgTgB4HC.root',
        password = 'en149xlgGX99WvV4',
        port='4000',
        database = 'student_task_manager_1',
        
    )

    return connection

# def get_database_connection():
#     connection = mysql.connector.connect(
#         host = 'localhost',
#         user = 'root',
#         password = 'root123',
#         database = 'student_task_manager'
#     )

#     return connection