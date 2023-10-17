from abc import ABCMeta

class Engine(ABCMeta):
    def needs_service(self):
        pass
