def sVolume(R):
    volume = (4/3) * (3.14) * (R**3)
    return volume

R = int(input())
print(round(sVolume(R), 3))