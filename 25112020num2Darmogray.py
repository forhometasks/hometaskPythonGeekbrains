inpsec = int(input("Введите время в секундах: "))
hours = inpsec // 3600
min = (inpsec - hours * 3600) // 60
sec = inpsec - (hours * 3600 + min * 60)
print(hours,":",min,":",sec)
