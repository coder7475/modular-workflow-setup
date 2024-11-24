from src.logger import logging
from src.exception import CustomException
import os, sys
import pickle

def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e, sys)

def load_object(file_path):
    try:
        with open(file_path, "rb") as file_objt:
            return pickle.load(file_objt)
    except Exception as e:
        raise CustomException(e, sys)