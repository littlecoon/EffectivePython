def find_anagrams(word, dictionary):
    """Find all anagrams for a word.

    This function only runs as fast as the test for 
    membership in the 'dictionary' container. It will
    be slow if the dictionary is a list and fast if
    it's a set.

    Args:
        word: String of the target word.
        dictionary: Container with all strings that
            are known to be acctual words.

    Returns:
        List of anagrams that were found. Empty if 
        none were found.
    """
    #...