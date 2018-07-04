# 问卷调查系统

基于Django框架的内网（局域网）问卷调查网站，后台数据库使用自带sqlite3，问卷题目为单选。

## Install
### 环境依赖
* python3.6
* django>=.9,<2
* sqlite3

### 下载
``` bash
git clone https://github.com/binyi10/questionnaire.git
```

### 服务器ip添加
* 进入
questionnaire/DjangoWebProject_questionnaire/DjangoWebProject_ques/DjangoWebProject_ques目录
* 在setteing.py文件中 ALLOWED_HOSTS中添加你服务器的ip（比如你的ip是127.0.0.0）
![添加ip](https://raw.githubusercontent.com/LiangCY/questionnaire/master/screenshots/index.jpg)

### Run
``` bash
cd questionnaire/DjangoWebProject_questionnaire/DjangoWebProject_questionnaire

python manage.py runserver 0.0.0.0：8080   
```
* 内网中的用户，就可以访问如下网址了（如果不行，修改你的防火墙试试）
* [http://127.0.0.0:8080/questionnaire/start](http://127.0.0.0:8080/questionnaire/start)

### 数据库设计
* users表:存访问网站的ip，以及每个ip当前做到第几页
* dataquery2表：存问卷中所有的问题
* result_final表：存每个用户填完问卷之后的结果
* 数据库在DjangoWebProject_questionnair目录下：db.sqlite3

[Live Demo](https://polar-escarpment-7201.herokuapp.com/questionnaire/566455a69c390da81276246f)

## 部分截图

- 问卷页面

![问卷页面](https://raw.githubusercontent.com/LiangCY/questionnaire/master/screenshots/index.jpg)

- 统计结果

![统计结果](https://raw.githubusercontent.com/LiangCY/questionnaire/master/screenshots/statistics.jpg)


### 后台管理

- 题库

![题库](https://raw.githubusercontent.com/LiangCY/questionnaire/master/screenshots/questions.jpg)

- 编辑题目

![编辑题目](https://raw.githubusercontent.com/LiangCY/questionnaire/master/screenshots/question.jpg)

- 添加问卷

![添加问卷](https://raw.githubusercontent.com/LiangCY/questionnaire/master/screenshots/questionnaire.jpg)