import customer



print(customer.getCustomer("c"))
customers = customer.getCustomers()

print(customer.getCustomers())

print(customers)


test = customer.Customer("t", "test", "Test Customer")

#customers["t"] = test

print(customers)
print("************************************")
for customerID in customers:
    customer1 = customers[customerID]
    print(customer1)

customer.updateCustomer(customers)
