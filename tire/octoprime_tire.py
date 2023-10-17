from tire.tire import Tire


class OctoprimeTire(Tire):
    def __init__(self, sensor_array):
        self.sensor_array = sensor_array


    def needs_service(self):
        return any([i >= 0.9 for i in self.sensor_array])