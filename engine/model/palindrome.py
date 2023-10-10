from datetime import datetime
from engine.sternman_engine import SternmanEngine

class Palindrome(SternmanEngine):
    def __init__(self, last_service_date, warning_light_is_on, sternman_criteria, spindler_criteria):
        super().__init__(last_service_date, warning_light_is_on, sternman_criteria)
        self.palindrome_engine_criteria = super().service_criteria(sternman_criteria)
        self.palindrome_battery_criteria = super().service_criteria(spindler_criteria)

    def needs_service(self):
        today = datetime.today().date()
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date + self.palindrome_battery_criteria)
        if service_threshold_date < today or self.engine_should_be_serviced:
            return True
        else:
            return False
