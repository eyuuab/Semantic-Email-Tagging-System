import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

tag_descriptions = {
    "Meeting (Urgent)": "This email is about an important meeting that requires immediate attention.",
    "Personal": "This email is personal and contains messages between friends or family.",
    "Notification": "This email provides a notification or update, usually from a service or company.",
    "Spam": "This email contains unsolicited and irrelevant information, winning and get suprise"
}

tag_embeddings = {tag: generate_embedding(description) for tag, description in tag_descriptions.items()}

def assign_tags(email_embedding, tag_embeddings):
    similarities = {tag: cosine_similarity(email_embedding.unsqueeze(0), tag_embedding.unsqueeze(0)).item()
                    for tag, tag_embedding in tag_embeddings.items()}
    sorted_tags = sorted(similarities.items(), key=lambda x: x[1], reverse=True)
    return sorted_tags[:2]

tagged_emails = [(subject, sender, assign_tags(embedding, tag_embeddings)) for subject, sender, embedding in email_embeddings]

for email in tagged_emails:
    print(f"Email: {email[0]} from {email[1]}")
    print(f"Assigned Tags: {email[2]}")
    print("-" * 50)