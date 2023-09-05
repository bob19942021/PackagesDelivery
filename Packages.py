# class to handle packages
import csv


class PackageClass:
    # constructor for the package class
    # Space and Time-complexity are O(1)
    def __init__(self, packageID, packageAddress, packageCity, packageState, packageZipcode,
                 delivery_date, weight, delivery_status):
        self.packageID = packageID
        self.packageAddress = packageAddress
        self.packageCity = packageCity
        self.packageState = packageState
        self.packageZipcode = packageZipcode
        self.delivery_date = delivery_date
        self.weight = weight
        self.delivery_status = delivery_status
        self.begin_time = None
        self.end_time = None

    # method to return info about the package
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.packageID, self.packageAddress, self.packageCity,
                                                       self.packageState, self.packageZipcode, self.delivery_date,
                                                       self.weight, self.end_time, self.delivery_status)

    # method to update time or change time of package delivery
    # Time-complexity: O(1)
    # Space-complexity: O(1)
    def update_status(self, change):
        if self.end_time < change:
            self.delivery_status = "Delivered"
        elif self.end_time > change:
            self.delivery_status = "En route"
        else:
            self.delivery_status = "At Hub"


# create an object of the package
# then load that object into the HashMap table
# Time-complexity: O(n)
# Space-complexity: O(1)
def add_package_info(fileinfo, package_table):
    with open(fileinfo) as packages_information:
        package_data = csv.reader(packages_information)
        for individual_info in package_data:
            the_package_ID = int(individual_info[0])
            the_Package_Address = individual_info[1]
            the_package_City = individual_info[2]
            the_package_State = individual_info[3]
            the_package_Zipcode = individual_info[4]
            the_package_Deadline_time = individual_info[5]
            the_package_Weight = individual_info[6]
            the_package_Status = "At Hub"

            # the package object
            package_Object = PackageClass(the_package_ID, the_Package_Address, the_package_City,
                                          the_package_State, the_package_Zipcode, the_package_Deadline_time,
                                          the_package_Weight, the_package_Status)

            # to put the data into a Hash-Table
            package_table.insert(the_package_ID, package_Object)
