from textblob import TextBlob


#REFERENCIA
#https://towardsdatascience.com/my-absolute-go-to-for-sentiment-analysis-textblob-3ac3a11d524

if __name__ == '__main__':
    texto = "I hate data mining"

    blob = TextBlob(texto)

    polaridade = blob.sentiment.polarity

    # Classificar o sentimento com base na polaridade
    if polaridade > 0:
        sentiment = 'Positivo'
    elif polaridade < 0:
        sentiment = 'Negativo'
    else:
        sentiment = 'Neutro'

    print(f'Texto: {texto}')
    print(f'Polaridade do Sentimento: {polaridade}')
    print(f'Classificação do Sentimento: {sentiment}')
