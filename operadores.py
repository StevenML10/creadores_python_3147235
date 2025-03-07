#Operadores en python
'''
Los operadores en python
siguen el siguiente orden jerarquico

1. (   )
2. **
3. / , * , %
4. + , -
5. NOT
6. AND
7.OR
8. =

NOTA#1
Si hay operaciones en el mismo nivel de jerarquia,
se resuelven de izquierda a derecha.

NOTA#2
Si hay prentesis dentro del parentesis se resuelve primero el parentesis interno.
'''

"y = a ** 2 - a * b - 1/ 3 + c"

"y = a * 2 ** 3 - a + c - c ** 3 + c"

"y= a ** 2 * 3 / (c - x)"

"y = ((2 * a + c) / 7) * ( a+ (4 * a) / c)"


'''
OPERADORES RELACIONALES:
Las operaciones aritmeticas
resultan en un valor numerico:
Las operaciones relacionales
resultan en un valor booleano:
True False (V, F SI NO)
Operadores Relacionales:
> , < , >= , <= , != , ==
JERARQUIA DE OPERADORES
(incluyendo Relacionales):

1. (  )
2.  **
3. * , / , %
4. + , -
5. < , > , >= , <= , != , ==
6. =
'''
a=2
b=3
c=7
x=5
h=1

y = c / (x + 2) < c * a - c + 1 - b * 2

print(y)
