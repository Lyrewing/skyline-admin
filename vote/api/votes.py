from vote.models.article import Article
import uuid, json
import logging
from flask import Blueprint, request, Response
from admin.libs.error import *

logger = logging.getLogger("vote")

votes = Blueprint('vote', __name__)


@votes.route("/add", methods=["POST"])
def add_article():
    data = request.json
    name = data["name"]
    author = data["author"]
    summary = data["summary"]
    cover = data["cover"]
    try:
        id = Article.add_article(name, author, summary, cover)
        logger.info("添加成功！")
        return Success()
    except Exception as err:
        logger.error("添加失败！")
        return ServerException()


@votes.route("/vote", methods=["POST"])
def vote():
    code = request.json["code"]
    usid = uuid.uuid1()
    try:
        Article.vote_article(code, usid)
        logger.info("投票成功！")
        return Success()
    except Exception as err:
        logger.error("添加失败！")
        return ServerException()


@votes.route("/list", methods=["GET"])
def get_article():
    try:
        articles = Article.get_articles(1)
        json_str = json.dumps(articles)
        return Response(json_str, mimetype="application/json")
    except Exception as err:
        logger.error("获取失败！")
        return ServerException()


"""
article_id = add_article()
vote(article_id)
get_articles()
"""
