import matplotlib.pyplot as plt
hours=[1,2,3,4,5]
marks=[30,45,50,70,90]
plt.scatter(hours,marks,color="blue",s=150,marker="o")
plt.xlabel("hours")
plt.ylabel("marks")
plt.title("hours vs marks")
plt.show()