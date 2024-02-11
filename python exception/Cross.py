number1=input("Entre un nombre\t")
number2=input("Entre un nombre\t")
resultat=0
try:
    number1=int(number1)  
    number2=int(number2)  
    resultat=number1//number2
    print(resultat)

except ZeroDivisionError:
    print("Vous ne pouvez pas diviser par zéro")
except ValueError:
    print("tu dois entrer un nombre")
else:
    print("bravo")
finally:
    print("bye")

    
