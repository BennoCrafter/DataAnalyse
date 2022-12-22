from collections import defaultdict

word_for_analyse = input("Für welches Wort sollen die Häufigkeiten dargelegt werden?:")
data_dict = {}


def read_data(filename):
    global data
    data = []
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split('|')
            data.append((parts[0], parts[1])) # parts[0] = hallo parts[1] = hey
    print(parts)
    return data


def create_word_count_dict(data):
    global word_count
    word_count = defaultdict(int)
    for first_word, second_word in data:
        word_count[second_word] += 1
    return word_count


def calculate_frequency(word, word_count, data):
    count = word_count[word]
    frequency = count / data * 100
    return frequency


word_count = create_word_count_dict(data=read_data("data.txt"))
max_count = max(word_count.items(), key=lambda x: x[1])
max_key = max_count[0]
max_frequency = calculate_frequency(max_key, word_count, len(data))

print("Das meist häufige Wort auf " + word_for_analyse + " ist " + max_key + " mit der Häufigkeit von " + str(max_frequency) + "%")

# testing
print("\n")
print("Testing Phase:")
print(dict(word_count))