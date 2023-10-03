class Cat:
    def __init__(self):
        self.arm_len = 30.0
        self.leg_len = 30.0
        self.eye_count = 2
        self.has_tail = True
        self.is_furry = True

    def print(self):
        print(f"A cat's arms are {self.arm_len} cm long.")
        print(f"A cat's legs are {self.leg_len} cm long.")
        print(f"A cat has {self.eye_count} eyes.")
        print(f"A cat has a tail: {self.has_tail}")
        print(f"A cat is furry: {self.is_furry}")


cat = Cat()

cat.print()
