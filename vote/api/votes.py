from vote.models.article import Article
import uuid
import logging

logger = logging.getLogger("vote")


def add_article():
    id = Article.add_article("G0 to statement considered harmful", "http://goo.gl/kZUSu", "人民邮电出版社")
    logger.info("添加成功！")
    print("添加成功！")
    return id


def vote(code: str):
    usid = uuid.uuid1()
    Article.vote_article(code, usid)
    print("投票成功！")


def get_articles():
    articles = Article.get_articles(1)
    print(articles)


article_id = add_article()
vote(article_id)
