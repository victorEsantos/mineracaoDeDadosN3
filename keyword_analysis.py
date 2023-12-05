import spacy

# REFERENCIA
# https://towardsdatascience.com/keyword-extraction-process-in-python-with-natural-language-processing-nlp-d769a9069d5c

if __name__ == '__main__':
    nlp = spacy.load("pt_core_news_sm")
    text = """"spaCy é uma biblioteca de software de código aberto para processamento avançado de linguagem natural,
    escrita nas linguagens de programação Python e Cython. A biblioteca é publicada sob a licença MIT,
    e seus principais desenvolvedores são Matthew Honnibal e Ines Montani, fundadores da empresa de software Explosion."""
    doc = nlp(text)
    print(doc.ents)
