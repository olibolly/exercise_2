import tweepy

consumer_key = "PZXHmQZmybZ1fT3FDEibSJSDQ";
#eg: consumer_key = "YisfFjiodKtojtUvW4MSEcPm";


consumer_secret = "9v0kvcYFtPUGdHZLw1cocZsMrMEFV9cEk9o616RAwI5UC7Rykw";
#eg: consumer_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token = "22124783-glipkzJpVTNc9kKsRA82UxCuTjqkNbJPi3TrUtsDb";
#eg: access_token = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token_secret = "dvQeX4eOGeHBUPrQ17VK3PcYvtwosb7wZzNaIWqNRnziu";
#eg: access_token_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



