import metapy

metapy.log_to_stderr()

doc = metapy.index.Document()
doc.content("I said that I can't believe that it only costs $19.95!")

tok = metapy.analyzers.ICUTokenizer(suppress_tags=True)
# tok = metapy.analyzers.LengthFilter(tok, min=2, max=30)
# tok = metapy.analyzers.ListFilter(tok, "lemur-stopwords.txt", metapy.analyzers.ListFilter.Type.Reject)
# tok = metapy.analyzers.Porter2Filter(tok)
# tok = metapy.analyzers.LowercaseFilter(tok)

ana = metapy.analyzers.NGramWordAnalyzer(1, tok)
print(doc.content())
unigrams = ana.analyze(doc)
print(unigrams)

tok.set_content(doc.content())
tokens = [token for token in tok]

print(tokens)

tok = metapy.analyzers.CharacterTokenizer()
ana = metapy.analyzers.NGramWordAnalyzer(4, tok)
fourchar_ngrams = ana.analyze(doc)
print(fourchar_ngrams)

seq = metapy.sequence.Sequence()
for word in ["The", "dog", "ran", "across", "the", "park", "."]:
    seq.add_symbol(word)
print(seq)
tagger = metapy.sequence.PerceptronTagger("perceptron-tagger/")
tagger.tag(seq)
print(seq)

doc = metapy.index.Document()
doc.content("I said that I can't believe that it only costs $19.95!")
tok = metapy.analyzers.ICUTokenizer()
tok.set_content(doc.content())
tokens = [token for token in tok]
print(tokens)


def extract_sequences(tok):
    sequences = []
    for token in tok:
        if token == '<s>':
            sequences.append(metapy.sequence.Sequence())
        elif token != '</s>':
            sequences[-1].add_symbol(token)
    return sequences


doc = metapy.index.Document()
doc.content("I said that I can't believe that it only costs $19.95!")
tok.set_content(doc.content())
for seq in extract_sequences(tok):
    tagger.tag(seq)
    print(seq)

ana = metapy.analyzers.load('config.toml')
doc = metapy.index.Document()
doc.content("I said that I can't believe that it only costs $19.95!")
print(ana.analyze(doc))
