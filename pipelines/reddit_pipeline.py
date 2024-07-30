from utils.constants import CLIENT_ID, SECRET,OUTPUT_PATH
from etls.reddit_etl import connect_reddit, extract_post, load_data_to_csv
import pandas as pd
from etls.reddit_etl import transform_data


def reddit_pipeline(file_name:str,subreddit:str,time_filter='day',limit = None):
    #connecting to reddit instance 
    instance = connect_reddit(CLIENT_ID, SECRET,'Airscholar Agent')

     
    #doing extraction
    posts = extract_post (instance, subreddit,time_filter,limit)
    post_df = pd.DataFrame(posts)

    #doing transformation

    post_transform_df = transform_data(post_df)
 
    #doing loading to csv
    file_path = f'{OUTPUT_PATH}/{file_name}.csv'
    load_data_to_csv(post_transform_df, file_path)
    
    return file_path