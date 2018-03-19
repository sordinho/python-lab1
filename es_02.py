#Esercizio 2 data una stringa ritornare i primi 2 e ultimi 2 caratteri

stringa = 'hello'
length = len(stringa)

if length < 4:
    print ("")
else:
    newString = stringa[0] + stringa[1] + stringa[len(stringa)-2] +stringa[len(stringa)-1]
    print(newString)