import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

def read_data_from_database(db_name):
    # Assuming you have already set up your database connection here
    # Replace 'username', 'password', 'host', 'port', and 'database_name' with your database credentials
    engine = create_engine(f"postgresql+psycopg2://username:password@host:port/database_name")
    
    # Assuming your table is named 'repositories' and has columns 'language', 'repository_count', and 'avg_stars'
    query = f"SELECT * FROM repositories;"
    
    # Execute the SQL query and read the data into a Pandas DataFrame
    df = pd.read_sql_query(query, engine)
    
    return df

def draw_data_graphs(db_name):
    df = read_data_from_database(db_name)   
    # plotting the number of repositories per language
    plt.figure(figsize=(12, 6))
    plt.bar(df['language'], df['repository_count'])
    plt.xlabel('programming language')
    plt.ylabel('repository count')
    plt.title('number of repositories per Language')
    plt.xticks(rotation=90)
    plt.show()

    # plotting the distribution of star counts per language
    plt.figure(figsize=(12, 6))
    plt.boxplot([df[df['language'] == lang]['avg_stars'] for lang in df['language']])
    plt.xlabel('programming Language')
    plt.ylabel('star count')
    plt.title('distribution of star counts per language')
    plt.xticks(range(1, len(df['language']) + 1), df['language'], rotation=90)
    plt.show()

# Call the function with the appropriate database name
draw_data_graphs('your_database_name')


