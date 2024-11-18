import sys
from src.logger import logging
from src.exception import CustomException

def call_examp():
    try:
        x = 10
        y = 0
        result = x / y
        logging.info(f"{result}")
    except Exception as e: 
        logging.info("Error Raised")
        raise CustomException(e, sys)

if __name__ == "__main__":
    logging.info("Starting application")

    try:
        call_examp()        
        logging.info("Application execution completed")        
    except CustomException as e:
        logging.error("Application failed", exc_info=True)
        print(e)
        raise e
   