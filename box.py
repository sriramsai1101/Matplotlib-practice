import matplotlib.pyplot as plt

maths =   [45, 67, 89, 54, 76, 88, 92, 61]
python =  [78, 85, 90, 72, 88, 95, 80, 76]
english = [55, 60, 70, 65, 72, 68, 58, 62]

data = [maths, python, english]

plt.figure(figsize=(8, 6))
plt.boxplot(data, tick_labels=["Maths", "Python", "English"])
plt.title("Subject wise Marks Distribution")
plt.ylabel("Marks")
plt.grid(True)
plt.show()