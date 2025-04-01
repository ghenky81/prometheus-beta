import logging
import pytest
import time
from src.function_logger import log_execution

# Create a custom logger for testing
class MockLogger:
    def __init__(self):
        self.logs = []
    
    def info(self, msg):
        self.logs.append(('info', msg))
    
    def error(self, msg):
        self.logs.append(('error', msg))

def test_log_execution_basic():
    """Test basic logging functionality"""
    mock_logger = MockLogger()
    
    @log_execution(logger=mock_logger)
    def test_func(x, y):
        return x + y
    
    # Call the function
    result = test_func(3, 4)
    
    # Check the result
    assert result == 7
    
    # Check logs
    assert len(mock_logger.logs) >= 4  # start, args, end, time logs
    assert any('Starting execution of test_func' in log[1] for log in mock_logger.logs)
    assert any('Finished execution of test_func' in log[1] for log in mock_logger.logs)
    assert any('Execution time:' in log[1] for log in mock_logger.logs)

def test_log_execution_with_exception():
    """Test logging when an exception occurs"""
    mock_logger = MockLogger()
    
    @log_execution(logger=mock_logger)
    def error_func():
        raise ValueError("Test error")
    
    # Expect the exception to be re-raised
    with pytest.raises(ValueError, match="Test error"):
        error_func()
    
    # Check logs
    assert any('Exception in error_func' in log[1] for log in mock_logger.logs)

def test_log_execution_performance():
    """Test that logging doesn't significantly impact performance"""
    mock_logger = MockLogger()
    
    @log_execution(logger=mock_logger)
    def slow_func():
        time.sleep(0.1)  # Simulate some work
    
    # Measure execution time
    start = time.time()
    slow_func()
    total_time = time.time() - start
    
    # Performance should not add significant overhead
    assert total_time >= 0.1  # At least sleep duration
    assert total_time < 0.2   # Not much more than sleep duration
    
    # Check logs
    assert any('Execution time:' in log[1] for log in mock_logger.logs)

def test_log_execution_preserves_function_metadata():
    """Test that decorator preserves function metadata"""
    @log_execution()
    def example_func(x, y):
        """A test function"""
        return x + y
    
    # Check that metadata is preserved
    assert example_func.__name__ == 'example_func'
    assert example_func.__doc__ == 'A test function'