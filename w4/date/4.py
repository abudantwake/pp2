from datetime import datetime

a = datetime(2021, 7, 5, 13, 53, 12)
b = datetime(2021, 7, 5, 13, 53, 32)

print(abs((a - b).total_seconds()))