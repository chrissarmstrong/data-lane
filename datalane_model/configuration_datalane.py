'''
This code leverages the Hugging Face GPTNeo model
'''

from transformers import GPTNeoConfig

class DatalaneGPTNeoConfig(GPTNeoConfig):
    def __init__(self, hidden_size=768, num_layers=4, **kwargs):
        super().__init__(**kwargs)

        # CA: We want a hidden size of 768 for compat with the Tiny Stories model
        self.hidden_size = hidden_size
        self.num_layers = num_layers
#        print(f"In DatalaneGPTNeoConfig init: {hidden_size = }, {num_layers = }")
