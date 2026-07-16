download_size = 123
download_speed = 27

second = 0
download = 0

while download < download_size:
    if download_speed <= 0:
        print("Скорость соединения не может быть меньше или равна нулю.")
        break

    second += 1
    download += download_speed

    percent = min((download / download_size) * 100, 100)

print(f"Прошло {second} сек. Скачано {download} из {download_size} — {percent:.1f}%")