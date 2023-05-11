def calcular_imc(Peso,Altura):
    Altura_aoquadrado = Altura**2
    Resultado = Peso / Altura_aoquadrado
    return Resultado
Peso = float(input("Insira seu peso (em kg) "))
Altura = float(input("Insira sua altura (em m): "))
Resultado = calcular_imc(Peso,Altura)

def definir_imc(Resultado):
    if Resultado < 18.5:
        return "Abaixo do peso"
    elif Resultado < 25:
        return (Resultado, "Peso normal")
        #print(Resultado,"Peso normal")
    #elif Resultado < 30:
        #print(Resultado,"Sobrepeso")
    #elif Resultado >= 30:
        #print(Resultado,"Obesidade")
        #return Resultado
#print(calcular_imc(Peso,Altura))
print(definir_imc(Resultado))