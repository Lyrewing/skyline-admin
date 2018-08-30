import uuid, time
from vote.libs import redis

ONE_WEEK_IN_SECONDS = 7 * 86400
VOTE_SCORE = 5
PAGE_SIZE = 10


class Article:
    title = None
    link = None
    poster = None
    time = None
    votes = 0

    def __init__(self, title, link, poster):
        self.title = title
        self.link = link
        self.poster = poster
        self.time = time.time()
        self.votes = 0

    @staticmethod
    def add_article(title, link, poster):
        # 添加文章
        code = str(uuid.uuid1())
        create_at = time.time()
        article = {"title": title, "link": link, "poster": poster, "time": create_at, "votes": 0}
        hkey = "article:" + code
        redis.hmset(hkey, article)

        # 将时间写入到有序的集合中
        redis.zadd("time:", code, create_at)
        redis.zadd("score:", code, 0)

        # 如果文章发布一周后讲voted进行删除

        redis.expire("voted:" + code, ONE_WEEK_IN_SECONDS)

        return code

    @staticmethod
    def vote_article(code: str, user: str):
        cutoff = time.time() - ONE_WEEK_IN_SECONDS
        if redis.zscore("time:", code) < cutoff:
            return
        skey = "voted:" + code
        if redis.sadd(skey, user):
            redis.zincrby("score:", code, amount=VOTE_SCORE)
            redis.hincrby("article:" + code, "votes", amount=1)
        pass

    @staticmethod
    def get_articles(page_index):
        start = (page_index - 1) * PAGE_SIZE
        end = start + PAGE_SIZE - 1
        ids = redis.zrevrange("score:", start, end)
        articles = []
        for id in ids:
            id = id.decode(encoding="UTF-8")
            article_data = redis.hgetall("article:" + id)
            article_data['id'] = id
            articles.append(article_data)
        return articles
