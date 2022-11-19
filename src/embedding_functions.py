from nltk.tokenize import word_tokenize
import pickle, numpy as np


# load vocabulary dict
lookup_dict = pickle.load(open('data/embeddings_dict.obj','rb'))

# create useful functions
def look_up(word):
    """ Function that returns the vocabulary index to an input string (recognised word).
    Input:
        word: a string (element of GoogleNews embeddings)
    Output:
        index: the corresponding vocabulary index
    """
    keys_list = list(lookup_dict)
    index = keys_list.index(word)
    return(index)

def inp2array(string, dict = lookup_dict):
    """" Function that converts the input paragraph into a list of word indices (function name is misleading).
    Input:
        string: input paragraph as string
        dict: look up dictionary of vocabulary
    Output:
        list of word indices
    """
    # replace . and - and / with whitespace (to increase recognised words), tokenise input
    tokens = word_tokenize(string.replace("-", " ").replace("/", " ").replace(".", " "))

    # filter out tokens unknown to vocabulary
    valid_input = []
    for token in tokens:
        if token in dict.keys():
            valid_input.append(look_up(token))
    return valid_input
