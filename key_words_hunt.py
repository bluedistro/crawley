# hunt for key words in a given article
from nltk.corpus import stopwords

def remove_stop_words(document):
    print('removing stopwords')
    """Return document without stopwords"""
    stop = stopwords.words('english')
    document = ' '.join([i for i in document.split() if i not in stop])
    return document

def find_key_word(test_string='Hackernews is a good site while Techcrunch is not so bad'):
    test_string = remove_stop_words(test_string)
    key_file = open('corpus/big.txt')
    data = key_file.read()
    words = data.split()
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word]+=1
        else:
            word_freq[word]=1
    word_prob_dict = {}
    size_corpus = len(words)
    for word in word_freq:
        word_prob_dict[word] = float(word_freq[word])/size_corpus

    prob_list = []
    for word, prob in word_prob_dict.items():
        prob_list.append(prob)
    non_exist_prob = min(prob_list)/2

    words = test_string.split()
    words = set(words)
    test_word_freq = {}
    for word in words:
        if word in test_word_freq:
            test_word_freq[word]+=1
        else:
            test_word_freq[word]=1

    test_word_ba = {}
    for word, freq in test_word_freq.items():
        if word in word_prob_dict:
            test_word_ba[word] = freq/word_prob_dict[word]
        else:
            test_word_ba[word] = freq/non_exist_prob

    test_word_ba_list = []
    for word, ba in test_word_ba.items():
        test_word_ba_list.append((word, ba))

    def sort_func(a, b):
        if a[1] > b[1]:
            return -1
        elif a[1] < b[1]:
            return 1
        return 0

    test_word_ba_list.sort(sort_func)
    return test_word_ba_list[:3]


test = 'The hurt won\'t go away'

print(find_key_word(test_string=test))