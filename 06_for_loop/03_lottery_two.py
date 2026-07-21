count = 0
for i in 345, 19, 87, 1020, 421:
    if len(str(i)) == 3 and i % 5 == 0:
        print(f"Билет {i} выигрышный")
        count += 1
    else:
        print(f"Билет {i} проигрышный")

print(f"Всего победителей: {count}")