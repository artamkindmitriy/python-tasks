violator_songs = {
'World in My Eyes': 4.86,
'Sweetest Perfection': 4.43,
'Personal Jesus': 4.56,
'Halo': 4.9,
'Waiting for the Night': 6.07,
'Enjoy the Silence': 4.20,
'Policy of Truth': 4.76,
'Blue Dress': 4.29,
'Clean': 5.83
}

choose_songs = int(input("Сколько песен выбрать? "))

total_minute = 0

for songs in range(1, choose_songs + 1):
    song = input(f"Название{songs}-й песни: ")

    minutes = violator_songs.get(song, 0)

    if minutes == 0:
        print("Такой песни нет, она не будет учтена")
    else:
        total_minute += minutes

print(f"Общее время звучания песен:{total_minute} минуты")