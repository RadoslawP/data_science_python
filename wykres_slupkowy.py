from matplotlib import pyplot as plt


movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

# Rysowanie słupków o współrzędnych x [0, 1, 2, 3, 4] i wysokosci [num_oscars].
plt.bar(range(len(movies)), num_oscars)
# Dodawanie etykiety osi y.
plt.ylabel("Liczba nagrod")
# Dodawanie tytułu.
plt.title("Moje ulubione filmy")


# Nanoszenie na oś x etykiet w postaci tytułów filmów i wyśrodkowanie ich.
plt.xticks(range(len(movies)), movies)

plt.show()
