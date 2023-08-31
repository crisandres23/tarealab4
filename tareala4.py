def calcular_promedios(verbales: str,numericas: str) -> int: 
  suma = []  # Lista para almacenar las sumas
  promedio = 0
  for i in range(len(verbales)):
        suma.append(verbales[i] + numericas[i])
        promedio += verbales[i]
    
  promedio = promedio / len(verbales)
  return suma, promedio  # Devuelve una tupla con la lista de sumas y el promedio


def calcular_suma_promedio(verbales, numericas) -> int:
    verbales = list(map(int, verbales.split()))  
    numericas = list(map(int, numericas.split()))  
    
    suma = []  # Lista para almacenar las sumas
    promedio = 0
    for i in range(len(verbales)):
        suma.append(verbales[i] + numericas[i])
        promedio += verbales[i]
    
    promedio = promedio / len(verbales)
    contador = 0
    for s in suma:
        if s <= promedio:
            contador += 1
    
    return suma, promedio, contador  # Devuelve una tupla con la lista de sumas, e

pass