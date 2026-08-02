def generate_test_users(count: int):
    for i in range(1, count + 1):
        yield {
            "id": i,
            "email": f"user_{i}@test.com"
        }

gen = generate_test_users(5)

for user in gen:
    print(user)