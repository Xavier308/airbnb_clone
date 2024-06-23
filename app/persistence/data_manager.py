import json
import os
import logging
from flask import current_app as app

# Ensures that logs from this module do not interfere with Flask's logs
logger = logging.getLogger('data_manager')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def ensure_path_exists(path):
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)
        logger.info(f"Created directory {path}")

def save_data(filename, data):
    try:
        storage_path = app.config['JSON_STORAGE_PATH']
        ensure_path_exists(storage_path)
        filepath = f"{storage_path}/{filename}.json"
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)  # ensure_ascii=False to save characters as is
        logger.info(f"Data successfully saved to {filepath}")
    except Exception as e:
        logger.error(f"Failed to save data to {filename}.json: {e}")
        raise

def load_data(filename):
    try:
        filepath = f"{app.config['JSON_STORAGE_PATH']}/{filename}.json"
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        logger.warning(f"{filename}.json not found, returning empty list.")
        return []
    except Exception as e:
        logger.error(f"Failed to load data from {filename}.json: {e}")
        raise
