class Bus:
    def __init__(self, route_number, capacity):
        self.route_number = route_number
        self.capacity = capacity
        self.city_name = "Default City"  # Default city name
        self._passengers = 0

    def add_passengers(self, count):
        new_count = self._passengers + count
        if new_count <= self.capacity:
            self._passengers = new_count
        else:
            print("Error: Bus is at capacity")

    def get_current_fare(self):
        # You would need a fare calculation logic here (for simplicity, let's use a base fare)
        base_fare = 2.00
        return base_fare + 0.25 * self._passengers

if __name__ == "__main__":
    bus1 = Bus(12, 50)
    bus2 = Bus(3, 40)

    print(f"Bus 1 city: {bus1.city_name}")  
    print(f"Bus 2 city: {bus2.city_name}") 

    bus1.city_name = "New City"  
    print("After changing bus1's city...")
    print(f"Bus 1 city: {bus1.city_name}") 
    print(f"Bus 2 city: {bus2.city_name}")  

    print(f"Bus 1 fare: ${bus1.get_current_fare()}")
    bus1.add_passengers(30)
    bus2.add_passengers(25) 