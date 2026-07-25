users_history = {
    'Алексей': ['google.com', 'yandex.ru', 'google.com'],
    'Марина': ['wikipedia.org', 'google.com', 'wikipedia.org', 'python.org'],
    'Иван': ['python.org', 'google.com']
}

for name, site in users_history.items():
    unique_sites = set(site)
    print(f"{name} -", *unique_sites)