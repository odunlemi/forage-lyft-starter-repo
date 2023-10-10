from abc import ABCMeta
from car import Car

class SternmanEngine(Car, ABCMeta):
    def __init__(self, last_service_date, warning_light_is_on, sternman_criteria):
        super().__init__(last_service_date)
        super().service_criteria(sternman_criteria)
        self.warning_light_is_on = warning_light_is_on

    def engine_should_be_serviced(self):
        if self.warning_light_is_on:
            return True
        else:
            return False
