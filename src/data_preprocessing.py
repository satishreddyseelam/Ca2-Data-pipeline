import pandas as pd
from data_aquisition import fetch_repository_data

# Preprocessing the data
def preprocess_data(repository_data):
    extracted_data = [
        {
            'name': repo['name'],
            'language': repo['language'],
            'stars': repo['stargazers_count']
        }
        for repo in repository_data['items']
    ]
    df = pd.DataFrame(extracted_data)
    return df

