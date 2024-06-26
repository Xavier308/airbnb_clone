import json
import os
import logging
from flask import current_app as app
from app.extensions import db  # Import the SQLAlchemy database instance


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

def save_data(filename, data, use_database=False):
    if use_database:
        try:
            db.session.add(data)
            db.session.commit()
            logger.info("Data successfully saved to database")
        except Exception as e:
            logger.error(f"Failed to save data to database: {e}")
            raise
    else:
        try:
            storage_path = app.config['JSON_STORAGE_PATH']
            ensure_path_exists(storage_path)
            filepath = f"{storage_path}/{filename}.json"
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            logger.info(f"Data successfully saved to {filepath}")
        except Exception as e:
            logger.error(f"Failed to save data to {filename}.json: {e}")
            raise

def load_data(model_class, filename=None, use_database=False):
    if use_database:
        try:
            return model_class.query.all()
        except Exception as e:
            logger.error(f"Failed to load data from database: {e}")
            raise
    else:
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
