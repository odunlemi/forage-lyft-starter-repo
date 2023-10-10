from datetime import datetime
from engine.capulet_engine import CapuletEngine

class Thovex(CapuletEngine):
    def __init__(self, last_service_date, current_mileage, last_service_mileage, capulet_criteria, spindler_criteria):
        super().__init__(last_service_date, current_mileage, last_service_mileage)
        self.thovex_engine_criteria = super().service_criteria(capulet_criteria)
        self.thovex_battery_criteria = super().service_criteria(spindler_criteria)

    def needs_service(self):
        today = datetime.today().date()
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date + self.thovex_battery_criteria)
        if service_threshold_date < today or self.engine_should_be_serviced:
            return True
        else:
            return False
