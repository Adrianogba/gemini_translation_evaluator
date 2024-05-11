#pip install -q -U google-generativeai
try:
    import google.generativeai as genai
    from google.api_core.exceptions import InvalidArgument
    print("Dependências instaladas. Iniciando código...")
except ImportError:
    print("Dependência não instalada. Favor rodar o codigo a seguir em um terminal para poder executar este código: pip install -q -U google-generativeai")

# Configurando a chave da API
GOOGLE_API_KEY = "SUA_CHAVE"
genai.configure(api_key=GOOGLE_API_KEY)

# Configurações de geração
generation_config = {
    "candidate_count": 1,
    "temperature": 0.6,
    "top_k": 1000,
    "top_p": 0.6,
    "max_output_tokens": 1000,
}

safety_settings = {
    "HARASSMENT": "BLOCK_NONE",
    "HATE": "BLOCK_NONE",
    "SEXUAL": "BLOCK_NONE",
    "DANGEROUS": "BLOCK_NONE"
}

# Criando o modelo
model = genai.GenerativeModel(model_name="gemini-1.0-pro", generation_config=generation_config, safety_settings=safety_settings)

# Frase original
frase_a_traduzir = "Ja, aber nur ein bisschen."
idioma_frase_a_traduzir = "alemao"

# Frase traduzida
frase_traducao = "sim, falo um pouco"
idioma_frase_traducao = "portugues"

# Opcional, mas detalhando os atores e contexto geral das frases acima
contexto_frases = "um alemao me perguntou 'Sprechen Sie Deutch?'"

# Gerando conteúdo

prompt = ("Você agora é um avaliador de traduções profissional. "
"Esta é a 'frase' em " + idioma_frase_a_traduzir + "é '" + frase_a_traduzir + "',"
"esta é a 'tradução' em " + idioma_frase_traducao + "é '" + frase_traducao + "' ,"
"e o 'contexto' dessas frases seria '" + contexto_frases + "'."
"Avalie a tradução, respondendo apenas um json com os seguintes parametros: "
"'traducao_valida' para caso a tradução seja boa e esteja absolutamente correta, respeitando o contexto se fornecido, respondendo com sim ou nao ou pode_melhorar, "
"'erro' null para caso não haja nenhum problema mas caso haja uma frase explicando em detalhes os erros no conteudo fornecido, "
"'avaliacao' com uma breve avaliação da tradução,"
"'sugestoes' null para caso não haja nenhuma e uma lista de frases ou termos para sugestões melhores,"
"'similares' null para caso não haja nenhuma e uma lista de frases ou termos para frases ou termos similares."
"'detalhe_contexto' explicando como a tradução respeita o contexto fornecido.")

try:
    response = model.generate_content(prompt)
    print(response.text)
except InvalidArgument as e:
    print('GOOGLE_API_KEY inválida.')
    print(e)

