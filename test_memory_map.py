import memory_map
import unittest

class MemoryMapTest(unittest.TestCase):
    def setUp(self):
        self.lookup = memory_map.generate_lookup()

    def test_player_lookup(self):
        for i in range(4):
            locations = memory_map.generate_locations_for_player(i)
            for variable, location in locations:
                lookuped_player, lookuped_variable = self.lookup[location]
                self.assertEqual(variable, lookuped_variable)
                self.assertEqual(i, lookuped_player)

    def tearDown(self):
        pass
    
if __name__ == '__main__':
    unittest.main()
