import re
import tweepy
from langdetect import detect_langs
import win32com.client
auth = tweepy.OAuthHandler("WZ9VoayS9f6fsz9ReWYiRi3aQ", "TXqNig43nkJivD7ofNQbwFL7UVt5PLtnNmi9zdXLJ1KYoGF4TB")
auth.set_access_token("231249661-297yAWMEqfKNdkookgBjbsqWveqcJ699lfjV0pcx", "M0vpMcPuAbH2Lx5e8IBTqTFv7asyc1DsYs7dG9oUy9eoW")
api = tweepy.API(auth)

username='imVKohli'

my_tweets = api.user_timeline(screen_name=username,count=20)
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
def Speak(text):
    win32com.client.Dispatch("SAPI.SpVoice").Speak(text)       
def sentiment_scores(sentence):
    sid_obj = SentimentIntensityAnalyzer() 
    sentiment_dict = sid_obj.polarity_scores(sentence) 
    print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative") 
    print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral") 
    print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive") 
    Speak("Sentence Overall Rated As")
    print("Sentence Overall Rated As", end = ":") 

    if sentiment_dict['compound'] >= 0.05 :
        Speak('positive')
        print('Positive') 
  
    elif sentiment_dict['compound'] <= - 0.05 : 
        Speak('negative')
        print("Negative") 
        
if __name__ == "__main__" :
    Speak("following are some tweets by "+api.get_user(username).name)
    for t in my_tweets:
        text=t.text
        text = re.sub(r'http\S+', '', text)
        if str(detect_langs(text)[0])[0:2] == 'en':
            print(text,'\n')
            Speak(text)
            sentiment_scores(text)
