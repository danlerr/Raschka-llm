from importlib.metadata import version
import tiktoken
print("tiktoken version:", version("tiktoken"))
tokenizer = tiktoken.get_encoding("gpt2")
text = (
    "Hello, do you like tea? <|endoftext|> In the sunlit terraces "
    "of someunknownPlace."
)
integers = tokenizer.encode(text, allowed_special={"<|endoftext|>"})
print(integers)
# [15496, 11, 466, 345, 588, 8887, 30, 220, 50256, 554, 262, 4252, 18250, 8812, 2114, 286, 617, 34680, 27271, 13]

strings = tokenizer.decode(integers)
print(strings)
# Hello, do you like tea? <|endoftext|> In the sunlit terraces of someunknownPlace.

# the BPE (Byte Pair Encoding) tokenizer encodes and decodes also unknown words correctly (in this case someunknownPlace).
# this type of tokenizer, based on BPE, can handle any unk words. But why?? 
# because the algorithm underlying BPE breaks down words that aren't in its predefined vocabolary into smaller subword units or even 
# individual chars. 
# So, if the tokenizer encounters an unfamiliar word (not in vocabolary) during tokenization, it can represents it as a sequence
# of subword tokens. [page 34]
