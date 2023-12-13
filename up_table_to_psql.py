import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# Replace these variables with your PostgreSQL credentials
db_user = "myuser"
db_password = "mypassword"
db_host = "localhost"
db_port = "5432"
db_name = "mpes"

# Create a connection to PostgreSQL
conn = psycopg2.connect(
    user=db_user,
    password=db_password,
    host=db_host,
    port=db_port,
    database=db_name
)

# Read data from Excel file
excel_file = "tabela_resultante.xlsx"
df = pd.read_excel(excel_file)

# Replace NaN values with an empty string
df = df.fillna("")

# Create an SQLAlchemy engine and append the DataFrame to the "gera_certidao" table
engine = create_engine(f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")
df.to_sql("gera_certidao", engine, if_exists='replace', index=False)

# Close the database connection
conn.close()

print("Data moved to PostgreSQL successfully.")
