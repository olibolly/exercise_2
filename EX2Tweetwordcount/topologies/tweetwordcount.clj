(ns tweetwordcount
  (:use     [streamparse.specs])
  (:gen-class))

(defn tweetwordcount [options]
   [
    ;; spout configuration
    {"tweet-spout" (python-spout-spec
          options
          "spouts.tweetsTest.Sentences"
          ["sentence"]
          )
    }
    ;; bolt configuration
    {"parse-tweet-bolt" (python-bolt-spec
          options
          {"tweet-spout" :shuffle}
          "bolts.parseTest.ParseTweet"
          ["valid_words"]
          :p 2
          )
    "count-bolt" (python-bolt-spec
          options
          {"parse-tweet-bolt" :shuffle}
          "bolts.wordcountTest.TweetCounter"
          ["word" "count"]
          :p 1
          )
    }
  ]
)
