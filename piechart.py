import matplotlib.pyplot as plt
games = ["BGMI", "Cricket", "Football", "Other"]
players = [40, 25, 20, 15]
plt.pie(
    players,
    labels=games,
    colors=["blue","red","orange","brown"],
    autopct="%1.1f%%",
    explode=(0.1,0,0,0)

)
plt.title("Favourite Games")
plt.show()