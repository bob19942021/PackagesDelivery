# Author: Michael Boktour
# Student ID: 010319942
# Title: WGU C950 Routing Program
# over all Time-complexity of this class: O(n^2)
# over all Space-complexity of this class: O(n)

import csv
import datetime
import TruckInfo
from builtins import ValueError

from CSV_Write_Up import distance_File, address_File
from hashMap import HashMap
from packageclass import add_package_info


class Main:
    # To have and read distance csv files and put them in a list
    # Space-complexity: O(1)
    # Time-complexity: O(n)
    with open("CSV/distance.csv") as file:
        distance_File = csv.reader(file)
        distance_File = list(distance_File)


# Creating an object for each truck
# each object contains average speed, array with package's ID NO, start mileage, begging address and time the truck left
truck1 = TruckInfo.TruckInfo(18, [14, 37, 1, 16, 13, 15, 20, 19, 29, 30, 31, 34, 40], 0, "4001 South 700 East",
                             datetime.timedelta(hours=8, minutes=10))
truck2 = TruckInfo.TruckInfo(18, [23, 17, 6, 38, 3, 26, 12, 18, 21, 22, 24, 27, 35, 36, 39], 0,
                             "4001 South 700 East", datetime.timedelta(hours=8))
truck3 = TruckInfo.TruckInfo(18, [9, 2, 25, 11, 4, 5, 6, 33, 7, 8, 10, 28, 32], 0, "4001 South 700 East",
                             datetime.timedelta(hours=9, minutes=30))

# make a HashMap
package_table = HashMap()

# add packages into the hashTable
add_package_info("CSV/package.csv", package_table)


# Method finding nearest neighbor algorithm to find distance between two addresses
# time and space complexity are O(1)

def interval(x, y):
    space_between = distance_File[x][y]
    if space_between == '':
        space_between = distance_File[y][x]

    return float(space_between)


# Method to acquire address information
# time and space complexity are O(n)

def address_extract(address_info):
    for row in address_File:
        if address_info in row[2]:
            return int(row[0])


# this method uses the nearest neighbour algo to order packages and calculates distance drove by truck
# Space-complexity: O(n)
# Time-complexity: O(n^2)

def package_delivery(the_truck):
    undelivered = []
    for ID in the_truck.packages:
        package = package_table.lookup(ID)
        undelivered.append(package)
    the_truck.packages.clear()

    # the next while part will cycle through undelivered packages and add the closest package to the truck
    while len(undelivered) > 0:
        address_next = 20
        package_next = None
        for package in undelivered:
            if interval(address_extract(the_truck.address), address_extract(package.packageAddress)) <= address_next:
                address_next = interval(address_extract(the_truck.address), address_extract(package.packageAddress))
                package_next = package

        # appends the nearest package
        the_truck.packages.append(package_next.packageID)

        undelivered.remove(package_next)
        the_truck.mileage += address_next
        the_truck.address = package_next.packageAddress
        the_truck.time += datetime.timedelta(hours=address_next / 18)
        package_next.end_time = the_truck.time
        package_next.departure_time = the_truck.leave_time


# to load the trucks
package_delivery(truck1)
package_delivery(truck2)
truck3.time_of_departure = min(truck1.time, truck2.time)
package_delivery(truck3)

# will print mileage per truck and then the total mileage between all 3 trucks
print("the mileage for each truck rout")
print(truck1.mileage)
print(truck2.mileage)
print(truck3.mileage)
print("total mileage")
print(truck3.mileage + truck2.mileage + truck1.mileage)
narrative = input("to begin the program please type 'start'")
# if 'start' is written it will run the below code to cycle through the data and get the required object
# Time-complexity: O(n^2)
if narrative == "start":
    # will ask to input specific time
    # will put it all in a try catch block so program will exist properly if requirements where not met
    try:
        time_input = input("enter a time to check the status of the package. format should be, HH:MM:SS")
        (h, m, s) = time_input.split(":")
        time_convert = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

        second_narrative = input("to view a single package  type 'single'. for all packages type 'all'")

        # if single is typed the below block of code will first ask for ID NO. then look-up and get the data for it
        if second_narrative == "single":
            try:
                single_input = input("enter package ID NO.")
                package_data = package_table.lookup(int(single_input))
                package_data.update_status(time_convert)
                print(str(package_data))
            except ValueError:
                print("No package with that ID. Program closing")
                exit()

        # if all is typed the below block of code will get all addresses printed with the status of each at time entered
        elif second_narrative == "all":
            try:
                for ID_NO in range(1, 41):
                    package_data = package_table.lookup(ID_NO)
                    package_data.update_status(time_convert)
                    print(str(package_data))

            except ValueError:
                print("No package with that ID. Program closing")
                exit()

        else:
            exit()
    except ValueError:
        print("No package with that ID. Program shutting down")
        exit()
elif input != "start":
    print("invalid start entry. Program will be shutting down")
    exit()
