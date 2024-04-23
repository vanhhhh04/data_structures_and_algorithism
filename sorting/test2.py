import random
from collections import defaultdict

def generate_random_string(length):
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=length))

def count_characters(string):
    char_count = defaultdict(int)
    for char in string:
        char_count[char] += 1
    return char_count

def analyze_char_count(char_count_dict):
    max_count = max(char_count_dict.values())
    min_count = min(char_count_dict.values())
    avg_count = sum(char_count_dict.values()) / len(char_count_dict)
    return {"max": max_count, "min": min_count, "avg": avg_count}

def main():
    random_string = generate_random_string(100)
    print("Random String:", random_string)

    char_count_dict = count_characters(random_string)
    print("Character count:", char_count_dict)

    analysis_dict = analyze_char_count(char_count_dict)
    print("Analysis:", analysis_dict)

if __name__ == "__main__":
    main()