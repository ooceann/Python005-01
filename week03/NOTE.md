学习笔记

一些用户的基础设置

```mysql
# 查看当前用户
mysql> use mysql
mysql> select Host,User from user;
+-----------+---------------+
| Host      | User          |
+-----------+---------------+
| %         | root          |
| localhost | mysql.session |
| localhost | mysql.sys     |
+-----------+---------------+
3 rows in set (0.00 sec)


# 创建用户
mysql> CREATE USER 'rose'@'%' IDENTIFIED BY 'Rose1234!';

# 授权testdb（也可以把all换成具体的关键字
mysql> GRANT ALL ON testdb.* TO 'rose'@'%';

# 授权all
# mysql> GRANT ALL ON *.* TO 'rose'@'%';

# 撤销授权rost对testdb的所有权限
mysql> REVOKE ALL ON testdb.* TO 'rose'@'%';

# 更改密码
mysql> SET PASSWORD = PASSWORD('1234');

# 删除用户
mysql> DROP USER 'rose'@'%';



```

