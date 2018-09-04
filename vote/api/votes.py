from vote.models.article import Article
import uuid
import logging
from flask import Blueprint

logger = logging.getLogger("vote")

vote = Blueprint('vote', __name__)


@vote.route("/add", ["POST"])
def add_article():
    id = Article.add_article("G0 to statement considered harmful", "http://goo.gl/kZUSu", "人民邮电出版社")
    logger.info("添加成功！")
    print("添加成功！")
    return id


@vote.route("/vote", ["POST"])
def vote(code: str):
    usid = uuid.uuid1()
    Article.vote_article(code, usid)
    print("投票成功！")


@vote.route("/get", ["POST"])
def get_articles():
    articles = Article.get_articles(1)
    print(articles)


article_id = add_article()
vote(article_id)
get_articles()
