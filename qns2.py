class clockTime:

    def __init__(self):
        self.hours = ""
        self.minutes = ""
        self.seconds = ""

    def setHours(self):
        self.hours = input("set your hours")
        if (int(self.hours)>24 or (int(self.hours) < 0)): self.setHours()
    
    def setMinutes(self):
        self.minutes= input("set your minutes")
        if (int(self.minutes)>60 or (int(self.minutes) < 0)): self.setMinutes()

    def setSeconds(self):
        self.seconds = input("set your seconds")
        if (int(self.seconds)>60 or (int(self.seconds) < 0)): self.setSeconds()

    def showTIme(self):
        print(self.hours,":",self.minutes,":",self.seconds)

clock = clockTime()

try:
    clock.setHours()
    clock.setMinutes()
    clock.setSeconds()
    clock.showTIme()
except ValueError:
    print("please enter only digits!")
