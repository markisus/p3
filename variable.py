from enum import Enum
from collections import namedtuple
import struct

Variable = namedtuple('Variable', ['name', 'type'])
class VariableType(Enum):
    Int = 1
    Bool = 2
    Float = 3

    def parse_bytes(self, data):
        if self.name == 'Int':
            return struct.unpack('>L', data)[0]
        if self.name == 'Bool':
            return bool(struct.unpack('>L', data)[0])
        if self.name == 'Float':
            return struct.unpack('>f', data)[0]
        
