import functools
import logging
import time
from typing import Callable, Any

# Configure basic logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def log_execution(logger: logging.Logger = logging.getLogger(__name__)) -> Callable:
    """
    A decorator to log function execution start and end times.
    
    Args:
        logger (logging.Logger, optional): Logger to use. Defaults to module-level logger.
    
    Returns:
        Callable: Decorated function that logs execution details.
    
    Example:
        @log_execution()
        def example_function(x, y):
            return x + y
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Log function start
            logger.info(f"Starting execution of {func.__name__}")
            logger.info(f"Args: {args}, Kwargs: {kwargs}")
            
            # Record start time
            start_time = time.time()
            
            try:
                # Execute the function
                result = func(*args, **kwargs)
                
                # Calculate and log execution time
                end_time = time.time()
                execution_time = end_time - start_time
                
                logger.info(f"Finished execution of {func.__name__}")
                logger.info(f"Execution time: {execution_time:.4f} seconds")
                
                return result
            
            except Exception as e:
                # Log any exceptions that occur
                logger.error(f"Exception in {func.__name__}: {str(e)}")
                raise
        
        return wrapper
    
    return decorator