response_times = [45, 120, 210, 85, 300, 199, 450, 95]

response = list(filter(lambda time: time >= 200, response_times))
print(response)