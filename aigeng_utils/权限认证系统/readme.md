## 如何运行

web框架使用Flask，ORM使用Flask-SQLAlchemy，需要安装相应的包。数据库使用mysql，配置`user_permission.py`中第15行的数据库URI，使用相应的数据库导入`forum.sql`，其中包含了表结构和测试数据。

然后运行`user_permission.py`，会使用本地5000端口提供服务

## 一些例子

以如下形式访问:
```
http://127.0.0.1:5000/user/<user_id>/article/<article_id>
```
表示使用`user_id`对应的用户去操作`article_id`对应的文章，测试数据中有两个用户，id为0的用户是管理员，id为1的用户是普通用户，分别有两篇文章。使用curl的一些测试结果：
```
正常GET：
curl http://127.0.0.1:5000/user/0/article/0

{
  "code": 0,
  "data": {
    "id": 0,
    "text": "this is article_0_test text",
    "title": "title_of_0",
    "user_id": 0,
    "user_name": "XiaoMing"
  },
  "message": "ok: get"
}

正常PUT(修改文章):
curl -H "Content-Type: application/json" -X PUT -d '{"text": "Oh, The artile changed"}' http://127.0.0.1:5000/user/0/article/1

{
  "code": 0,
  "data": {},
  "message": "ok: put"
}

正常DELETE(删除文章):
curl -H "Content-Type: application/json" -X DELETE  http://127.0.0.1:5000/user/1/article/2

{
  "code": 0,
  "data": {},
  "message": "ok: delete"
}

无权限PUT(修改文章):
curl -H "Content-Type: application/json" -X PUT -d '{"text": "Oh, The artile changed"}' http://127.0.0.1:5000/user/1/article/0

{
  "code": 1,
  "data": {},
  "message": "error: no permission"
}

无权限DELETE(删除文章):
curl -H "Content-Type: application/json" -X DELETE  http://127.0.0.1:5000/user/1/article/0

{
  "code": 1,
  "data": {},
  "message": "error: no permission"
}

```