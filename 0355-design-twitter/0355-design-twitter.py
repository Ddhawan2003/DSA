class Twitter:

    def __init__(self):
        self.follows = defaultdict(set) # map of user id to set of follows
        self.tweets = defaultdict(list) # map of user id to list of tweets
        self.time=0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        all_follows = self.follows[userId]
        all_follows.add(userId)
        heap = []
        for n in all_follows:
            for time, tweet in self.tweets[n][-10:]:
                heapq.heappush(heap, (-time, tweet))
        feed = []
        while heap and len(feed) < 10:
            _, tweetId = heapq.heappop(heap)
            feed.append(tweetId)
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)