from datetime import datetime
from engine.willoughby_engine import WilloughbyEngine

class Rorschach(WilloughbyEngine):
    def __init__(self, last_service_date, current_mileage, last_service_mileage, willoughby_criteria, nubbin_criteria):
        super().__init__(last_service_date, current_mileage, last_service_mileage)
        self.rorschach_engine_criteria = super().service_criteria(willoughby_criteria)
        self.rorschach_battery_criteria = super().service_criteria(nubbin_criteria)

    def needs_service(self):
        today = datetime.today().date()
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date + self.rorschach_battery_criteria)
        if service_threshold_date < today or self.engine_should_be_serviced():
            return True
        else:
            return False

