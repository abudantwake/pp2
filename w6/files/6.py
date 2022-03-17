for letter in range(65, 65 + 26):
    filename = chr(letter) + '.txt'
    
    with open (chr(letter) + '.txt', 'w') as f:
        f.writelines(chr(letter))
        
f.close()