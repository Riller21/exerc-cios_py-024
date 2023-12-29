# Número total de carros
TOTAL_CARROS = 5

# Listas para armazenar modelos e consumos
listaModelos = []
listaConsumo = []

# Preencher listas com dados fictícios
for i in range(TOTAL_CARROS):
    modelo = input(f"Informe o modelo do carro {i+1}: ")
    consumo = float(input(f"Informe o consumo do carro {i+1} em km/l: "))
    
    listaModelos.append(modelo)
    listaConsumo.append(consumo)

# Encontrar o modelo mais econômico
indice_mais_economico = listaConsumo.index(max(listaConsumo))
modelo_mais_economico = listaModelos[indice_mais_economico]

# Informações sobre o modelo mais econômico
print("\nModelo do carro mais econômico:", modelo_mais_economico)

# Calcular e mostrar consumo para percorrer 1000 km
distancia_percorrer = 1000
custo_gasolina = 2.25  # preço por litro de gasolina

for i in range(TOTAL_CARROS):
    litros_consumidos = distancia_percorrer / listaConsumo[i]
    custo = litros_consumidos * custo_gasolina

    print(f"\nCarro: {listaModelos[i]}")
    print(f"Litros consumidos para 1000 km: {litros_consumidos:.2f} litros")
    print(f"Custo para percorrer 1000 km: R$ {custo:.2f}")

