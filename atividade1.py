import math

maleOscarAges = [44, 41, 62, 52, 41, 34,
                  34, 52, 41, 37, 38, 34,
                  32, 40, 43, 56, 41, 39,
                  49, 57, 41, 38, 42, 52,
                  51, 35, 30, 39, 41, 44,
                  49, 35, 47, 31, 47, 37,
                  57, 42, 45, 42, 44, 62,
                  43, 42, 48, 49, 56, 38,
                  60, 30, 40, 42, 36, 76,
                  39, 53, 45, 36, 62, 43,
                  51, 32, 42, 54, 52, 37,
                  38, 32, 45, 60, 46, 40,
                  36, 47, 29, 43]

def createEmptyList(size):
  list = []
  for i in range(size):
    list.append(0)
  return list

def getMiddleElementPos(list):
  return int((len(list) / 2)) - 1

def media(list):
  media = 0
  for age in list:
    media += age
  return round(media / len(list), 2)

def mediana(list):
  list.sort()
  if len(list) % 2 == 0:
    return list[getMiddleElementPos(list)]
  else:
    first = list[getMiddleElementPos(list)]
    second = list[getMiddleElementPos(list) + 1]
    return round((first + second) / 2, 2)

def moda(list):
  list.sort()
  modaList = createEmptyList(list[len(list) - 1] + 1)
  for element in list:
    modaList[element] += 1

  biggestOcurrency = 0
  for element in list:
    if modaList[element] > biggestOcurrency:
      biggestOcurrency = modaList[element]
  modas = set()
  for element in list:
    if modaList[element] == biggestOcurrency:
      modas.add(element)

  return modas

def pontoMedio(list):
  list.sort()
  lowest = list[0]
  biggest = list[len(list) - 1]
  return round((lowest + biggest) / 2, 2)

def amplitude(list):
  list.sort()
  lowest = list[0]
  biggest = list[len(list) - 1]
  return biggest - lowest

def variancia(list):
  avarage = media(list)
  value = 0
  for element in list:
    value += math.pow(element - avarage, 2)

  value /= len(list)
  return round(value, 2)

def desvioPadrao(list):
  variance = variancia(list)
  return round(math.sqrt(variance), 2)

def coeficienteVariacao(list):
  return round((desvioPadrao(list) / media(list)) * 100, 2)

print("Média: " + str(media(maleOscarAges)))
print("Mediana: " + str(mediana(maleOscarAges)))
print("Moda: " + str(moda(maleOscarAges)))
print("Ponto Médio: " + str(pontoMedio(maleOscarAges)))
print("Amplitude: " + str(amplitude(maleOscarAges)))
print("Desvio Padrão: " + str(desvioPadrao(maleOscarAges)))
print("Variância: " + str(variancia(maleOscarAges)))
print("Coeficiente de Variação: " +str(coeficienteVariacao(maleOscarAges)) + "%")
