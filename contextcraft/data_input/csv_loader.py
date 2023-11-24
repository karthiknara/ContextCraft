# contextcraft/data_input/csv_loader.py

import pandas as pd
import os
from .validator import check_missing_values, validate_data_types


def load_csv(file_path, delimiter=',', quotechar='"', encoding='utf-8', skipinitialspace=True):
    """
    Load a CSV file and return a pandas DataFrame.

    Parameters:
    file_path (str): The path to the CSV file to be loaded.
    delimiter (str): The delimiter used in the CSV file.
    quotechar (str): The character used to quote fields containing special characters.
    encoding (str): The encoding format used in the CSV file.
    skipinitialspace (bool): Skip spaces after delimiter.

    Returns:
    pd.DataFrame: DataFrame containing the contents of the CSV file.
    """

    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file specified does not exist: {file_path}")

    # Check if the file has a CSV extension
    if not file_path.lower().endswith('.csv'):
        raise ValueError(f"The file specified does not have a CSV extension: {file_path}")

    try:
        # Attempt to read the CSV file into a DataFrame
        df = pd.read_csv(
            file_path,
            delimiter=delimiter,
            quotechar=quotechar,
            encoding=encoding,
            skipinitialspace=skipinitialspace
        )

        # Basic validation to check if the DataFrame is empty
        if df.empty:
            raise ValueError("The CSV file is empty")

        return df

    except pd.errors.EmptyDataError:
        raise ValueError("No data: The CSV file is empty")
    except pd.errors.ParserError:
        raise ValueError("Parse error: The CSV file is not formatted correctly")
    except Exception as e:
        # Handle any other exception and re-raise with a user-friendly message
        raise Exception(f"An error occurred while loading the CSV file: {e}")


# Example usage:
# try:
#     df = load_csv('path/to/your/data.csv')
# except Exception as e:
#     print(e)

def load_multiple_csv(file_paths, delimiter=',', quotechar='"', encoding='utf-8', skipinitialspace=True):
    """
    Load multiple CSV files and return a list of pandas DataFrames.

    Parameters:
    file_paths (list of str): The paths to the CSV files to be loaded.
    delimiter (str): The delimiter used in the CSV files.
    quotechar (str): The character used to quote fields containing special characters.
    encoding (str): The encoding format used in the CSV files.
    skipinitialspace (bool): Skip spaces after delimiter.

    Returns:
    list of pd.DataFrame: List containing DataFrames for each CSV file.
    """
    dataframes = []
    for file_path in file_paths:
        df = load_csv(file_path, delimiter, quotechar, encoding, skipinitialspace)
        dataframes.append(df)
    return dataframes


# Example usage for multiple CSV files:
# file_paths = ['path/to/your/data1.csv', 'path/to/your/data2.csv', ...]
# try:
#     dfs = load_multiple_csv(file_paths)
# except Exception as e:
#     print(e)

def load_and_validate_csv(file_path, delimiter=',', quotechar='"', expected_dtypes=None):
    df = load_csv(file_path, delimiter, quotechar)

    # Check for missing values
    missing_values = check_missing_values(df)
    if missing_values:
        # Handle or log missing values
        pass

    # Validate data types
    if expected_dtypes:
        dtype_issues = validate_data_types(df, expected_dtypes)
        if dtype_issues:
            # Handle or log data type issues
            pass

    return df
