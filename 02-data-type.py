import numpy as np

'''Tipos de datos
Los arrays de NumPy solo pueden contener un tipo de dato, ya que esto es lo que le confiere las ventajas de la optimización de memoria.'''

#Podemos conocer el tipo de datos del array consultando la propiedad .dtype.

arr = np.array([1, 2, 3, 4])
arr.dtype
'''---> dtype('int64')
Si queremos usar otro tipo de dato lo podemos definir en la declaración del array.'''

arr = np.array([1, 2, 3, 4], dtype = 'float64')
arr.dtype
'''	---> dtype('float64')
Ahora vemos que los valores están con punto decimal.'''

arr
'''	---> array([1., 2., 3., 4.])
Si ya se tiene el array definido se usa el método .astype() para convertir el tipo de dato.'''

arr = np.array([1, 2, 3, 4])
arr = arr.astype(np.float64)
arr
'''	---> array([1., 2., 3., 4.])
También se puede cambiar a tipo booleano recordando que los números diferentes de 0 se convierten en True.'''

arr = np.array([0, 1, 2, 3, 4])
arr = arr.astype(np.bool_)
arr
'''	---> array([False,  True,  True,  True,  True])
También podemos convertir los datos en tipo string.'''

arr = np.array([0, 1, 2, 3, 4])
arr = arr.astype(np.string_)
arr
'''	---> array([b'0', b'1', b'2', b'3', b'4'], dtype='|S21')
De igual forma se puede pasar de string a numero.'''

arr = np.array(['0', '1', '2', '3', '4'])
arr = arr.astype(np.int8)
arr
'''	---> array([0, 1, 2, 3, 4], dtype=int8)
Si un elemento no es de tipo número el método falla.'''


'''
Es importante que un único tipo de dato debe estar en el array
arr = np.array(['hola','0', '1', '2', '3', '4'])
arr = arr.astype(np.int8)
arr'''
"""---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-30-b9bb95861c7b> in <module>()
      1 # DSi un elemento no es de tipo número el método falla.
      2 arr = np.array(['hola','0', '1', '2', '3', '4'])
----> 3 arr = arr.astype(np.int8)
      4 arr

ValueError: invalid literal for int() with base 10: 'hola'"""