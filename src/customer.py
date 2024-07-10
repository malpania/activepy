import csv
import os.path

class Customer:
    customerID = ""
    firstName = ""
    lastName = ""
    def __init__(self, customerID, firstName, lastName):
        self.customerID = customerID
        self.firstName = firstName
        self.lastName = lastName
    def fullName(self):
        return self.firstName + " " + self.lastName








customersToWrite = {
    "a": Customer("a","James", "Baker"),
    "b": Customer("b", "Jonathan", "D"),
    "c": Customer("c", "Aleem", "Janmohamed"),
    "d": Customer("d", "Ivo", "Galic"),
    "e": Customer("e", "Joel", "Griffiths"),
    "f": Customer("f", "Michael", "Spinks"),
    "g": Customer("g", "Victor", "Savkov"),
    "h" : Customer("h", "Marcel", "Dempers")
}




if os.path.isfile("customers.log"):
    f = open("customers.log", "r")
    for customer in f:
        print(customer)
    f.close()
else:
    f = open("customers.log", "a")
    fields = ['customerID', 'firstName', 'lastName']
    writer = csv.writer(f)
    writer.writerow(fields)
    for customerID in customersToWrite:
        c = customersToWrite[customerID]
        print("writing a file")
        writer.writerow([c.customerID , c.firstName , c.lastName ])
    f.close()




def getCustomers():
    if os.path.isfile("customers.log"):
        with open("customers.log", newline='') as customerFile:
            reader = csv.DictReader(customerFile)
            l = list(reader)
            customers = {c["customerID"]: c for c in l}
            return customers
    else:
        return {}


def getCustomer(customerID):
    customers = getCustomers()
    return customers[customerID]



customers = getCustomers()
for customerID in customers:
    print(customers[customerID])