from abc import ABCMeta, abstractmethod

class Serviceable(ABCMeta):
    @abstractmethod
    def needs_service(self):
        pass
