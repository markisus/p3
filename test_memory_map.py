import memory_map
import unittest

class MemoryMapTest(unittest.TestCase):
    def setUp(self):
        self.lookup = memory_map.generate_lookup()

    def test_player_lookup(self):
        for i in range(4):
            locations = memory_map.generate_locations_for_player(i)
            for location_name, location in locations:
                lookup_result = self.lookup[location]
                lookup_player, lookup_location_name = lookup_result
                self.assertEqual(location_name, lookup_location_name)
                self.assertEqual(i, lookup_player)

    def tearDown(self):
        pass
    
if __name__ == '__main__':
    unittest.main()
