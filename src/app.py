import customer



print(customer.getCustomer("Third"))
customers = customer.getCustomers()
customers["First"] = "New First Customer"
print(customer.getCustomers())
print(customers)
print(customers["Second"].fullName())

