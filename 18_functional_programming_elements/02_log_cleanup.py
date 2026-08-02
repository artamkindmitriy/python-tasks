responses = ["status: OK", "ERROR 504", "not found", "BAD gateway"]

answer = list(map(lambda resp: resp.lower().capitalize(), responses))
print(answer)