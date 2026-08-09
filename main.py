import random
class DataGen:
    def __init__(self):
        self.users = ["Alice", "Bob", "Charlie"]
    def generate(self):
        return random.choice(self.users)
def main():
    print("Hello from datagen!")
    generator = DataGen()
    print("Generated test user:", generator.generate())
if __name__ == "__main__":
    main()