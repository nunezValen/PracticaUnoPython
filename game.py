import random
# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo",
"inteligencia"]

# Elegir una palabra al azar
secret_word = random.choice(words)
# Número máximo de intentos permitidos
max_attempts = 0
# Lista para almacenar las letras adivinadas
guessed_letters = []

print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")

#MENU
print("---MENU---")
print("1.Facil")
print("2.intermedio")
print("3.Dificil")
nivel=int(input("Elija una opcion de dificultad "))
print("----------")

#NIVEL FACIL
if (nivel==1):
     word_displayed = "" 
     for letter in secret_word:
         if letter in "aeiou":
             word_displayed +=letter
             guessed_letters +=letter #hago que cuente como advinada 
         else:
             word_displayed +="_"
     # Mostrarla palabra parcialmente adivinada
     print(f"Palabra: {word_displayed}")

#NIVEL INTERMEDIO
elif (nivel==2):
     word_displayed = secret_word[0]+"_"*(len(secret_word)-2)+secret_word[-1]
     guessed_letters +=secret_word[0]+secret_word[-1] #hago que cuente como advinada 
     print(f"Palabra: {word_displayed}")

#NIVEL DIFICIL
elif (nivel==3):
     word_displayed = "_"*len(secret_word)
     print(f"Palabra: {word_displayed}")

while max_attempts<10 :
     # Pedir al jugador que ingrese una letra
     letter = input("Ingresa una letra: ").lower()
     #Verifica si es una letra
     if not letter.isalpha():
         print("Por favor, ingresa solo letras.")
         max_attempts=max_attempts+1
         continue          
     # Verificar si la letra ya ha sido adivinada
     if letter in guessed_letters:
         print("Ya has intentado con esa letra. Intenta con otra.")
         max_attempts=max_attempts+1
         continue
     # Agregar la letra a la lista de letras adivinadas
     guessed_letters.append(letter)
     # Verificar si la letra está en la palabra secreta
     if letter in secret_word:
         print("¡Bien hecho! La letra está en la palabra.")
     else:
         print("Lo siento, la letra no está en la palabra.")
         max_attempts=max_attempts+1
     # Mostrar la palabra parcialmente adivinada
     letters = []
     for letter in secret_word:
         if letter in guessed_letters:
             letters.append(letter)
         else:
             letters.append("_")
     word_displayed = "".join(letters)
     print(f"Palabra: {word_displayed}")
     # Verificar si se ha adivinado la palabra completa
     if word_displayed == secret_word:
         print(f"¡Felicidades! Has adivinado la palabra secreta:  {secret_word} y con tan solo {max_attempts} fallos")
         break
else:
     print(f"¡Oh no! Has llegado a {max_attempts} fallos.")
     print(f"La palabra secreta era: {secret_word}")