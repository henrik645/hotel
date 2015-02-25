import random, curses
random.seed()

VERSION = "0.1"
GUESTS = {
    "John": "male",
    "Maria": "female",
    "Curt": "male",
    "Josef": "male",
    "Starly": "female",
    "Anna": "female"
}
FAILURE_RATE = 0.1

class Room():
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

def init():
    print("Hotel Simulator " + VERSION)
    print("Welcome!")
    print("")
    hotel_name = input("Hotel name: ")
    print("")
    print("You are a hotel owner. Your goal is to make as much money as possible without going bankrupt.")
    
def day(number):
    for i in range(30):
        print("")
    
    print("Day " + str(number))
    time.sleep(2)
    for i in range(30):
        print(hh)

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(1)

screen.addstr(0, 0, "Test", curses.A_REVERSE)
screen.refresh()

curses.nocbreak()
curses.echo()
screen.keypad(0)