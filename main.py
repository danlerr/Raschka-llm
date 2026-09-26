from SimpleTokenizerV1 import SimpleTokenizerV1
from SimpleTokenizerV2 import SimpleTokenizerV2
import re

#load the the-verdict.txt file
with open("the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

# L'obiettivo è generare degli IDs dati i token (parole) dato del testo 

# 1.dato il testo prendiamo parola (token) per parola (compresi caratteri speciali o spazi) 
# re.split fa proprio questo: data una stringa in input ritorna un array di sottostringhe 
preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text) 
preprocessed = [item.strip() for item in preprocessed if item.strip()]

# 2.dato l'array con i token, vogliamo associare ad ogni token un ID unico 
# 2.1.creiamo il vocabolario 
all_tokens = sorted(set(preprocessed))
all_tokens.extend(["<|endoftext|>", "<|unk|>"])                               # special context tokens
vocab = {token:integer for integer,token in enumerate(all_tokens)}
for i, item in enumerate(vocab.items()):
    print(item)
    if i >= 50:
        break

tokenizer = SimpleTokenizerV2(vocab)
# text = """"It's the last he painted, you know,"
# Mrs. Gisburn said with pardonable pride."""
text = "Hello, do you like tea?"
ids = tokenizer.encode(text)
print(ids)  

# [1, 56, 2, 850, 988, 602, 533, 746, 5, 1126, 596, 5, 1, 67, 7, 38, 851, 1108, 754, 793, 7]


print(tokenizer.encode(text))
print(tokenizer.decode(ids))

# [1131, 5, 355, 1126, 628, 975, 10]
# [1131, 5, 355, 1126, 628, 975, 10]
# <|unk|>, do you like tea?