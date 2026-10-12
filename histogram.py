import matplotlib.pyplot as plt

marks = [10, 20, 20, 30, 30, 30, 40, 50, 50, 50]
plt.hist(marks, bins=5, color="skyblue", edgecolor="black")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.title("Marks Distribution")
plt.grid(axis="y", alpha=0.6)
plt.show()