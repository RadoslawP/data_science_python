from matplotlib import pyplot as plt


variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
total_error = [x + y for x, y in zip(variance, bias_squared)]
xs = [i for i, _ in enumerate(variance)]


# Wywoływanie funkcji plt.plot wielokrotnie.
# w celu umieszczenia wielu serii danych na tym samym wykresie.
plt.plot(xs, variance, 'g-', label='variance')  #zielona linia ciagla
plt.plot(xs, bias_squared, 'r-', label='bias^2')    #czerwona linia z kropek i kresek
plt.plot(xs, total_error, 'b:', label='total_error')    #niebieska linia punktowa


# Przypisanie etykiet do wszystkich serii danych,
# więc legenda zostanie wygenerowana automatycznie.
# Parametr loc=9 umieszcza ją na środku u góry wykresu.
plt.legend(loc=9)
plt.xlabel("Stopien skomplikowania modelu")
plt.title("Kompromis pomiędzy wartoscia progowa i zlozonoscia modelu")


plt.show()
