"""
Part of Speech(POS) Tagging refers to a task that identifies each token with their part of speech. Part of speech is a grammatical concept that denotes which role a word is playing in a sentence. The examples of them would be noun, verb, adverbs, adjectives, pronouns, etc. 

The significance of POS tagging lies in its ability to enhance the understanding and analysis of textual data. Without POS tagging, we would be limited to the vocabularies and frequencies of appearance in the text. However, by tagging each token with part of speech, it allows models to understand the context and the words usage in a sentence. 

POS tagging is employeed frequently in tasks such as sentiment analysis, syntax analysis, speech recognition, and grammar and style checking.
"""
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize

# We will be using NLTK's POS Tagging class
def samplePOSTagging(): 
    sentence = "John's big idea isn't all that bad."
    tokens = word_tokenize(sentence)

    print(pos_tag(tokens))

# Write a sentence that contains the following: a singular noun (NN tag, ie 'apple'), an adjective(JJ tag, ie 'many', 'big'), and a verb in base form (VB tag, ie 'take').
# And then complete the following function that will:
#   1. tokenize the sentence 
#   2. Tag each token with their respective POS tags
#   3. And return the resulting list 
# The test will verify that the NN, JJ, and VB tag exists somewhere in the returned list of pos tagged word tokens
def posTaggingExercise():
    text = "your_ingenuous_sentence_here"

    return text