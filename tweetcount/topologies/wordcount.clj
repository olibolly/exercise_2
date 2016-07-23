(ns wordcount
  (:use     [streamparse.specs])
  (:gen-class))

(defn wordcount [options]
   [
    ;; spout configuration
    {"tweets" (python-spout-spec
          options
          "spouts.tweets.Tweets"
          ["tweet"]
          )
    }
    ;; bolt configuration 1
    {"parse" (python-bolt-spec
          options
          {"tweets" :shuffle}
          "bolts.parse.ParseTweet"
          ["valid_words"]
          :p 2
          )    
    ;; bolt configuration 2
    "tweetcounter" (python-bolt-spec
          options
          {"parse" :shuffle}
          "bolts.tweetcounter.TweetCounter"
          ["word" "count"]
          :p 1
          )   
    }
   ]
)
