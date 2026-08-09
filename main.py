from generator import DataGen

def main():
    print("Hello from datagen!")
    data = ["User_101", "User_102", "User_103", "User_104", "User_105"]
    
    generator = DataGen(data)
    
    # Generate 3 items
    results = generator.generate(count=3)
    
    # Iterate and print each generated user
    for user in results:
        print("Generated user:", user)

if __name__ == "__main__":
    main()
