import unittest
from datetime import datetime

from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire

class TestCarriganTire(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        sensor_array = [0.9,0.9,0.9,0.9]
        tire = CarriganTire(sensor_array)
        self.assertTrue(tire.needs_service())
    def test_tire_shouldnt_be_serviced(self):
        sensor_array = [0.1,0.2,0.1,0]
        tire = CarriganTire(sensor_array)
        self.assertFalse(tire.needs_service())

class TestOctoprimeTire(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        sensor_array = [0.9,0,0,0]
        tire = OctoprimeTire(sensor_array)
        self.assertTrue(tire.needs_service())
    def test_tire_shouldnt_be_serviced(self):
        sensor_array = [0.8,0.8,0.8,0]
        tire = OctoprimeTire(sensor_array)
        self.assertFalse(tire.needs_service())

if __name__ == '__main__':
    unittest.main()