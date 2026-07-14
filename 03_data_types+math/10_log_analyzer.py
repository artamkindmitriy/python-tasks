error_str = "[ERROR] 2026-06-10: Connection timeout"

start_type = error_str.find("[") + 1
end_type = error_str.find("]")

event_type = error_str[start_type:end_type]
print(f"Тип события: {event_type}")

find_index = error_str.find(":")
event_index = error_str[find_index + 2:]
print(f"Текст сообщения: {event_index}")
print(f"Текст в верхнем регистре: {error_str.upper()}")