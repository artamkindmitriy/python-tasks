violator_songs = [
['World in My Eyes', 4.86],
['Sweetest Perfection', 4.43],
['Personal Jesus', 4.56],
['Halo', 4.9],
['Waiting for the Night', 6.07],
['Enjoy the Silence', 4.20],
['Policy of Truth', 4.76],
['Blue Dress', 4.29],
['Clean', 5.83]
]

total_minute = 0

N = int(input("Сколько песен выбрать? "))

for songs in range(1, N + 1):
    song = input(f"Название {songs} песни: ")
    found = False

    for name_song in violator_songs:
        if name_song[0] == song:
            total_minute += name_song[1]
            found = True
    if not found:
        print("Такой песни нету в списке")
print(f"Общее время звучания - {total_minute:.2f} минут")