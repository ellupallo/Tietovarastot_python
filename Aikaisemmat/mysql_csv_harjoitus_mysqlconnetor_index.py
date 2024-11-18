## TÄMÄ EI VALMISTUNUT!!!!!!!!!!

import pandas as pd
import mysql.connector

myus5002df_ind = pd.read_csv("us-500.csv")

myus5002df_ind.reset_index(inplace=True)
myus5002df_ind.rename(columns={"index": "id"}, inplace=True)
print(myus5002df_ind.head(5))

connection = mysql.connector.connect(
    host="localhost",
    user="oka",
    password="Vesseli",
    database="us500"
)
cursor = connection.cursor()

create_table = ("CREATE TABLE IF NOT EXISTS allempl_mysql_ind \
               (id INT PRIMARY KEY, \
                first_name TEXT, \
                last_name TEXT, \
                company_name TEXT, \
                address TEXT, \
                city TEXT, \
                county TEXT, \
                state TEXT, zip TEXT,  phone1 TEXT, phone2 TEXT, email TEXT, web TEXT)")

cursor.execute(create_table)

for _, row in myus5002df_ind.iterrows():
    insert_query = """
    INSERT INTO allempL_mysql_ind (id, first_name, last_name, company_name, address, city, county, state, zip, phone1, phone2, email, web)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(insert_query, tuple(row))

# # Commit the transaction
# connection.commit()

# # Close the connection
# cursor.close()
# connection.close()