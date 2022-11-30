class TV:
    def __init__(self):
        self.__channels = []
        for i in range(0, 30):
            self.__channels.append(f"-|{i+1}|-")
        self.__channel = 0

    def getChannels(self):
        print(self.__channels)

    def getChannel(self):
        print(f"Current channel is : {self.__channels[self.__channel]}")

    def setChannel(self, name):
        if self.__channel >= 0 and self.__channel <= 29:
            self.__channels[self.__channel] = f"-|{name}|-"
        else:
            print("something went wront with the setChannel function")

    def nextChannel(self):
        if self.__channel >= 0 and self.__channel < 29:
            self.__channel += 1
        elif self.__channel == 29:
            self.__channel = 0
        else:
            print("something went wront with the nextChannel function")


tv = TV()
tv.getChannels()
tv.setChannel("MTV")
tv.getChannel()
tv.nextChannel()
tv.nextChannel()
tv.nextChannel()
tv.setChannel("VIVA")
tv.getChannel()
tv.getChannels()
for i in range(0, 27):
    tv.nextChannel()
tv.getChannel()
