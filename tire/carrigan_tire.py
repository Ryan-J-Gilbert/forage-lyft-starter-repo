from tire.tire import Tire


class CarriganTire(Tire):
    def __init__(self, sensor_array):
        self.sensor_array = sensor_array


    def needs_service(self):
        return sum(self.sensor_array) >= 3