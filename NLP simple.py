raw_text = ("The quick brown fox jumps over the lazy dog. He is a good runner!")
print( " 1. Raw text ;" , raw_text)
lowered_text = raw_text.lower()
print("Lower Text: " , lowered_text)
cleaned_text = "".join(
    char for char in lowered_text if char.isalnum() or char.isspace()
)
print( "3.Cleaned text:", cleaned_text)
tokens = cleaned_text.split()
print("4. Tokens:", tokens)
stop_words = ["the", "over", "he", "is", "a"]
tokens_no_stops = [word for word in tokens if word not in stop_words]
print("5. Stopwords Removed:", tokens_no_stops)
lemma_lookup = {"jumps": "jump", "runner": "run"}
lemmatized_tokens = [
    lemma_lookup.get(word, word) for word in tokens_no_stops
]
print("7. Lemmatized:", lemmatized_tokens)
clean_data = " ".join(lemmatized_tokens)
print("8. Clean Data:", clean_data)