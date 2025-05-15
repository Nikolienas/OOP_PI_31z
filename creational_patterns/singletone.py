
class SingletoneMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class GameSettings(metaclass=SingletoneMeta):
    def __init__(self):
        self.volume = None
        self.difficulty = None

    @classmethod
    def get_instance(cls):
        return cls()


settings1 = GameSettings.get_instance()
settings2 = GameSettings.get_instance()

print(settings1 is settings2)

settings1.volume = 70
settings1.difficulty = "Hard"

print(settings2.volume)
print(settings2.difficulty)
    