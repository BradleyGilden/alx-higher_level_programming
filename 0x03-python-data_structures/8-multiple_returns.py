#!/usr/bin/python3

# returns first character of a sentence and it's length
def multiple_returns(sentence):
    if sentence == "" or sentence is None:
        return(0, None)
    else:
        a_len = len(sentence)
        return (a_len, sentence[0])
