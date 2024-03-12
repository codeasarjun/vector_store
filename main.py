from core.create_vetore_store import vectorStore

import numpy as np

vector_Store=vectorStore()
sentences = [
    "I eat mango",
    "mango is my favorite fruit",
    "mango, apple, oranges are fruits",
    "fruits are good for health",
]

# Tokenization and Vocabulary Creation
vocabulary = set()
for sentence in sentences:
    tokens = sentence.lower().split()
    vocabulary.update(tokens)

# Assign unique indices to words in the vocabulary
word_to_index = {word: i for i, word in enumerate(vocabulary)}
# Vectorization
sentence_vectors = {}
for sentence in sentences:
    tokens = sentence.lower().split()
    vector = np.zeros(len(vocabulary))
    for token in tokens:
        vector[word_to_index[token]] += 1
    sentence_vectors[sentence] = vector

# Storing in VectorStore
for sentence, vector in sentence_vectors.items():
    vector_Store.add_vector(sentence, vector)

# Searching for Similarity
query_sentence = "Mango is the best fruit"
query_vector = np.zeros(len(vocabulary))
query_tokens = query_sentence.lower().split()
for token in query_tokens:
    if token in word_to_index:
        query_vector[word_to_index[token]] += 1

similar_sentences = vector_Store.find_similar_vector(query_vector, num_results=2)

# Print similar sentences
print("Query Sentence:", query_sentence)
print("Similar Sentences:")
for sentence, similarity in similar_sentences:
    print(f"{sentence}: Similarity = {similarity:.4f}")