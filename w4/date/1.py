from datetime import datetime, timedelta

x=datetime.today() - timedelta(days=5)

print(x.strftime("%d/%m/%Y"))

# import time
# print(time.gmtime(0))

# import datetime

# x=datetime.datetime.today()

