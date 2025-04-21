def are_shadow_sentences(sentence1, sentence2):
    # Split both sentences into words
    words1 = sentence1.split()
    words2 = sentence2.split()

    # Check if the sentences have the same number of words
    if len(words1) != len(words2):
        return False
    
    # Check each word pair for the same length and no common letters
    for w1, w2 in zip(words1, words2):
        if len(w1) != len(w2):  # Words must be the same length
            return False
        
        # Check if any letter appears in both words
        if any(letter in w2 for letter in w1):
            return False
    
    return True

# Example usage
sentence1 = "they are round"
sentence2 = "fold two times"
result = are_shadow_sentences(sentence1, sentence2)
print(result)  # Output: True

sentence1 = "his friends"
sentence2 = "our company"
result = are_shadow_sentences(sentence1, sentence2)
print(result)  # Output: False
