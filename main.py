import random
class DataGen:
    def __init__(self):
        self.users = ["Alice", "Bob", "Charlie"]
    def generate(self):
        return random.choice(self.users)

if __name__ == "__main__":
    main()

