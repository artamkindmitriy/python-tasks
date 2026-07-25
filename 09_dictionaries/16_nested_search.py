servers = {
    'srv-1': {'ram': 16, 'status': 'up'},
    'srv-2': {'ram': 8, 'status': 'down'},
    'srv-3': {'ram': 32, 'status': 'up'},
}

srv_result = []

for server_name, data in servers.items():
    if data["ram"] > 10 and data["status"] == "up":
        srv_result.append(server_name)

print(srv_result)