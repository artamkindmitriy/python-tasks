with open("day_plan.txt", "r") as f:
    for line_number, line in enumerate(f, start=1):
        print(f"{line_number}:{line.rstrip()}")