import time
import logging

# Configuramos el logger
logging.basicConfig(level=logging.INFO, format="%(asctime)s-%(levelname)s-%(message)s")

def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        logging.info(f"{func.__name__} ejecutada en {elapsed_time:.4f} seconds")
        return result
    return wrapper

def logit(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Corriendo {func.__name__}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} completada")
        return result
    return wrapper
