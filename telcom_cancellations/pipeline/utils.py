import pandas as pd

def load_data_from_csv_files(file_paths):
    """
    Load data from CSV files and concatenate them into a single DataFrame.

    Parameters:
    file_paths (list): A list of file paths for CSV files.

    Returns:
    pandas.DataFrame: Concatenated DataFrame containing data from all CSV files.
    """
    data_frames = []
    for file_path in file_paths:
        df = pd.read_csv(file_path)
        data_frames.append(df)

    return pd.concat(data_frames, ignore_index=True)

def preprocess_data(data):
    """
    Preprocess the data by renaming columns and converting date and numeric columns.

    Parameters:
    data (pandas.DataFrame): The main DataFrame.

    Returns:
    pandas.DataFrame: The preprocessed DataFrame.
    """
    # Rename columns
    data.rename(columns={'customerID': 'CustomerID', 'gender': 'Gender'}, inplace=True)

    # Convert date columns
    data['BeginDate'] = pd.to_datetime(data['BeginDate'])
    data['EndDate'] = pd.to_datetime(data['EndDate'], errors='coerce')

    # Convert numeric column and fill missing values
    data['TotalCharges'] = pd.to_numeric(data['TotalCharges'], errors='coerce')
    data['TotalCharges'] = data['TotalCharges'].fillna(0)

    return data



