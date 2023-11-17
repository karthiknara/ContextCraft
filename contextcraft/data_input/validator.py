# contextcraft/data_input/validator.py

import pandas as pd


def check_missing_values(df):
    """
    Check for missing values within the DataFrame.

    Parameters:
    df (pd.DataFrame): The DataFrame to check for missing values.

    Returns:
    dict: A dictionary with column names as keys and counts of missing values as values.
    """
    missing_values = df.isnull().sum()
    return missing_values[missing_values > 0].to_dict()


def validate_data_types(df, expected_dtypes):
    """
    Validate the data types of the DataFrame's columns against expected data types.

    Parameters:
    df (pd.DataFrame): The DataFrame to validate.
    expected_dtypes (dict): A dictionary with column names as keys and expected dtypes as values.

    Returns:
    list: A list of messages about data type mismatches.
    """
    mismatch_info = []
    for column, expected_dtype in expected_dtypes.items():
        if column in df.columns and not pd.api.types.is_dtype_equal(df[column].dtype, expected_dtype):
            mismatch_info.append(
                f"Data type mismatch in column '{column}': Expected {expected_dtype}, got {df[column].dtype}")

    return mismatch_info

# Example usage:
# df = pd.DataFrame({...})
# expected_dtypes = {'column1': 'int64', 'column2': 'float64', ...}
# missing_values = check_missing_values(df)
# dtype_issues = validate_data_types(df, expected_dtypes)

# Handle the issues as necessary, e.g., log them, raise exceptions, etc.
