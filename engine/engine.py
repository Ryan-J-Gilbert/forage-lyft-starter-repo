from abc import ABC, abstractmethod

class Engine(ABC):
    # @abstractmethod
    def needs_service(self, last_service_date):
        self.last_service_date = last_service_date
