site = {

    'html': {

        'head': {

            'title': 'Мой сайт'

        },

        'body': {

            'h2': 'Здесь будет мой заголовок',

            'div': 'Тут, наверное, какой-то блок',

            'p': 'А вот здесь новый абзац'

        }

    }

}

def find_key_in_dict(d, target):
    if target in d:
        return d[target]

    for key, value in d.items():
        if isinstance(value, dict):
            result = find_key_in_dict(value, target)
            if result:
                return result
    return "Такого ключа в структуре сайта нет"

find_key = input("Искомый ключ: ")
print(find_key_in_dict(site, find_key))