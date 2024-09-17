from bio_ml_models import BioModelCollection

from biotrainer.embedders.one_hot_encoding_embedder import OneHotEncodingEmbedder

# Load collection
collection = BioModelCollection()

# Attribute-style access
aav_flip = collection.proteins.adeno_associated_virus_fitness.aav_flip

# Dictionary-style access
aav_flip = collection["proteins"]["adeno_associated_virus_fitness"]["aav_flip"]

# Example sequences, shortened from the training set
example_sequences = ["SEPRPIGTRYLTRNL", "EPRPIGTRYLTRNL"]

# Embed
one_hot_encoding_embedder = OneHotEncodingEmbedder()
embeddings = {f"Sequence{i}": one_hot_encoding_embedder.reduce_per_protein(embd) for i, embd in
              enumerate(one_hot_encoding_embedder.embed_many(sequences=example_sequences))}

# Predict and print result
print(aav_flip.predict(input_data=embeddings))
