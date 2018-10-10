# SimpleBlog 
基于django搭建的简单博客系统。
# chapter1 - 配置数据库模块
## 配置pymysq
```py

# blog/__init__.py

import pymysql
pymysql.install_as_MySQLdb()
```
## ORM
我们需要创建三个类，分别是文章，分类，标签，对应关系如下
```
一对多的关系
1 文章 - 1分类
1 分类 - 多文章
----------------
多对多的关系
1 文章 - 多标签 
1 标签 - 多文章
```
## 完成ORM，进行数据迁移
```
python manage.py makemigrations 
python manage.py migrate  

```