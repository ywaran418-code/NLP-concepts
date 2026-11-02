import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Download required NLTK resources (runs once)
nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)
nltk.download("stopwords", quiet=True)
nltk.download("wordnet", quiet=True)

# 1. Raw Text
raw_text = "The quick brown fox jumps over the lazy dog. He is a good runner!"
print("1. Raw text:\n", raw_text)

# 2. Lowercasing
lowered_text = raw_text.lower()
print("\n2. Lowered text:\n", lowered_text)

# 3. Cleaning Special Characters (Regex Library)
cleaned_text = re.sub(r"[^a-zA-Z0-9\s]", "", lowered_text)
print("\n3. Cleaned text:\n", cleaned_text)

# 4. Tokenization (NLTK Tokenizer)
tokens = word_tokenize(cleaned_text)
print("\n4. Tokens:\n", tokens)

# 5. Stopwords Removal (NLTK Corpus)
stop_words = set(stopwords.words("english"))
tokens_no_stops = [word for word in tokens if word not in stop_words]
print("\n5. Stopwords Removed:\n", tokens_no_stops)

# 6. Lemmatization (NLTK WordNet Lemmatizer)
lemmatizer = WordNetLemmatizer()
# Lemmatize verbs (pos='v' converts 'jumps' -> 'jump')
lemmatized_tokens = [
    lemmatizer.lemmatize(word, pos="v") for word in tokens_no_stops
]
# Lemmatize nouns (pos='n' converts plural nouns to singular, runner remains runner)
lemmatized_tokens = [
    lemmatizer.lemmatize(word, pos="n") for word in lemmatized_tokens
]
print("\n6. Lemmatized Tokens:\n", lemmatized_tokens)

# 7. Clean Data (Reconstructed Text)
clean_data = " ".join(lemmatized_tokens)
print("\n7. Clean Data:\n", clean_data)