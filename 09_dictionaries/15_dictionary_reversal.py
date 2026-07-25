cities = {'Москва': 'Россия', 'Берлин': 'Германия', 'Париж': 'Франция', 'Санкт-Петербург': 'Россия'}
results = {}

for city, country in cities.items():
    if country not in results:
        results[country] = []
    results[country].append(city)

print(results)