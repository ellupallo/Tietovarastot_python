from flask import Flask, render_template, request, redirect
import mysql.connector
from sqlalchemy import create_engine

#Intialisoidaan ohjelma Flask-applikaatioksi:
app = Flask (__name__) # __name__ n paikalle menee tiedoston nimen etuosa

# LUO sql-yhteys ja kursori muuttujiin
# TEE phpMyAdminilla tyhjä taskDB-tietokanta. >>> täällä sit se mySQL
# AJA KÄSKY, JOKA LUO TAULUN tasks SEURAAVASTI:
# id INT AUTO_INCREMENT PRIMARY KEY
# task VARCHAR("%%)
# status BOOLEAN (ei käytetä, mutta harjoituksena)


# Connect to the MySQL database
connection = mysql.connector.connect(
    host="localhost",  # Replace with your MySQL host (e.g., 'localhost' or an IP address)
    user="oka",  # Replace with your MySQL username
    password="Vesseli",  # Replace with your MySQL password
    database="tasks"  # Your database name
)

# Create a cursor object to interact with the database
cursor = connection.cursor()

# SQL query to create the 'tasks' table
create_table_query = """
CREATE TABLE IF NOT EXISTS tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Auto-incrementing primary key for the 'id' column
    task VARCHAR(255) NOT NULL,         -- 'task' column with a maximum length of 255 characters
    status BOOLEAN DEFAULT FALSE        -- 'status' column, boolean type with default value False
);
"""

# Execute the query to create the table
cursor.execute(create_table_query)

# Commit the changes to the database (in case any schema changes were made)
connection.commit()


@app.route('/')
def index():
    # Hae kaikki taskit SELECT-lauseella
    # aseta tulos tasks-muuttujaan
    # return render_template("index.html", all_tasks=[(0, "SIIVOA", False), (1, "TISKAA", False)]) # hakee oletuksena templates-kansiosta
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()       
    return render_template("index.html", all_tasks=tasks) # hakee oletuksena templates-kansiosta

@app.route("/add", methods=["POST"]) # voisi olla myös ["GET", "POST"]
def add_task():
    task = request.form["task"] # mitä käyttäjä kirjoitti kenttään
    insert_task_query = """
    INSERT INTO tasks(task, status)
    VALUES (%s,%s) """
    cursor.execute(insert_task_query, (task, False)) # tuple, siksi pilkku
    connection.commit()
    return redirect("/") # päivitetään data lataamalla pääsivu uudelleen

@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    cursor.execute("DELETE FROM tasks WHERE id=%s", (task_id,)) # tuple!! eu tarvitse 0 tai False, koska kaikki poistetaan
    connection.commit()
    return redirect("/")


    cursor.close()
    connection.close()


if __name__ == '__main__':
    app.run(debug=True) #debug=True toimii, jos ajetaan python app.py
    # jos ajetaan flask-komennolla, pitää ajaa flask run --debug


# # Close the cursor and connection
# cursor.close()
# connection.close()