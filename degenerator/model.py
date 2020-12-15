import random
import time
from random import randint

from transformers import GPT2LMHeadModel, GPT2Tokenizer


class TextDegenerator:
    def __init__(self):
        random.seed(time.time())
        try:
            self.tokenizer = GPT2Tokenizer.from_pretrained("./models/gpt2/")
            self.model = GPT2LMHeadModel.from_pretrained(
                "./models/gpt2/", pad_token_id=self.tokenizer.eos_token_id
            )
        except Exception:
            self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
            self.model = GPT2LMHeadModel.from_pretrained(
                "gpt2", pad_token_id=self.tokenizer.eos_token_id
            )

    def generate(self):
        text = "What should i say to you my friend?"

        input_ids = self.tokenizer.encode(text, return_tensors="pt")

        beam_outputs = self.model.generate(
            input_ids,
            max_length=500,
            num_beams=7,
            no_repeat_ngram_size=2,
            num_return_sequences=5,
            early_stopping=True,
        )
        return self.tokenizer.decode(
            beam_outputs[randint(0, len(beam_outputs))], skip_special_tokens=True
        )
