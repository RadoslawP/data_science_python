from matplotlib import pyplot as plt


friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']


plt.scatter(friends, minutes)


# Nadawanie etykiety wszystkim punktom.
for label, friend_count, minute_count in zip(labels, friends, minutes):
    plt.annotate(label,
        xy=(friend_count, minute_count),    # Umieszczenie etykiety we wlasciwym miejscu,
        xytext=(5, -5),                     # ale lekko przesunietej.
        textcoords='offset points')


plt.title("Czas spędzony na stronie a liczba znajomych.")
plt.xlabel("Liczba znajomych")
plt.ylabel("Dzienny czas spedzony na stronie (minuty)")


plt.show()
