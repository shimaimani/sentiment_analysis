import re
import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import TweetTokenizer

def process_tweets(tweet):
    """process tweets
        Input: 
            tweet: a string 
        Output: 
            tweets_clean: a list of clean tweet
    """
    
    stemmer = PorterStemmer()
    stopwords_english = stopwords.words('english')

    stemmer = PorterStemmer()
    stopwords_english = stopwords.words('english') 
    tweet = re.sub(r'^RT[\s]+', '', tweet)
    tweet = re.sub(r'https?:\/\/.*[\r\n]*', '', tweet)
    tweet = re.sub(r'#', '', tweet)
    
    tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True, reduce_len=True)

    # tokenize tweets
    tweet_tokens = tokenizer.tokenize(tweet)
    
    tweets_clean = []
    for w in tweet_tokens:
        if w not in stopwords_english and  w not in string.punctuation:
            
            stem_word = stemmer.stem(w)
            tweets_clean.append(stem_word)
    return tweets_clean

    
   

