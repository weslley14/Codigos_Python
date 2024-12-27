import re
from collections import Counter

def calcular_tracos(texto):
    # Remover pontuação e converter para minúsculas
    texto = re.sub(r'[.!?;:]', '', texto).lower()
    palavras = texto.split()
    
    # Número total de palavras
    total_palavras = len(palavras)
    
    if total_palavras == 0:
        return [0] * 6  # Retorna zero se não houver palavras
    
    # Tamanho médio de palavra
    tamanho_medio_palavra = sum(len(p) for p in palavras) / total_palavras
    
    # Relação Type-Token
    palavras_unicas = set(palavras)
    relacao_type_token = len(palavras_unicas) / total_palavras
    
    # Razão Hapax Legomana
    contagem_palavras = Counter(palavras)
    hapax_legomena = sum(1 for count in contagem_palavras.values() if count == 1)
    razao_hapax_legomana = hapax_legomena / total_palavras
    
    # Dividir o texto em sentenças
    sentencas = re.split(r'[.!?]', texto)
    num_sentencas = len([s for s in sentencas if s.strip()])  # Conta apenas sentenças não vazias
    
    # Tamanho médio de sentença
    tamanho_medio_sentenca = sum(len(s) for s in sentencas if s.strip()) / num_sentencas if num_sentencas > 0 else 0
    
    # Contar frases
    frases = re.split(r'[,.]', texto)
    num_frases = len([f for f in frases if f.strip()])  # Conta apenas frases não vazias
    
    # Complexidade de sentença
    complexidade_sentenca = num_frases / num_sentencas if num_sentencas > 0 else 0
    
    # Tamanho médio de frase
    tamanho_medio_frase = sum(len(f) for f in frases if f.strip()) / num_frases if num_frases > 0 else 0
    
    return [
        tamanho_medio_palavra,
        relacao_type_token,
        razao_hapax_legomana,
        tamanho_medio_sentenca,
        complexidade_sentenca,
        tamanho_medio_frase
    ]

def calcular_similaridade(tracos_a, tracos_b):
    return sum(abs(a - b) for a, b in zip(tracos_a, tracos_b)) / 6

def main():
    # Leitura da assinatura do portador de COH-PIAH
    assinatura = list(map(float, input("Digite os traços linguísticos da assinatura (separados por espaço): ").strip().split()))
    
    textos = []
    print("Digite os textos (digite 'FIM' para terminar):")
    
    while True:
        texto = input()
        if texto.strip().upper() == "FIM":
            break
        textos.append(texto)
    
    # Processar textos e calcular similaridade
    similaridades = []
    
    for texto in textos:
        tracos_texto = calcular_tracos(texto)
        similaridade = calcular_similaridade(tracos_texto, assinatura)
        similaridades.append(similaridade)
    
    # Encontrar o texto mais semelhante
    indice_texto_similar = similaridades.index(min(similaridades))
    
    print(f"O texto mais semelhante à assinatura de COH-PIAH é o texto #{indice_texto_similar + 1}.")

# Chamada da função principal
if __name__ == "__main__":
    main()
