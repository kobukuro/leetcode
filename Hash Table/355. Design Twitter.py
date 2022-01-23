# Hash Table, Linked List, Design, Heap(Priority Queue)
# TODO need to be improved
from typing import List
import datetime
from operator import itemgetter


class Twitter:

    def __init__(self):
        self.user_feed = {}
        self.follow_list = {}  # 誰follow誰
        self.tweets = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = [[tweetId, datetime.datetime.now()]]
        else:
            self.tweets[userId].append([tweetId, datetime.datetime.now()])

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets_to_show = []
        if userId in self.tweets:
            for tweet in self.tweets[userId]:
                tweets_to_show.append(tweet)
        if userId in self.follow_list:
            for user in self.follow_list[userId]:
                if user in self.tweets:
                    for tweet in self.tweets[user]:
                        tweets_to_show.append(tweet)
        tweets_to_show = sorted(tweets_to_show, key=itemgetter(1), reverse=True)
        tweets_to_show = [tweet[0] for tweet in tweets_to_show]
        tweets_to_show = tweets_to_show[0:10]
        return tweets_to_show

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follow_list:
            self.follow_list[followerId] = [followeeId]
        else:
            if followeeId not in self.follow_list[followerId]:
                self.follow_list[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follow_list:
            self.follow_list[followerId].remove(followeeId)


if __name__ == '__main__':
    # ["Twitter","postTweet","getNewsFeed","follow","getNewsFeed","unfollow","getNewsFeed"]
    # [[],[1,1],[1],[2,1],[2],[2,1],[2]]
    tw = Twitter()
    tw.postTweet(1, 5)
    # print(tw.tweets)
    print(tw.getNewsFeed(1))
