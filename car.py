"""car module: contains the Car class"""

from abc import ABCMeta, abstractmethod
class Car(ABCMeta):
    """Car class"""
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self):
        pass
    
    @abstractmethod
    def service_criteria(self, capulet_criteria, sternman_criteria, willoughby_criteria, spindler_criteria, nubbin_criteria) -> None:
        self.capulet_criteria = 30000
        self.sternman_criteria = bool
        self.willoughby_criteria = 60000
        self.spindler_criteria = 2
        self.nubbin_criteria = 4

    @classmethod
    def add_new_car():
        pass