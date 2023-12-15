import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# Replace these variables with your PostgreSQL credentials
db_user = "user_geracertidao"
db_password = "g3rac3rtida0"
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

# Create an SQLAlchemy engine and retrieve data from the "gera_certidao" table into a DataFrame
engine = create_engine(f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")
query = "SELECT * FROM gera_certidao"
df = pd.read_sql_query(query, engine)

# Close the database connection
conn.close()

# Display the DataFrame
print(df)
