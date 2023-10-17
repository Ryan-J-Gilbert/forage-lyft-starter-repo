from abc import ABC


class Engine(ABC):
    def needs_service(self, last_service_date):
        pass