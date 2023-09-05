# Create class for info about the individual trucks
# Time-complexity: O(1)
# Space-complexity: O(1)
class TruckInfo:
    def __init__(self, speed, packages, mileage, main_address, leave_time):
        self.speed = speed
        self.packages = packages
        self.mileage = mileage
        self.address = main_address
        self.leave_time = leave_time
        self.time = leave_time
