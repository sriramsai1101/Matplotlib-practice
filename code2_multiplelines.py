import matplotlib.pyplot as plt
days=[1,2,3,4,5]
actual_sales=[100,120,110,150,140]
target_sales=[90,100,120,130,150]
plt.plot(days,actual_sales,marker="o",linestyle="--",color="blue",label="Actual sales")
plt.plot(days,target_sales,marker="o",linestyle="--",color="orange",label="Target sales")
plt.title("Daily Sails Comparision")
plt.xlabel("Days")
plt.ylabel("Sales")
plt.legend()
plt.grid()
plt.show()