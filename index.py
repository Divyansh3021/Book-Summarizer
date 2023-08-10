import torch
from transformers import AutoTokenizer, AutoModelWithLMHead, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained('t5-small')
model = AutoModelWithLMHead.from_pretrained('t5-small', return_dict = True)
# model = AutoModelForSeq2SeqLM.from_pretrained("sgugger/my-awesome-model")
# model = AutoModelForCausalLM.from_pretrained('t5-small', return_dict = True)


class summarizer:
    def __init__(self, text):
        self.text = text
    
    def summarize(self, max_length = 200, min_length = 10):
        inputs = tokenizer.encode("summarize: "+self.text, return_tensors = 'pt', max_length = 1024, truncation = True)
        summarize_ids = model.generate(inputs, max_length = max_length, min_length = min_length, length_penalty =3, num_beams = 2)
        summary = tokenizer.decode(summarize_ids[0])
        return summary

    def translate(self):
        inputs = tokenizer.from_pretrained("translate English to German:"+self.text, return_tensors = 'pt', max_length = 1024, truncation = True)
        translation_ids = model.generate(inputs, length_penalty = 4, num_beams = 3)
        translated_text = tokenizer.decode(translation_ids[0])
        return translated_text



# translation = obj.translate()

# print("Translation is: ", translation)