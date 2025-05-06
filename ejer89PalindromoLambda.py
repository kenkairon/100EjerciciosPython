"""
ejercicio 89
comprobar si una palabra
es un palíndromo usanda lambda
"""
palindromo = lambda palabra: palabra == palabra[::-1]
print(palindromo("radar")) 
print(palindromo("python")) 