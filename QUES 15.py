def reverse_words(sentence):
    # Split the sentence into words
    words = sentence.split()
    reversed_words = words[::-1]
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence

input_sentence = "Python is fun"
output_sentence = reverse_words(input_sentence)
print("Reversed Sentence:", output_sentence)
