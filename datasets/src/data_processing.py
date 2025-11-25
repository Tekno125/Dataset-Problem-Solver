"""
Data Processing Module

This module contains functions for data cleaning and preprocessing.
"""

import pandas as pd
import numpy as np


def clean_data(df):
    """
    Clean the input dataframe
    
    Parameters:
    df (pandas.DataFrame): Input dataframe
    
    Returns:
    pandas.DataFrame: Cleaned dataframe
    """
    # Remove duplicates
    df = df.drop_duplicates()
    
    # Handle missing values
    df = df.fillna(method='ffill')
    
    # Add age group column
    df['age_group'] = df['age'].apply(lambda x: 'Young Adult' if x < 30 else 'Adult')
    
    return df


def load_data(filepath):
    """
    Load data from CSV file
    
    Parameters:
    filepath (str): Path to the CSV file
    
    Returns:
    pandas.DataFrame: Loaded dataframe
    """
    return pd.read_csv(filepath)


if __name__ == "__main__":
    # Example usage
    raw_df = load_data('../raw/dummy_data.csv')
    cleaned_df = clean_data(raw_df)
    cleaned_df.to_csv('../processed/cleaned_data.csv', index=False)
    print("Data processing completed!")