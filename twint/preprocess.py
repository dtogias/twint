import html

import re
import unicodedata


def html_decode(sample):
    return html.unescape(sample)

def remove_user_handle(sample):
    return re.sub(r"@[\w]+","",sample)


def remove_punctuation_simple(sample):

    normalized = str(sample)
    # normalized = normalized.replace('.', ' ')
    # normalized = normalized.replace('. ', ' ')
    # normalized = normalized.replace('..', ' ')
    normalized = normalized.replace('!', ' ')
    normalized = normalized.replace('?', ' ')
    normalized = normalized.replace('; ', ' ')
    # normalized = normalized.replace(',', ' ')
    normalized = normalized.replace(':', ' ')
    normalized = normalized.replace('-', ' ')
    normalized = normalized.replace('–', ' ')
    normalized = normalized.replace('(', ' ')
    normalized = normalized.replace(')', ' ')
    normalized = normalized.replace('[', ' ')
    normalized = normalized.replace(']', ' ')
    normalized = normalized.replace('{', ' ')
    normalized = normalized.replace('}', ' ')

    return normalized


def remove_URL(sample):
    """Remove URLs from a sample string"""
    return re.sub(r"http\S+", "", sample)


def remove_multiple_whitespace(sample):
    return re.sub(' +', ' ', sample)

def remove_non_ascii(words):
    """Remove non-ASCII characters from list of tokenized words"""
    new_words = []
    for word in words:
        new_word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        new_words.append(new_word)
    return new_words


def remove_punctuation(words):
    """Remove punctuation from list of tokenized words"""
    new_words = []
    for word in words:
        new_word = re.sub(r'[^\w\s]', '', word)
        if new_word != '':
            new_words.append(new_word)
    return new_words
