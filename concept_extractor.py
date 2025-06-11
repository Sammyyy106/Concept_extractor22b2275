import re
from nltk.stem import PorterStemmer
from fuzzywuzzy import process

ps = PorterStemmer()

def extract_concepts(text, concept_dict, threshold=80):
    text = text.lower()
    words = re.findall(r'\b\w+\b', text)
    stems = [ps.stem(word) for word in words]
    matched_concepts = set()
    all_keys = list(concept_dict.keys())

    for word in words + stems:
        match, score = process.extractOne(word, all_keys)
        if score >= threshold:
            matched_concepts.update(concept_dict[match])

    return list(matched_concepts) if matched_concepts else ["No concept matched"]

