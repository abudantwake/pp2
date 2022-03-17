import os
path = 'C:pp2.1\w6'

if os.path.exists(path):
    print ('Exists')
    print(os.path.basename(path))
    print(os.path.dirname(path))
    
else:
    print("Doesn't exists")
