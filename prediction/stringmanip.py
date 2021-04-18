import re          

stopwords = ("a","|","•", "about","above","after","again","against","all","am","an",
'b','c','d','e','f','g','h','i','j','k','l','m'
"and","any","are","aren't","as","at","be","because","been","before",
"being","below","between","both","but","by","can't","cannot","could",
"couldn't","did","didn't","do","does","doesn't","doing","don't","down",
"during","each","few","for","from","further","had","hadn't","has","hasn't",
"have","haven't","having","he","he'd","he'll","he's","her","here","here's","hers",
"herself","him","himself","his","how","how's","i","i'd","i'll","i'm","i've","if",
"in","into","is","isn't","it","it's","its","itself","let's","me","more","most","mustn't",
"my","myself","no","nor","not","of","off","on","once","only","or","other","ought","our",
"ours","out","over","own","same","shan't","she","she'd","she'll","she's","should",
"shouldn't","so","some","such","than","that","that's","the","their","theirs","them",
"themselves","then","there","there's","these","they","they'd","they'll","they're",
"they've","this","those","through","to","too","under","until","up","very","was",
"wasn't","we","we'd","we'll","we're","we've","were","weren't","what","what's",
"when","when's","where","where's","which","while","who","who's","whom","why",
"why's","with","won't","would","wouldn't","you","you'd","you'll","you're",
"you've","your","yours","yourself","yourselves","us", "also", "can", "keep", "just")

def get_words(paragraph, stopwords = stopwords):
    """
    Returns the list of all
    words in the paragraph
    """
    s = paragraph.strip()
    #removing punctuations.
    s = re.sub(r"[\']\w", '', s)
    s = re.sub(r"[\'\"!@#$%^&*,.]", ' ', s)
    #removing multiple spaces
    s = re.sub(r"\s+", " ", s)
    #removing stopwords 
    return [word for word in s.lower().strip().split(' ') if word not in stopwords]


def get_sentences(paragraph):
    """
    Returns a list of sentences
    in the paragraph and the total
    number of sentences.
    """
    result = re.split(r"\.", paragraph)
    result_len = len(result)
    return ([s.strip() for s in result][:-1], result_len)


def clean_sentence(sentence):
    """
    Returns the words in the sentence.
    """
    return get_words(sentence)


