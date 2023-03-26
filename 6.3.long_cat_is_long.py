
def count_words(sentence):
    """
    This function receives a string sentence as an argument, and returns a dictionary
    where the keys are the words in the sentence (converted to lowercase and without any punctuation),
    and the values are the length of each word.
    using set to store one time each element(like in the example)
    using list comprehension to save the words

    :param sentence: A string sentence
    :return: A dictionary where the keys are the words in the sentence (converted to lowercase and without any punctuation),
    and the values are the length of each word.
    """

    clean_words = [word.strip(',.:;!?').lower() for word in sentence.split() if word.strip(',.:;!?').isalpha()]
    convert_to_dict_and_count = {the_word: len(the_word) for the_word in clean_words}
    return convert_to_dict_and_count




# ----- TEST -----


sentence = """
You see, wire telegraph is a kind of a very, very long cat.
You pull his tail in New York and his head is meowing in Los Angeles.
Do you understand this?
And radio operates exactly the same way: you send signals here, they receive them there.
The only difference is that there is no cat.
"""
# my result
# print(len(count_words(sentence)))


# the result that i should get:
# expected_result = {'you': 3, 'see': 3, 'wire': 4, 'telegraph': 9, 'is': 2, 'a': 1, 'kind': 4, 'of': 2, 'very': 4, 'long': 4, 'cat': 3, 'pull': 4, 'his': 3, 'tail': 4, 'in': 2, 'new': 3, 'york': 4, 'and': 3, 'head': 4, 'meowing': 7, 'los': 3, 'angeles': 7, 'do': 2, 'understand': 10, 'this': 4, 'radio': 5, 'operates': 8, 'exactly': 7, 'the': 3, 'same': 4, 'way': 3, 'send': 4, 'signals': 7, 'here': 4, 'they': 4, 'receive': 7, 'them': 4, 'there': 5, 'only': 4, 'difference': 10, 'that': 4, 'no': 2}
# print(len(expected_result))



