time = int(input("Input time - "))
hours = time // 3600
min = (time // 60) - (hours * 60)
sec = time % 60
print(f"{hours:02}:{min:02}:{sec:02}")
