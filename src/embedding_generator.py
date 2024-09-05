from transformers import AutoTokenizer, AutoModel
import torch

tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
model = AutoModel.from_pretrained('bert-base-uncased')

def generate_embedding(text):
    inputs = tokenizer(text, return_tensors='pt', padding=True, truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).squeeze()

email_embeddings = [(subject, sender, generate_embedding(body)) for subject, sender, body in preprocessed_emails]

for email_item in email_embeddings:
    print("Embedding for email:", email_item[0], email_item[1])
    print("Embedding size:", email_item[2].size())
    print("-" * 50)