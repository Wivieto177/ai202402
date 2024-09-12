def busqueda_lineal(lista, valor):

  for i in range(len(lista)):
    if lista[i] == valor:
      return i
  return -1
mi_lista = [3, 7, 4, 9, 12, 6]
valor_a_buscar = 9

indice = busqueda_lineal(mi_lista, valor_a_buscar)

if indice != -1:
  print("El valor", valor_a_buscar, "se encontró en el índice", indice)
else:
  print("El valor", valor_a_buscar, "no se encontró en la lista")