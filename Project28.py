class Vehicle:
    def __init__(self, name, seating_capacity):
        self.name = name
        self.seating_capacity = seating_capacity

    def fare(self):
        # Default fare calculation: capacity * 100
        return self.seating_capacity * 100

class Bus(Vehicle):
    def fare(self):
        # Calculate the base fare from the parent class
        base_fare = super().fare()
        # Add 10% maintenance charge
        total_fare = base_fare + (base_fare * 0.10)
        return total_fare

# Example Usage
school_bus = Bus("School Bus", 50)
print(f"Total {school_bus.name} fare is: INR {school_bus.fare()}")

    
  

 


