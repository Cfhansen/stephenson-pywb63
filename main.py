###Solution to exercise 63 in ben stephenson's "the python workbook".

temps = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for t in temps:
  f = (t * 9 / 5) + 32
  print(f'{t}°C = {f}°F.')
