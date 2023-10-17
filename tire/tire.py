from abc import ABC


class Tire(ABC):
    def needs_service(self, sensor_array):
        pass