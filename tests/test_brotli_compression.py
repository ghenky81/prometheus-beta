import pytest
import brotli
from src.brotli_compression import brotli_compress, brotli_decompress


def test_brotli_compress_string():
    """Test compression of a string."""
    input_string = "Hello, Brotli compression! " * 10  # Make input large enough to compress
    compressed = brotli_compress(input_string)
    assert isinstance(compressed, bytes)
    assert len(compressed) < len(input_string.encode('utf-8'))


def test_brotli_compress_bytes():
    """Test compression of bytes."""
    input_bytes = b"Binary data compression test" * 10  # Make input large enough to compress
    compressed = brotli_compress(input_bytes)
    assert isinstance(compressed, bytes)
    assert len(compressed) < len(input_bytes)


def test_brotli_decompress():
    """Test decompression of compressed data."""
    input_string = "Hello, Brotli compression!"
    compressed = brotli_compress(input_string)
    decompressed = brotli_decompress(compressed)
    assert decompressed.decode('utf-8') == input_string


def test_brotli_compress_quality():
    """Test different compression qualities."""
    input_string = "Test compression quality " * 10  # Make input large to show compression
    compressed_default = brotli_compress(input_string)
    compressed_low = brotli_compress(input_string, quality=1)
    compressed_high = brotli_compress(input_string, quality=11)
    
    # Verify roundtrip decompression
    assert brotli_decompress(compressed_default).decode('utf-8') == input_string
    assert brotli_decompress(compressed_low).decode('utf-8') == input_string
    assert brotli_decompress(compressed_high).decode('utf-8') == input_string
    
    # Verify that different qualities produce different compressed lengths
    compressed_lengths = {
        'default': len(compressed_default),
        'low': len(compressed_low),
        'high': len(compressed_high)
    }
    
    # At least one of the compression qualities should be different
    assert len(set(compressed_lengths.values())) > 1


def test_invalid_input_type():
    """Test handling of invalid input types."""
    with pytest.raises(TypeError):
        brotli_compress(123)
    with pytest.raises(TypeError):
        brotli_decompress("not bytes")


def test_invalid_compression_quality():
    """Test handling of invalid compression quality."""
    with pytest.raises(ValueError):
        brotli_compress("test", quality=12)
    with pytest.raises(ValueError):
        brotli_compress("test", quality=-1)


def test_decompress_invalid_data():
    """Test handling of invalid compressed data."""
    with pytest.raises(ValueError):
        brotli_decompress(b"invalid compressed data")


def test_roundtrip_large_data():
    """Test compression and decompression of large data."""
    large_data = "A" * 10000
    compressed = brotli_compress(large_data)
    decompressed = brotli_decompress(compressed)
    assert decompressed.decode('utf-8') == large_data


def test_edge_cases():
    """Test edge cases like empty input."""
    empty_string = ""
    empty_bytes = b""
    
    compressed_string = brotli_compress(empty_string)
    compressed_bytes = brotli_compress(empty_bytes)
    
    assert brotli_decompress(compressed_string) == empty_string.encode('utf-8')
    assert brotli_decompress(compressed_bytes) == empty_bytes


def test_compression_modes():
    """Test different compression modes."""
    text_input = "Compression mode test" * 10
    
    # Test generic mode
    generic_compressed = brotli_compress(text_input, mode=brotli.MODE_GENERIC)
    
    # Test text mode
    text_compressed = brotli_compress(text_input, mode=brotli.MODE_TEXT)
    
    # Verify that compression worked
    assert isinstance(generic_compressed, bytes)
    assert isinstance(text_compressed, bytes)
    
    # Verify roundtrip decompression
    assert brotli_decompress(generic_compressed).decode('utf-8') == text_input
    assert brotli_decompress(text_compressed).decode('utf-8') == text_input