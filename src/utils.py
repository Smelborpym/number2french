import json
import pandas as pd
from os.path import join

def load_from_file(file_path):
    """
    Load a list of numbers from a JSON file.
    (The file should have the numbers stored
    under a key named 'numbers')

    :param file_path: Path to the JSON file.
    :return: List of numbers.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        if 'numbers' not in data:
            raise ValueError("Missing 'numbers' key")

        numbers = data['numbers']

        if not isinstance(numbers, list):
            raise ValueError("'numbers' must be associated with a list")

        return numbers
    
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON file: {e}")
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")

def save_to_file(output_data, file_path, lang_key):
    """
    Save the output data to a JSON file. 
    (The list of words is saved under 
    a key named after the input language)

    :param output_data: The data to be saved.
    :param file_path: Path to the directory where the file will be saved.
    :param file_name: The name of the file to be saved.
    :param lang_key: The key under which the data should be saved.
    """
    try:
        with open(file_path, 'x', encoding='utf-8') as file:
            json.dump({lang_key: output_data}, file, indent=4, ensure_ascii=False)
    except IOError as e:
        raise IOError(f"Could not write to file '{file_path}': {e}")

def load_labeled(json_file):
    try:
        df = pd.read_json(json_file)
        expected_columns = ["numbers", "french", "belgian"]
        if all(col in df.columns for col in expected_columns):
            return df
        else:
            raise ValueError("File does not have the expected columns.")

    except Exception as e:
        print(f"Error loading JSON file: {str(e)}")
        return None

