#!/usr/bin/env python3

import os
from enum import Enum
from flask import Flask, request, render_template, url_for, abort, jsonify
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_mapping(
    SECRET_KEY='permission_demo_key',
    SQLALCHEMY_DATABASE_URI='mysql://root:loroot@localhost:3306/forum',
    SQLALCHEMY_COMMIT_ON_TEARDOWN=True,
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)

db = SQLAlchemy()
db.init_app(app)


class Role(Enum):
    """角色枚举"""
    Admin = 0
    NormalUser = 1


class Restful():
    """RESTFUL 响应"""

    def __init__(self, code, message, data):
        self.code = code
        self.message = message
        self.data = data

    def to_dict(self):
        return {'code': self.code, 'message': self.message, 'data': self.data}


# 数据库Model

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.ForeignKey('user.id'), nullable=False, index=True)
    title = db.Column(db.String(255))
    text = db.Column(db.Text)
    user = db.relationship('User', primaryjoin='Article.user_id == User.id', backref='articles')

    def to_dict(self):
        return {'id': self.id, 'user_id': self.user_id, 'title': self.title, 'text':
            self.text, 'user_name': self.user.name}


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    role = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())


def permission_check(user, article, action):
    """权限验证"""
    if (user.role == Role.NormalUser.value):
        if action == "delete" or action == "put":
            if user.id != article.user_id:
                return False
    return True


@app.errorhandler(404)
def page_not_found(e):
    return jsonify(Restful(1, "error: ", {}).to_dict()), 404


@app.errorhandler(400)
def page_not_found(e):
    return jsonify(Restful(1, "error: ", {}).to_dict()), 400


@app.route("/user/<int:u_id>/article/<int:a_id>", methods=['GET', 'DELETE', 'PUT'])
def get_article(u_id, a_id):
    article = Article.query.filter_by(id=a_id).first()
    user = User.query.filter_by(id=u_id).first()
    if not (article and user):
        return jsonify(Restful(1, "find article or user error", {}).to_dict())
    if request.method == "GET":
        return jsonify(Restful(0, "ok: get", article.to_dict()).to_dict())
    elif request.method == "DELETE":
        if permission_check(user, article, "delete"):
            db.session.delete(article)
            db.session.commit()
        else:
            return jsonify(Restful(1, "error: no permission", {}).to_dict())
        return jsonify(Restful(0, "ok: delete", {}).to_dict())
    elif request.method == "PUT":
        if permission_check(user, article, "put"):
            article.text = request.json.get('text', article.text)
            db.session.commit()
        else:
            return jsonify(Restful(1, "error: no permission", {}).to_dict())
        return jsonify(Restful(0, "ok: put", {}).to_dict())
    else:
        abort(400)
        pass
    return jsonify(Restful(1, "unknown request", {}).to_dict())


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
