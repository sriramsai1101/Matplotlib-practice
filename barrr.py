import matplotlib.pyplot as plt
products=["pen","books","bags"]
sales=[20,35,50]
plt.barh(products,sales,color="green")
plt.title("products sales")
for i in range(len(products)):
    plt.text(i,sales[i]+2,sales[i]+2)
plt.show()