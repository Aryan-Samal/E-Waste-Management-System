#VU21CSEN0400035 Bhoomik Aryan Samal

import datetime

class Device:
    def __init__(self, name, purchase_date, expected_lifespan):
        self.name = name
        self.purchase_date = purchase_date
        self.expected_lifespan = expected_lifespan
    
    def get_end_of_life(self):
        return self.purchase_date + datetime.timedelta(days=self.expected_lifespan * 365)

    def needs_replacement(self):
        return datetime.date.today() >= self.get_end_of_life()

class EWasteManager:
    def __init__(self):
        self.devices = []

    def add_device(self):
        name = input("Enter the device name: ")
        purchase_date_str = input("Enter the purchase date (YYYY-MM-DD): ")
        lifespan_years = int(input("Enter the expected lifespan in years: "))

        purchase_date = datetime.datetime.strptime(purchase_date_str, "%Y-%m-%d").date()
        device = Device(name, purchase_date, lifespan_years)
        self.devices.append(device)
        print(f"Device '{name}' successfully added.\n")

    def check_for_replacement(self):
        devices_for_replacement = [device.name for device in self.devices if device.needs_replacement()]
        
        if devices_for_replacement:
            print("These devices need to be replaced and recycled:")
            for device in devices_for_replacement:
                print(f"- {device}")
        else:
            print("No devices need replacement at this time.\n")
    
    def show_all_devices(self):
        if not self.devices:
            print("No devices in the system.\n")
            return
        
        print("Current devices in the system:")
        for device in self.devices:
            end_of_life = device.get_end_of_life()
            print(f"Device: {device.name}, Purchased on: {device.purchase_date}, End of Life: {end_of_life}")
        print()

def main():
    ewaste_manager = EWasteManager()
    
    while True:
        print("Aryan's E-Waste Management Software V1")
        print("1. Add a new device")
        print("2. Check devices for replacement")
        print("3. View all devices")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            ewaste_manager.add_device()
        elif choice == '2':
            ewaste_manager.check_for_replacement()
        elif choice == '3':
            ewaste_manager.show_all_devices()
        elif choice == '4':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please select again.\n")

if __name__ == "__main__":
    main()