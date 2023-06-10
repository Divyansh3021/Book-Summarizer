import torch
from transformers import AutoTokenizer, AutoModelWithLMHead

tokenizer = AutoTokenizer.from_pretrained('t5-small')
model = AutoModelWithLMHead.from_pretrained('t5-small', return_dict = True)
# model = AutoModelForCausalLM.from_pretrained('t5-small', return_dict = True)


class summarizer:
    def __init__(self, text):
        self.text = text
    
    def summarize(self, max_length = 200, min_length = 50):
        inputs = tokenizer.encode("summarize: "+self.text, return_tensors = 'pt', max_length = 1024, truncation = True)
        summarize_ids = model.generate(inputs, max_length = max_length, min_length = min_length, length_penalty =2, num_beams = 1)
        summary = tokenizer.decode(summarize_ids[0])
        return summary

    def translate(self):
        inputs = tokenizer.from_pretrained("translate English to German:"+self.text, return_tensors = 'pt', max_length = 1024, truncation = True)
        translation_ids = model.generate(inputs, length_penalty = 4, num_beams = 3)
        translated_text = tokenizer.decode(translation_ids[0])
        return translated_text

obj = summarizer("""Greetings, VIPNAN (The marketing club of usms) is organising a "RECYCLE RIDDLES" event where participants have to make a creative product using the waste material. So Set your calendars🗓️ for 14th june 2023
       
✨♦️EVENT DESCRIPTION ♦️✨

Participants have to make a team of two people and give their teams an innovative name. Individual players are also welcome. 

ROUND 1  
Digital puzzle solving- The team who solves the puzzle first, will get the chance to pick the items first, from which they'll make the final product.

ROUND 2  

Marketing Quiz round where Best 5 teams will be selected. 

ROUND 3
Make a unique product from the items (waste materials) selected by the participants in the first round.
Give the product a tag line, USP,etc.


Don't think 💬 much and just register yourselves.""")

summary = obj.summarize(max_length= 100)

print("Summary is: ", summary)

# translation = obj.translate()

# print("Translation is: ", translation)