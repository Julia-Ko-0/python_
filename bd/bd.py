import mysql.connector
from mysql.connector import Error
# Соединение
def create_connection(host_name, user_name, user_password):
    connect = None
    try:
        connect= mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            # database = bd
        )
        print("Connection to MySQL DB successful")
    
    except Error as e:
        print(f"The error '{e}' occurred")
    return connect
# создание бд
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


# сщздание таблицы
def execute_query(connection, query):
     cursor = connection.cursor()
     try:
         cursor.execute(query)
         connection.commit()
         print("Query executed successfully")
     except Error as e:
         print(f"The error '{e}' occurred")

# выборка
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

connection = create_connection("localhost","root","1234567890")

# execute_query(connection, """
# CREATE TABLE posts (
#   id INT AUTO_INCREMENT, 
#   title TEXT NOT NULL, 
#   description TEXT NOT NULL, 
#   user_id INTEGER NOT NULL, 
#   PRIMARY KEY (id)
# ) ENGINE = InnoDB
# """)
# execute_query(connection, """
# CREATE TABLE user (
#   id INT AUTO_INCREMENT, 
#   name TEXT NOT NULL, 
#   age int NOT NULL, 
#   gender text,
#   nationality text,
#   PRIMARY KEY (id)
# ) ENGINE = InnoDB
# """)

# execute_query(connection, """
# INSERT INTO
#   `user` (`name`, `age`, `gender`, `nationality`)
# VALUES
#   ('James', 25, 'male', 'USA'),
#   ('Leila', 32, 'female', 'France'),
#   ('Brigitte', 35, 'female', 'England'),
#   ('Mike', 40, 'male', 'Denmark'),
#   ('Elizabeth', 21, 'female', 'Canada');
# """)

# users = execute_read_query(connection, "SELECT * FROM user")
# print(users)

# execute_query(connection,  """
# UPDATE
#   posts
# SET
#   description = "The weather has become pleasant now"
# WHERE
#   id = 2
# """)

# execute_query(connection, "DELETE FROM comments WHERE id = 5")

# create_database(connection, "CREATE DATABASE aaaa")