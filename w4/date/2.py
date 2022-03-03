from datetime import datetime, timedelta

yesterday=datetime.today() - timedelta(days=1)

today=datetime.today()

tomorrow=datetime.today() + timedelta(days=1)

print(yesterday.strftime("%d/%m/%Y"))

print(today.strftime("%d/%m/%Y"))

print(tomorrow.strftime("%d/%m/%Y"))
