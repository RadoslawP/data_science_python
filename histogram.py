from matplotlib import pyplot as plt
from collections import Counter


grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]


# Podzielenie stopni na decyle, ale tak, żeby wartość 100 znalazła się w jednym
# przedziale z 91 i 95.
histogram = Counter(min(grade // 10 * 10, 90) for grade in grades)


plt.bar([x + 5 for x in histogram.keys()],  # Przesunięcie słupków w prawo o 5.
        histogram.values(),                 # Nadawanie każdemu słupkowi właściwą wysokość.
        10)                                 # Nadawanie każdemu słupkowi szerokość 10.
plt.axis([-5, 105, 0, 5])                   # Zdefiniowanie zakresu osi x od -5 do 105
                                            # i zakres osi y od 0 do 5.
plt.xticks([10 * i for i in range(11)])     # Umieszczenie etykiety osi x w punktach 0, 10, ..., 100.
plt.xlabel("Decyl")
plt.ylabel("Liczba studentow")
plt.title("Rozkład ocen z pierwszego egzaminu")


plt.show()
