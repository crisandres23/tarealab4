def calcular_promedios(verbales: str,numericas: str) -> int:
# Calcular la suma de los elementos de la lista
  verbales = sum(verbales)
  numericas = sum(numericas) 
  # Calcular el promedio dividiendo la suma por la longitud de la lista
  promedio = (verbales + numericas) / (len(verbales))
  return promedio
def estudiantes_bajos(verbales: str,numericas: str) -> int:
  # Convertir las cadenas de texto en listas de números enteros
  verbales = list(map(int, verbales.split()))
  numericas = list(map(int, numericas.split()))
  # Crear una lista vacía para almacenar la suma de las habilidades verbales y numéricas de cada estudiante
  sumas = []
  # Recorrer las listas de habilidades y sumarlas
  for i in range(len(verbales)):
    sumas.append(verbales[i] + numericas[i])
  # Calcular el promedio de la lista de sumas
  promedio = calcular_promedios(sumas)
  # Inicializar un contador de estudiantes por debajo del promedio
  contador = 0
  # Recorrer la lista de sumas y compararlas con el promedio
  for suma in sumas:
    # Si la suma es menor que el promedio, incrementar el contador
    if suma <= promedio:
      contador += 1
  # Devolver el contador como resultado
  return contador

# Ejemplo de uso de la función con los datos del problema