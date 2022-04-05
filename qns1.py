class calculator:

    def __init__(self):
        self.sum=0

    def adder(self):
        print("-----adding------")
        input1 = int(input("number 1:"))
        input2 = int(input("number 2:"))
        print("adding to sum:", (input1+input2))
        self.sum+=(input1+input2)

    def subtractor(self):
        print("-----subtracting------")
        input1 = int(input("number 1:"))
        input2 = int(input("number 2:"))
        print("adding to sum:", (input1+input2))
        self.sum+=(input1-input2)

    def multiplier(self):
        print("-----multiplier------")
        input1 = int(input("number 1:"))
        input2 = int(input("number 2:"))
        print("adding to sum:", (input1+input2))
        self.sum+=(input1*input2)

    def divider(self):
        print("-----divide------")
        input1 = int(input("number 1:"))
        input2 = int(input("number 2:"))
        print("adding to sum:", (input1+input2))
        self.sum+=(input1/input2)

    def reset(self):
        print("-----reset------")
        print("last known value is:", self.sum)
        print("resetting now...")
        self.sum=0

calc = calculator()
calc.adder()
calc.subtractor()
calc.multiplier()
calc.divider()
calc.reset()