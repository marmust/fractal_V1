import math
text = int(input("code: "))
key = int(input("decryption key: "))
decryption = float(text*key/math.pi)
if decryption == 0.3183098861837907:
    print("succedded")
else:
    print("unidentified code or decryption key")