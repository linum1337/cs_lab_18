import string
from collections import Counter

def get_stats(filename):
    with open(filename, 'r') as f:
        text = f.read().lower()
        text = ''.join(c for c in text if c not in string.punctuation)
        words = text.split()

    letter_counts = Counter()
    total_words = len(words)

    for word in words:
        letter_counts.update(word)

    letter_stats = {letter: count / total_words * 100 for letter, count in letter_counts.items()}

    return letter_stats

def main():
    filename = '/Users/vladislavcehov/cs_lab_18/text_for_stat.txt'
    stats = get_stats(filename)
    cyrillic_lower_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    for letter in cyrillic_lower_letters:
        print(f"Буква {letter}: {stats.get(letter, 0)}%")

    least_common = min(stats, key=stats.get)
    print(f"\nСамая распространенная буква: {least_common}")

if __name__ == "__main__":
    main()
