(ns tweetwordcount
  (:use     [streamparse.specs])
  (:gen-class))

(defn tweetwordcount [options]
   [
    ;; spout configuration
   {"sentences" (python-spout-spec
          options
          "spouts.tweetsTest.Sentences"
          ["sentence"]
          )
    }
    ;; bolt configuration 1
    {"parse" (python-bolt-spec
          options
          {"sentences" :shuffle}
          "bolts.parseTest.ParseTweet"
          ["valid_words"]
          :p 2
          )
    ;; bolt configuration 2
    "tweetcounter" (python-bolt-spec
          options
          {"parse" :shuffle}
          "bolts.wordcountTest.TweetCounter"
          ["word" "count"]
          :p 1
          )
    }
  ]
)
