# Avaliador de Traduções em Python utilizando o modelo Gemini 1.0 Pro

## Descrição
Este projeto é um exemplo simples de como utilizar o Gemini para avaliar uma tradução em uma resposta padronizada em um formato JSON.

## Opcional
Caso queira experimentar um chatbot com o modelo antes de tocar em código, basta acessar: https://aistudio.google.com/app/prompts/new_chat/

## Instalação
Para executar o código, siga estas etapas:
1. Instale o Python 3 em seu computador: https://www.python.org/downloads/
2. Com o Python instalado, também instale a dependência necessária executando o abaixo no terminal:
```
pip install -q -U google-generativeai
```
3. Gere sua chave de acesso a API na página do AI Studio: https://aistudio.google.com/app/apikey/ e atualize a variável GOOGLE_API_KEY com a sua chave.

## Exemplo
Com a chave da API devidamente gerada e inserida em código, basta ajustar os campos a partir da linha 32 a tradução que deseja avaliar. Segue o exemplo abaixo:
```
# Frase original
frase_a_traduzir = "Ja, aber nur ein bisschen."
idioma_frase_a_traduzir = "alemao"

# Frase traduzida
frase_traducao = "sim, falo um pouco"
idioma_frase_traducao = "portugues"

# Opcional, mas detalhando os atores e contexto geral das frases acima
contexto_frases = "um alemao me perguntou 'Sprechen Sie Deutch?'"
```
E segue um exemplo de resposta para o conteudo acima:
```
{
  "traducao_valida": "pode_melhorar",
  "erro": "A tradução está incorreta. A resposta correta seria \"Sim, falo um pouco de alemão.\"",
  "avaliacao": "A tradução está incorreta e não respeita o contexto.",
  "sugestoes": [
    "Sim, falo um pouco de alemão."
  ],
  "similares": [],
  "detalhe_contexto": "A tradução não respeita o contexto porque a pergunta original era \"Você fala alemão?\" e a resposta correta seria \"Sim, falo um pouco de alemão.\""
}
```

## Melhorias/Sugestões

1. Mais testes e uma melhor calibragem dos parametros e utilização de termos mais precisos para garantir respostas com mais qualidade para que possam ser utilizadas em avaliações de aplicações no mundo real.