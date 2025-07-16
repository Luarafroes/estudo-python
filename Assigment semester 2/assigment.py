import json
import os

# === Bike Class ===
class Bike:
    def __init__(self, bike_id, model, type_, available=True):
        self.bike_id = bike_id
        self.model = model
        self.type = type_
        self.available = available

    def to_dict(self):
        return {
            "bike_id": self.bike_id,
            "model": self.model,
            "type": self.type,
            "available": self.available
        }

    @staticmethod
    def from_dict(data):
        return Bike(data["bike_id"], data["model"], data["type"], data["available"])


# === Load/Save Functions ===
def load_bikes():
    if os.path.exists("bikes.json"):
        with open("bikes.json", "r") as f:
            data = json.load(f)
            return [Bike.from_dict(b) for b in data]
    return []

def save_bikes(bikes):
    with open("bikes.json", "w") as f:
        json.dump([b.to_dict() for b in bikes], f, indent=2)


# === Menu Functions ===
def show_bikes(bikes):
    print("\nAvailable Bikes:")
    for bike in bikes:
        status = "Available" if bike.available else "Rented"
        print(f"ID: {bike.bike_id} | Model: {bike.model} | Type: {bike.type} | {status}")
    print()

def add_bike(bikes):
    try:
        bike_id = int(input("Enter bike ID: "))
        model = input("Enter model: ")
        type_ = input("Enter type: ")
        bikes.append(Bike(bike_id, model, type_))
        print("✓ Bike added.\n")
    except:
        print("⚠️ Invalid input.\n")

def rent_bike(bikes):
    try:
        bike_id = int(input("Enter bike ID to rent: "))
        for bike in bikes:
            if bike.bike_id == bike_id:
                if bike.available:
                    bike.available = False
                    print("✓ Bike rented.\n")
                else:
                    print("⚠️ That bike is already rented.\n")
                return
        print("⚠️ Bike not found.\n")
    except:
        print("⚠️ Invalid input.\n")

def return_bike(bikes):
    try:
        bike_id = int(input("Enter bike ID to return: "))
        for bike in bikes:
            if bike.bike_id == bike_id:
                if not bike.available:
                    bike.available = True
                    print("✓ Bike returned.\n")
                else:
                    print("⚠️ That bike is already available.\n")
                return
        print("⚠️ Bike not found.\n")
    except:
        print("⚠️ Invalid input.\n")


# === Main Program ===
def main():
    bikes = load_bikes()

    while True:
        print("=== Bike Rental Menu ===")
        print("1. Show all bikes")
        print("2. Add new bike")
        print("3. Rent a bike")
        print("4. Return a bike")
        print("5. Save and Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            show_bikes(bikes)
        elif choice == "2":
            add_bike(bikes)
        elif choice == "3":
            rent_bike(bikes)
        elif choice == "4":
            return_bike(bikes)
        elif choice == "5":
            save_bikes(bikes)
            print("✓ Data saved. Goodbye!")
            break
        else:
            print("⚠️ Invalid option. Try again.\n")


if __name__ == "__main__":
    main()