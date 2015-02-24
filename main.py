import random
random.seed()

GUESTS = {
    "John": "male",
    "Maria": "female",
    "Curt": "male",
    "Josef": "male",
    "Starly": "female",
    "Anna": "female"
}
FAILURE_RATES = {"normal": 0.1, "sturdy": 0.05}

class Capsule():
    def __init__(self, type, guest=None, clean=True, broken=False):
        self.type = type
        self.failure_rate = FAILURE_RATES[type]
        self.guest = guest
        self.clean = clean
        self.broken = broken

class Person():
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

def assign_guest(guest, room):
    if room.clean and not room.broken:
        room.guest = guest
        return True
    else:
        return False

def remove_guest(room):
    if room.guest:
        room.guest = None
        room.clean = False
        if random.random() < room.failure_rate:
            room.broken = True