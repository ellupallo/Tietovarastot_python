from sqlalchemy import create_engine
import pandas as pd

# Assuming your DataFrame is loaded as myus5002df
myus5002df2 = pd.read_csv("us-500.csv")

# Replace with your actual MySQL credentials
engine = create_engine("mysql+mysqlconnector://oka:Vesseli@localhost/us500")

# Write DataFrame to MySQL table
myus5002df2.to_sql("employees_index", engine, if_exists="replace", index=True)
