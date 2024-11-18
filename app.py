from src.logger import logging

def main():
    try:
        logging.info("Starting the main function")        

        # Simulate some application steps
        logging.info("Initialize the application")
        x = 5
        y = 10

        logging.info(f"Performing {x} + {y}")
        result = x + y

        logging.info(f"Result: {result}")

        # Simulate a warning
        if result > 10:
            logging.warning(f"Result {result} is greater than 10")

    except Exception as e:
        logging.error("An error occurred in main function", exec_info=True)
        raise e


if __name__ == "__main__":
    logging.info("="*50)
    logging.info("Starting logger test application")
    logging.info("="*50)

    try:
        main()
        logging.info("Application execution completed")        
    except Exception as e:
        logging.error("Application failed", exc_info=True)
    finally:
        logging.info("="*50)
        logging.info("Application execution ended!")
        logging.info("="*50)
