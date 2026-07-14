email = "alex.python_master@innopolis.university"

result = email[:3] + "***" + email[email.find("@"):]
print(result)