# Twitter API credentials
API_KEY = __________________
API_SECRET_KEY = _______________________
ACCESS_TOKEN = ______________________
ACCESS_TOKEN_SECRET = _____________________

# Authenticate with Tweepy
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def fetch_tweets(keyword, count=100):
    """
    Fetch tweets containing a specific keyword.

    Parameters:
    keyword (str): The keyword to search for.
    count (int): The number of tweets to fetch.

    Returns:
    list: List of tweets.
    """
    tweets = tweepy.Cursor(api.search_tweets, q=keyword, lang="en").items(count)
    tweet_list = [tweet.text for tweet in tweets]
    return tweet_list

def analyze_sentiment(tweet):
    """
    Analyze the sentiment of a tweet.

    Parameters:
    tweet (str): The tweet text.

    Returns:
    str: Sentiment (Positive, Negative, Neutral).
    """
    analysis = TextBlob(tweet)
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity < 0:
        return "Negative"
    else:
        return "Neutral"

def twitter_sentiment_analysis(keyword, count=100):
    """
    Perform sentiment analysis on tweets and visualize results.

    Parameters:
    keyword (str): The keyword to search for.
    count (int): The number of tweets to fetch and analyze.
    """
    # Fetch tweets
    tweets = fetch_tweets(keyword, count)

    # Analyze sentiment
    sentiments = [analyze_sentiment(tweet) for tweet in tweets]

    # Create a DataFrame
    df = pd.DataFrame({"Tweet": tweets, "Sentiment": sentiments})

    # Print the first few rows
    print(df.head())

    # Visualize the sentiment distribution
    sentiment_counts = df["Sentiment"].value_counts()
    sentiment_counts.plot(kind="bar", color=["green", "red", "blue"])
    plt.title(f"Sentiment Analysis for '{keyword}'")
    plt.xlabel("Sentiment")
    plt.ylabel("Count")
    plt.show()

# Run the analysis
twitter_sentiment_analysis("Python", count=200)
