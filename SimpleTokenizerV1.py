import re
#tokenizer class
class SimpleTokenizerV1:
    def __init__(self, vocab):
        self.str_to_int = vocab
        self.int_to_str = {i:s for s,i in vocab.items()}

#text -> token_id
    def encode(self, text):
        preprocessed = re.split(r'([,.?_!"()\']|--|\s)', text)
        preprocessed = [
            item.strip() for item in preprocessed if item.strip()
        ]
        ids = [self.str_to_int[s] for s in preprocessed]
        return ids

#token_id -> text
    def decode(self, ids):
        text = " ".join([self.int_to_str[i] for i in ids])
        text = re.sub(r'\s+([,.?!"()\'])', r'\1', text)
        return text

# Questo tokenizer ha un problema: quando nel testo in input ci sono parole che non fanno parte del vocabolario, non sa come comportarsi. 
#   File "/Users/daniele/Documents/Projects/llm/SimpleTokenizerV1.py", line 14, in encode
#     ids = [self.str_to_int[s] for s in preprocessed]
#            ~~~~~~~~~~~~~~~^^^
# KeyError: 'Hello'

# V2 risolve questo problema. 