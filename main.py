from generator import DataGen  # Connection line linking both files

def main():
    print("Hello from datagen!")
    data = ["User_101", "User_102", "User_103"]
    
    generator = DataGen(data)
    print("Generated user:", generator.generate())

if __name__ == "__main__":
    main()
