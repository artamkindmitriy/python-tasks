server_data = {

    "server": {

        "host": "127.0.0.1",

        "port": "10"

    },

    "configuration": {

        "access": "true",

        "login": "Ivan",

        "password": "qwerty"

    }

}

def dict_to_str(d):
    result = []
    for main_key, sub_dict in d.items():
        result.append(f"{main_key}:")
        for sub_key, value in sub_dict.items():
            result.append(f"{sub_key}:{value}")
    return "\n".join(result)

simple_str = dict_to_str(server_data)
print(simple_str)