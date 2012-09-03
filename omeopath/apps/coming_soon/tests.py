import time
from django.test import TestCase
import timestamp_encoder as edr


unix_time, code = (1346710595.9632721, "psjhfpzdud")

class TimestampEncoderTest(TestCase):
    def test_encode(self):
        self.assertEqual(edr.encode(unix_time), code)
        self.assertEqual(edr.encode(), edr.encode(time.time())) #test argument default
        
    def test_decode(self):
        self.assertEqual(edr.decode(code), int(unix_time))
        
