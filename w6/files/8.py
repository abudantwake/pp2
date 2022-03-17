import os

path = 'C:pp2.1\w6'

if os.path.exists(path):
    os.remove(path)
else:
    print('Can not be deleted')