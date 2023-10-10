from abc import ABCMeta
from car import Car

class WilloughbyEngine(Car, ABCMeta):
    def __init__(self, last_service_date, current_mileage, last_service_mileage, willoughby_criteria):
        super().__init__(last_service_date)
        super().service_criteria(willoughby_criteria)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def engine_should_be_serviced(self):
        return self.current_mileage - self.last_service_mileage > self.change_service_criteria(self.willoughby_criteria)
