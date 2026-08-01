class Guitar:
    def play(self):
        print("Дзынь!")

class Piano:
    def play(self):
        print("Бам!")

class Flute:
    def play(self):
        print("Ту-ту!")

guitar = Guitar()
piano = Piano()
flute = Flute()

music_tools = [guitar, piano, flute]

for tool in music_tools:
    tool.play()