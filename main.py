from rm3100  import RM3100

DRDY = 27 #GPIO 27
SSN = 17 #GPIO 17

print("Start..........")

rm3100 = RM3100(17,27)
while True:
    data = rm3100.getHeading()
    if data != None:
        print(data)
