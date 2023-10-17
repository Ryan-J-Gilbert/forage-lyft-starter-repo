from abc import ABC, abstractmethod
from typing import date, int
from car import Car
from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex

class CarFactory(ABC):
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        return Calliope(current_date, last_service_date, current_mileage, last_service_mileage)
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        return Glissade(current_date, last_service_date, current_mileage, last_service_mileage)
    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool) -> Car:
        return Palindrome(current_date, last_service_date, warning_light_on)
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        return Rorschach(current_date, last_service_date, current_mileage, last_service_mileage)
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        return Thovex(current_date, last_service_date, current_mileage, last_service_mileage)