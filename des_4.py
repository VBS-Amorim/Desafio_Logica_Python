def percentualFaturamentos (faturamentos):
    faturamento_tudo = sum(faturamentos.values())
    percentuais = {}
    for estado, valor in faturamentos.items():
        percentual = (valor/faturamento_tudo)*100
        percentuais[estado] = percentual
    return percentuais

faturamentos = { "SP": 67836.43, "RJ": 36678.66, "MG":29229.88, "ES": 271165.48, "Outros": 19849.53}

percentuais = percentualFaturamentos(faturamentos)

for estado, percentual in percentuais.items():
    print(f"Percentual {estado}: {percentual:.2f}%")