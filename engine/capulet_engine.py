from abc import ABCMeta
from car import Car

class CapuletEngine(Car, ABCMeta):
    def __init__(self, current_mileage, last_service_mileage, last_service_date, capulet_criteria):
        super().__init__(last_service_date)
        super().service_criteria(capulet_criteria)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def engine_should_be_serviced(self):
        return self.current_mileage - self.last_service_mileage > self.capulet_criteria
