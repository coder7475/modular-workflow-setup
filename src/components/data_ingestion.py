import os, sys
import panda as pd
import numpy as np
from src.logger import logger
from src.exception import CustomException
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path = os.path.join( )