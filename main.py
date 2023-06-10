import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained('t5-small')
# model = AutoModelWithLMHead.from_pretrained('t5-small', return_dict = True)
model = AutoModelForCausalLM.from_pretrained('t5-small', return_dict = True)


class summarizer:
    def __init__(self, text):
        self.text = text
    
    def model(self, max_length = 200, min_length = 50):
        inputs = tokenizer.encode("summarize: "+self.text, return_tensors = 'pt', max_length = 1024, truncation = True)
        summarize_ids = model.generate(inputs, max_length = max_length, min_length = min_length, length_penalty =2, num_beams = 1)
        summary = tokenizer.decode(summarize_ids[0])
        return summary

    def translate(self):
        inputs = tokenizer.from_pretrained("translate English to German:"+self.text, return_tensors = 'pt', max_length = 1024, truncation = True)
        translation_ids = model.generate(inputs, length_penalty = 4, num_beams = 3)
        translated_text = tokenizer.decode(translation_ids[0])
        return translated_text

obj = summarizer("""Our mission is driven by the undeniable need to break down the barriers that limit visually impaired individual’s access to educational materials. The challenges they face in traditional learning methods, such as reading books or utilizing online resources, cannot be ignored. These methods heavily rely on visual cues and extensive text, making it arduous for visually impaired learners to access and comprehend study materials within a limited timeframe, thereby impeding their educational progress. Moreover, Blind individuals encounter difficulties when it comes to effectively taking notes and organizing their study materials for future use.
To overcome these obstacles, visually impaired individuals often rely on sighted assistance from family members, friends, or teachers. However, this dependency limits their independence and prevents them from learning at their own pace, hindering their academic growth and self-confidence.
Furthermore, the digital shift in education further exacerbates the exclusion of visually impaired individuals. Graphs, images, and other visual elements remain inaccessible, excluding them from a wealth of digital educational resources. While braille and assistive technologies exist, their availability is limited, and they may not fully address the diverse needs of visually impaired learners.""")

summary = obj.model(max_length= 100)

print("Summary is: ", summary)

# translation = obj.translate()

# print("Translation is: ", translation)