# Käytä esim us-500.csv -tiedostoa
# Lue tiedosto datagrameen ja koita viedä mysql-tietokantaan

# 1) Lue tiedosto pandas df:ään v
# 2) Muodosta yhteys mysql-kantaan v
# 3) Luo taulu (jos sitä ei ole ko. kannassa) tai lue taulu phpMyAdminissa v
# 4) Käy df läpi rivi riviltä ja lisää sql:n INSERT -komennolla rivit kannan tauluun

import pandas as pd
import mysql.connector

myus5002df = pd.read_csv("us-500.csv")
print(myus5002df.head(5))

connection = mysql.connector.connect(
    host="localhost",
    user="oka",
    password="Vesseli",
    database="us500"
)
cursor = connection.cursor()

# cursor.execute("DROP TABLE IF EXITS allemployees") >>> tällainen voi olla varmuuden vuoksi

create_table = ("CREATE TABLE IF NOT EXISTS allemployees \
               (first_name TEXT, \
                last_name TEXT, \
                company_name TEXT, \
                address TEXT, \
                city TEXT, \
                county TEXT, \
                state TEXT, zip TEXT,  phone1 TEXT, phone2 TEXT, email TEXT, web TEXT)")

cursor.execute(create_table)

for _, row in myus5002df.iterrows():
    insert_query = """
    INSERT INTO allemployees (first_name, last_name, company_name, address, city, county, state, zip, phone1, phone2, email, web)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(insert_query, tuple(row))

# for i, row in myus5002df.iterrows():
#     insert_query = """
#     INSERT INTO allemployees.data (first_name, last_name, company_name, address, city, county, state, zip, phone1, phone2, email, web)
#     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#     """
    cursor.execute(insert_query, tuple(row))



# # Vaihtoehtoinen, TSEKKAA TÄMÄ
# for row in myus5002df.itertuples(index=False, name=None):
#     sql = "INSERT INTO employees.employee_data VALUES()"


# Commit the transaction
connection.commit()

# Close the connection
cursor.close()
connection.close()