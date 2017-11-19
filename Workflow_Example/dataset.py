import pandas as pd
import numpy as np

'''
Some functions for loading a dataset and performing simple data preparation
'''


def load_dataset(filename, filetype='csv', header=True):
    '''
    Loads a dataset from file

    Parameters:
    -----------
    filename: str
        Name of data file
    filetype: str
        The type of data file (csv, tsv)
    Returns:
    --------
    DataFrame
        Dataset as pandas DataFrame
    '''

    in_file = open(filename)
    data = []
    header_row = ''

    # Read the file line by line into instance structure
    for line in in_file.readlines():

        # Skip comments
        if not line.startswith("#"):

            # TSV file
            if filetype == 'tsv':
                if header:
                    header_row = line.strip().split('\t')
                else:
                    raw = line.strip().split('\t')

            # CSV file
            elif filetype == 'csv':
                if header:
                    header_row = line.strip().split(',')
                else:
                    raw = line.strip().split(',')

            # Neither = problem
            else:
                print('Invalid file type')
                exit()

            # Append to dataset appropriately
            if not header:
                data.append(raw)
            header = False

    # Build a new dataframe of the data instance list of lists and return
    df = pd.DataFrame(data, columns=header_row)
    return df


def to_numeric(dataset, attr_name):
    '''
    Performs a simple categorical to numeric attribute value transformation

    Parameters:
    -----------
    dataset: DataFrame
        Dataset on which to perform transformation
    attr_name: str
        Dataset attribute name to convert from nominal to numeric values
    Returns:
    --------
    DataFrame
        DataFrame of with data transformation performed
    dict
        Python dictionary of attribute name to integer mappings
    '''

    # Get unique entries in column
    unique_vals = dataset[attr_name].unique()

    # Create dict
    val_dict = {}
    for val in unique_vals:
        if not val in val_dict:
            val_dict[val] = len(val_dict)

    # Replace values in attr_name col as per dict
    dataset[attr_name].replace(val_dict, inplace=True)
    # print val_dict
    # Return dataset and value dictionary
    return dataset, val_dict


def from_str(dataset, attrs):
    '''
    Performs numeric values stored as strings to numeric value transformation

    Parameters:
    -----------
    dataset: DataFrame
        Dataset on which to perform transformation
    attr_name: str
        Dataset attribute name to convert from strings to equivalent numeric values

    Returns:
    --------
    DataFrame
        DataFrame with data transformation performed
    '''

    # Make conversions on list of attributes
    if type(attrs) == list:
        for attr_name in attrs:
            dataset[attr_name] = dataset[attr_name].astype(float)

    # Make conversion on single attribute
    else:
        dataset[attrs] = dataset[attrs].astype(float).fillna(0.0)

    # Return dataset after conversion
    return dataset


def to_matrix(dataset):
    '''
    Converts a pandas DataFrame dataset to a numpy matrix representation

    Parameters:
    -----------
    dataset: DataFrame
        Dataset to convert to matrix representation
    Returns:
    --------
    ndarray
        numpy ndarray representation of dataset
    '''

    return dataset.as_matrix()