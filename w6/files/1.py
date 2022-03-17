import os 

path = 'C:pp2.1\w6'

print('Only directories:')
print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path,name)) ])
print('\nOnly files')
print([ name for name in os.listdir(path) if os.path.isfile(os.path.join(path,name)) ])
print('\nAll directories and files')
print([ name for name in os.listdir(path)])