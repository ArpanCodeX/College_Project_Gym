import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="system",
    database="gymDB_1"
)

cursor = conn.cursor()

create_table_query = """
CREATE TABLE users (
    id INT NOT NULL AUTO_INCREMENT COMMENT 'Primary Key',
    name VARCHAR(255) NOT NULL COMMENT 'User Name',
    password VARCHAR(255) NOT NULL COMMENT 'User Password',
    create_time DATETIME COMMENT 'Create Time',
    PRIMARY KEY (id)
) COMMENT='done';
"""

cursor.execute(create_table_query)

print("Table 'users' created successfully.")

cursor.close()
conn.close()
