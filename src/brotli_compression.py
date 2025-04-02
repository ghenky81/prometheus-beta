import brotli
from typing import Union, Optional


def brotli_compress(data: Union[str, bytes], quality: int = 11) -> bytes:
    """
    Compress data using Brotli compression algorithm.

    Args:
        data (Union[str, bytes]): The input data to compress. 
                                  Can be a string or bytes.
        quality (int, optional): Compression level (0-11). 
                                 Defaults to 11 (maximum compression).

    Returns:
        bytes: Compressed data in Brotli format.

    Raises:
        TypeError: If input is not str or bytes.
        ValueError: If compression quality is out of range.
    """
    # Validate input type
    if not isinstance(data, (str, bytes)):
        raise TypeError("Input must be str or bytes")

    # Convert string to bytes if necessary
    if isinstance(data, str):
        data = data.encode('utf-8')

    # Validate compression quality
    if not 0 <= quality <= 11:
        raise ValueError("Compression quality must be between 0 and 11")

    # Compress data using Brotli
    try:
        compressed_data = brotli.compress(data, quality)
        return compressed_data
    except Exception as e:
        raise RuntimeError(f"Compression failed: {str(e)}")


def brotli_decompress(compressed_data: bytes) -> bytes:
    """
    Decompress Brotli compressed data.

    Args:
        compressed_data (bytes): Brotli compressed data.

    Returns:
        bytes: Decompressed original data.

    Raises:
        TypeError: If input is not bytes.
        ValueError: If decompression fails.
    """
    # Validate input type
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")

    # Decompress data using Brotli
    try:
        decompressed_data = brotli.decompress(compressed_data)
        return decompressed_data
    except Exception as e:
        raise ValueError(f"Decompression failed: {str(e)}")