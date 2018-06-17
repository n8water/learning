# 4 x 4 Schablone mit X an den Stellen, die gesucht werden
# 4 x 4 Passwortfeld mit lowercase ascii zeichen als Passwortbestandteile

# die Schablone muss 4 x angewendet werden. jeweils 90 Grad im Uhrzeigersinn drehen!
# Koordinaten der X in der Schablone herausfinden und im Passwortfeld raussuchen gehen
# Lösung = string len 16

def recall_password(cipher_grille, ciphered_password):
    """User the cipher grille to decipher the password"""
    password = ""
    grille = list(cipher_grille)

    for i in range(4):
            # Find coordinates
        counter = 0
        mask = []
        for row in grille:
            for i in range(len(row)):
                if row[i] == "X":
                    new = (counter, i)
                    mask.append(new)
            counter += 1
    
        for item in mask:
            letter = ciphered_password[item[0]][item[1]]
            password = password + letter
    
     # Turn cipher_grille
    """Hier steckt ein Fehler""" 
    grille = (list(zip(*grille)))
    counter = 0
    return password


# Next step, turn the cipher_grille 3 times 90 degrees clockwise
# Run the above code 4 times and turn the cipher_grille at the end of each turn

print(recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi'))
    )

# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert recall_password(
#         ('X...',
#          '..X.',
#          'X..X',
#          '....'),
#         ('itdf',
#          'gdce',
#          'aton',
#          'qrdi')) == 'icantforgetiddqd', 'First example'

#     assert recall_password(
#         ('....',
#          'X..X',
#          '.X..',
#          '...X'),
#         ('xhwc',
#          'rsqx',
#          'xqzz',
#          'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
