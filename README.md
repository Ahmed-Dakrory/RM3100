Python RM3100
=============

This project contains a python module for interfacing with SPI RM3100 from user space via the spidev linux kernel driver.

All code is MIT licensed unless explicitly stated otherwise.

Usage
-----

```python
from rm3100  import RM3100

DRDY = 27 #GPIO 27
SSN = 17 #GPIO 17

print("Start..........")

rm3100 = RM3100(17,27)
while True:
    data = rm3100.getHeading()
    if data != None:
        print(data)
```