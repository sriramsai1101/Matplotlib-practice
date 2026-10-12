import matplotlib.pyplot as plt
products=["laptop","phone","tablet","watch"]
sales=[50,80,40,70]
plt.bar(products,sales,color="orange",width=0.5)
for i in range(len(products)):
    plt.text(i,sales[i],sales[i])
plt.xlabel("Products")
plt.ylabel("Sales")
plt.title("Product Sales")
plt.show()