import matplotlib.pyplot as plt
months=[1,2,3,4,5]
sales=[100,150,120,180,160]
profit=[20,40,25,50,35]
fig,ax=plt.subplots(1,2,figsize=(10,4))
ax[0].plot(months,sales,label="sales")
ax[0].set_xlabel("Sales")
ax[0].grid()
ax[0].legend()
ax[0].set_title("sales")
ax[1].plot(months,profit,label="profit")
ax[1].set_ylabel("Profit")
ax[1].grid()
ax[1].legend()
ax[1].set_title("profit")
plt.show()