import json

def processoFaturamento(faturamento):
    with open(faturamento, 'r') as arquivo:
        faturamentos = json.load(arquivo)
    faturamentosValidados = [f for f in faturamentos if f >0]
    menorFaturamento = min(faturamentosValidados, default=0)
    maiorFaturamento = max(faturamentosValidados, default=0)
    
    if faturamentosValidados:
        mediaMes = sum(faturamentosValidados) / len(faturamentosValidados)
        diasUpMedia = sum(1 for f in faturamentosValidados if f > mediaMes)
    else:
        mediaMes = 0
        diasUpMedia = 0
    return {
        "Menor_Faturamento": menorFaturamento,
        "Maior_Faturamento": maiorFaturamento,
        "Dias_acima_da_media": diasUpMedia
    }

arquivo = 'faturamento.json'

resposta = processoFaturamento (arquivo)

print("O menor faturameto foi: ", resposta["Menor_Faturamento"])
print("O maior faturamento foi: ", resposta["Maior_Faturamento"])
print("O número de dias no qual o faturamento foi acima da média é: ", resposta["Dias_acima_da_media"])