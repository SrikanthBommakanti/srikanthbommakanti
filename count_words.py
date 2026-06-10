def count_words(s, n):
    # Input validation
    if not s or n <= 0:
        return []
    
    # Split the string into words and convert to lowercase for case-insensitive counting
    words = s.lower().split()
    
    # Count the occurrences of each word
    counters = {}
    for word in words:
        # Remove common punctuation
        word = word.strip('.,!?;:')
        if word:
            counters[word] = counters.get(word, 0) + 1
    
    # Sort the words by frequency (descending), then alphabetically (ascending)
    top = sorted(counters.items(), key=lambda d: (-d[1], d[0]))
    
    # Get the top n words
    top_n = top[:n]
    return top_n

def test_run():
    print(count_words("cat bat mat cat bat cat", 3))
    # Test with punctuation and mixed case
    print(count_words("Cat, bat! Mat. Cat, bat, cat.", 3))
    # Test edge cases
    print(count_words("", 3))
    print(count_words("hello world", 0))

if __name__ == '__main__':
    test_run()
