import torch
from transformers import AutoTokenizer, AutoModelWithLMHead

tokenizer = AutoTokenizer.from_pretrained('t5-small')
model = AutoModelWithLMHead.from_pretrained('t5-small', return_dict = True)

inputs = tokenizer.encode("""summarize: Natural language processing (NLP) is an interdisciplinary subfield of linguistics, computer science, and artificial intelligence concerned with the interactions between computers and human language, in particular how to program computers to process and analyze large amounts of natural language data. The goal is a computer capable of "understanding" the contents of documents, including the contextual nuances of the language within them. The technology can then accurately extract information and insights contained in the documents as well as categorize and organize the documents themselves. Challenges in natural language processing frequently involve speech recognition, natural-language understanding, and natural-language generation.""", return_tensors = 'pt', max_length = 1024, truncation = True)

summarize_ids = model.generate(inputs, max_length = 200, min_length = 50, length_penalty =2, num_beams = 1)

summary = tokenizer.decode(summarize_ids[0])

print(summary)