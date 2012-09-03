import time


ENCODING_KEY = "zpwsjdhfru"

def encode(unix_time=None):
    """
    Encode UNIX timestamp.
    unix_time: a float or integer.
    return the code.
    """
    unix_time = int(unix_time or time.time())
    digits = map(int, str(unix_time))
    encoded_digits = map(ENCODING_KEY.__getitem__, digits)
    return ''.join(encoded_digits)
    
def decode(code):
    """Decode to an integer UNIX timestamp."""
    digits = map(ENCODING_KEY.index, code)
    return reduce(lambda a, b: 10 * a + b, digits)  #concatenate the digits
    
