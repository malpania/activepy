import os.path
import csv
import json
from flask import Flask
class Customer:
    def __init__(self, c="",f="",l=""):
        self.customerID = c
        self.firstName  = f
        self.lastName   = l
    def fullName(self):
        return self.firstName + " " + self.lastName


def getCustomers():
    if os.path.isfile("customers.json"):
        with open('customers.json', newline='') as customerFile:
            data = customerFile.read()
            customers = json.loads(data)
            return customers
    else:
        return {}


def getCustomer(customerID):
    customers = getCustomers()
    if customerID in customers:
        return customers[customerID]
    else:
        return {}

def updateCustomers(customers):
    with open('customers.json', 'w', newline='') as customerFile:
        customerJSON = json.dumps(customers)
        customerFile.write(customerJSON)


app = Flask(__name__)

@app.route("/")
def get_customers():
    return json.dumps(getCustomers())

@app.route("/get/<string:customerID>", methods=['GET'])
def get_customer(customerID):
    customer = getCustomer(customerID)
    if customer == {} :
        return {}, 404

    return json.dumps(customer)