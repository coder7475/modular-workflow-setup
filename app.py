from src.logger import logging

def test_logger():
    try:
        # Test different logging levels
        logging.info("This is an info message")
        logging.warning("This is a warning message")
        logging.error("This is an error message")
        
        # Test logging with some calculations
        x = 10
        y = 0
        try:
            result = x / y
        except Exception as e:
            logging.error(f"Error in division: {e}")
            
        # Test logging with file operations    
        try:
            with open("nonexistent.txt", "r") as f:
                content = f.read()
        except Exception as e:
            logging.error(f"Error reading file: {e}")
            
        logging.info("Logger testing completed successfully")
        
    except Exception as e:
        logging.error(f"Error in test_logger: {e}")

if __name__ == "__main__":
    logging.info("Starting logger test application")
    test_logger()
    logging.info("Application execution completed")
