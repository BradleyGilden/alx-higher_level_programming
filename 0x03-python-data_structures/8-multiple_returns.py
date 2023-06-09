#!/usr/bin/python3

# returns first character of a sentence and it's length
def multiple_returns(sentence):
    return (len(sentence), sentence[0] if sentence is None else None)
