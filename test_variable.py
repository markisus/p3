from variable import VariableType
import unittest

class VariableTest(unittest.TestCase):
    def test_float(self):
        result = VariableType.Float.parse_bytes(b'\xc2g\xae\x14')
        print(result)

    def test_int(self):
        result = VariableType.Int.parse_bytes(b'\x00\x00\x00\x00')
        print(result)

    def test_bool(self):
        result = VariableType.Bool.parse_bytes(b'\x00\x00\x00\x00')
        print(result)
    
if __name__ == '__main__':
    unittest.main()
