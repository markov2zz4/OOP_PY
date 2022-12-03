from dataclasses import dataclass


@dataclass
class Location:
    name: str
    longitude: float = 0.0
    latitude: float = 11.5


location = Location(name="Stonehenge", longitude=51, latitude=1.5)
print(location.name, location.longitude, location.latitude)