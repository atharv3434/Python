"""
Exercise 11: Group Anagrams
Write a program that starts with a list of strings defined at the top of your script
(e.g., words = ["eat", "tea", "tan", "ate", "nat", "bat"]) 
and groups the anagrams (words formed by rearranging letters) together. 
Print the final grouped list of lists.

Hardcoded Input: words = ["eat", "tea", "tan", "ate", "nat", "bat"]
Sample Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
"""

from collections import defaultdict

# Hardcoded input defined at the top
words = ["eat", "tea", "tan", "ate", "nat", "bat"]


def group_anagrams(word_list: list[str]) -> list[list[str]]:
    """Groups words that share the same sorted character sequence."""
    anagram_map = defaultdict(list)

    for word in word_list:
        # Sorting characters creates a canonical signature common to all anagrams
        # e.g., sorted('eat') -> ['a', 'e', 't'] -> key 'aet'
        canonical_key = "".join(sorted(word))
        anagram_map[canonical_key].append(word)

    # Return the grouped lists
    return list(anagram_map.values())


def main():
    result = group_anagrams(words)
    print(result)


if __name__ == "__main__":
    main()