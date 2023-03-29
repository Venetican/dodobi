import pandas as pd
import numpy as np
import datetime as dt

class transform_table:
    """
    control class with methods to transform the whole dataframe
    """
    def load_df_and_convert(df: pd.DataFrame) -> pd.DataFrame:
        """
        method which returns properly converted dataframe
        -> try to convert object to datetime
        -> try to convert bool to object (string)
        -> try to convert _id type of column to int
        """
        for col in df.columns:
            try:
                if df[f'{col}'].dtype == 'object':
                    try:
                        df[f'{col}'] = pd.to_datetime(df[f'{col}'])
                    except ValueError:
                        pass
                if df[f'{col}'].dtype == 'bool':
                    try:
                        df[f'{col}'] = df[f'{col}'].map({True: 'True', False: 'False'})
                    except ValueError:
                        pass
                if '_id' in col:
                    try:
                        df[f'{col}'] = df[f'{col}'].astype(int)
                    except ValueError:
                        pass
            except ValueError:
                pass
        return df
    
    def drop_all_tmp_columns(df:pd.DataFrame) -> pd.DataFrame:
        """
        method which returns dataframe without tmp columns
        """
        df_list = df.filter(like='_tmp').columns.to_list()
        for tmp_column in df_list:
            df = df.drop(tmp_column,axis=1)
        return df
    
class transform_time:
    """
    control class with methods to obtain current time
    """
    def get_current_date() -> str:
        """
        method which returns current time in string format 
        """
        current_time = dt.datetime.now().date().strftime("%Y-%m-%d")
        return current_time


