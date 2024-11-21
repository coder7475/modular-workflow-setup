# type: ignore
import os, sys
import pandas as pd
import numpy as np
from src.logger import logger
from src.exception import CustomException
from dataclasses import dataclass
from sklearn.model_selection import train_test_split 

@dataclass
class DataIngestionConfig:
    train_data_path = os.path.join("artifacts/data_ingestion", "train.csv")
    test_data_path = os.path.join("artifacts/data_ingestion", "test.csv")
    raw_data_path = os.path.join("artifacts/data_ingestion", "raw.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            data = pd.read_csv(os.path.join("data_sources", "adult.csv"))

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path, index=False)

            train_set, test_set = train_test_split(data, test_size=.20, random_state=42)

        except Exception as e:
            