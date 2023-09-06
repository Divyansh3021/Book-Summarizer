import torch
from transformers import AutoTokenizer, AutoModelWithLMHead, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained('t5-small')
model = AutoModelWithLMHead.from_pretrained('t5-small', return_dict = True)
# model = AutoModelForSeq2SeqLM.from_pretrained("sgugger/my-awesome-model")
# model = AutoModelForCausalLM.from_pretrained('t5-small', return_dict = True)


class summarizer:
    
    def summarize(self,text, max_length = 400):
        inputs = tokenizer.encode("summarize: "+text, return_tensors = 'pt', max_length = 1024, truncation = True)
        summarize_ids = model.generate(inputs, max_length = max_length, min_length = 20, length_penalty =3, num_beams = 2)
        summary = tokenizer.decode(summarize_ids[0])
        return summary

    def translate(self):
        inputs = tokenizer.from_pretrained("translate English to German:"+self.text, return_tensors = 'pt', max_length = 1024, truncation = True)
        translation_ids = model.generate(inputs, length_penalty = 4, num_beams = 3)
        translated_text = tokenizer.decode(translation_ids[0])
        return translated_text



# obj = summarizer()
# summary = obj.summarize("I apologize for any confusion earlier. It's possible that the issue with text extraction might be due to specific encoding or formatting within the PDF. In that case, you might want to experiment with different extraction methods provided by PyMuPDF to see if you can get the desired result. here's an approach that attempts to use different PyMuPDF methods to extract text, which might work better for your PDF:")

# print(summary)