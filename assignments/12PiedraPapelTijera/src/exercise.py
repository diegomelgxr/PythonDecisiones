def main():
    # Escribe tu código abajo de esta línea
    #Variables
TiroAna = (input('Tirada de Ana: '))
TiroJuan = (input('Tirada de Juan: '))
if len(TiroAna) > 1:
    print("Las tiradas deben ser un caracter")
elif len(TiroJuan) > 1:
    print("Las tiradas deben ser un caracter") 
elif TiroAna != 'a' and TiroAna != 'p' and TiroAna != 't':
    print("Tirada incorrecta")
elif TiroJuan != 'a' and TiroJuan != 'p' and TiroJuan != 't':
    print("Tirada incorrecta")

#Ganador/Empate
if TiroAna == 'a' and TiroJuan == 'a':
  print('Empate')
  
elif TiroAna == 'p' and TiroJuan == 'p':
  print('Empate')
  
elif TiroAna == 't' and TiroJuan == 't':
  print('Empate')
  
elif TiroAna == 'p' and TiroJuan == 'a':
  print('Gana Ana')
  
elif TiroAna == 'p' and TiroJuan == 't':
  print('Gana Juan')
  
elif TiroAna == 'a' and TiroJuan == 'p':
  print('Gana Juan')
  
elif TiroAna == 'a' and TiroJuan == 't':
  print('Gana Ana')
  
elif TiroAna == 't' and TiroJuan == 'a':
  print('Gana Juan')
  
elif TiroAna == 't' and TiroJuan == 'p':
  print('Gana Ana')
    

if __name__ == '__main__':
    main()
