# 导入模块
import pymysql
# 导入数据库密码
from conf.db_connect import *

# 连接数据库
# PyMySQL 模块提供了四个连接数据库的函数名，其本质是多个变量的函数引用横等赋值，最终还是执行一个函数。
# 官方代码：Connect = connect = Connection = connections.Connection
# 按代码的赋值顺序，推荐使用 Connect 方式连接，其它函数使用方式相同。
# 连接数据库函数格式及主要参数如下：
# Connect(host, port, user, password, database, charset)
# host：数据库主机的地址，默认为 localhost。
# port：数据库的端口号，默认为 3306。
# user：连接数据库所用的用户名。
# password：连接数据库所用的密码。
# database：要连接的数据库的名称。
# charset：连接数据库时使用的字符集，默认为 utf8。
db_connect = pymysql.Connect(host=DBHOST, port=DBPORT, user=DBUSER, password=DBPASSWORD, database=DBNAME, charset="utf8")
print(db_connect)
# <pymysql.connections.Connection object at 0x102dc0ad0>

# 断开数据库连接，避免资源泄露
# db_connect.close()

# 数据库连接对象创建成功后，还需要创建游标对象
# 游标对象的作用是用来执行数据库操作，在执行完一次操作后，应调用 close() 方法将游标对象关闭
# 在进行数据库操作时，每次数据库操作都应该建立一个游标对象，在操作完毕后将其关闭，不应使用一个游标对象进行多次操作
# PyMySQL 模块使用 数据库连接对象.cursor() 方法获取游标对象
cursor = db_connect.cursor()
print(cursor)
# <pymysql.cursors.Cursor object at 0x100bdcbf0>
# 关闭游标对象
cursor.close()

# 执行sql操作
# PyMySQL 模块使用 execute() 方法执行 SQL 语句，实现数据库操作
# 游标对象.execute(query, args=None)
# query：需要执行的 SQL 语句；args：为 SQL 语句中的占位符提供参数，防止 SQL 注入的发生
cursor = db_connect.cursor()
cursor.execute("select * from department")


# 查询操作：查询单条记录
# 使用 execute 执行完毕 SQL 语句后，可以使用 游标对象.fetchone() 方法获取一条查询结果
# fetchone() 方法可重复使用，程序会继续向后读取查询结果。如果无查询结果可读取，则返回 None
print(cursor.fetchone()) # (1, '研发部', '张无忌', '北京')
print(cursor.fetchone()) # (2, '运营部', '赵敏', '深圳')
print(cursor.fetchone()) # (3, '销售部', '周芷若', '成都')
print(cursor.fetchone()) # (4, '人力资源部', '王五', '上海')
print(cursor.fetchone()) # None
cursor.close()


# 查询操作：查询多条记录
# 可以使用 游标对象.fetchall() 方法获取全部查询结果
cursor = db_connect.cursor()
cursor.execute("select * from department")
print(cursor.fetchall())
# ((1, '研发部', '张无忌', '北京'), (2, '运营部', '赵敏', '深圳'), (3, '销售部', '周芷若', '成都'), (4, '人力资源部', '王五', '上海'))
cursor.close()


# 查询操作：查询指定条数记录
# 可以使用 游标对象.fetchmany(size) 方法获取指定数量查询结果
cursor = db_connect.cursor()
cursor.execute("select * from department;")
# fetchmany() 获取的查询结果也是和文件指针一样，获取了结果后指针就向后移动到相应位置，下一次再使用fetchmany就从指针的位置开始获取，而不是每次都从头开始获取
print(cursor.fetchmany(1))
# ((1, '研发部', '张无忌', '北京'),)
print(cursor.fetchmany(3))
# 从指针开始的位置向后获取查询结果
# ((2, '运营部', '赵敏', '深圳'), (3, '销售部', '周芷若', '成都'), (4, '人力资源部', '王五', '上海'))
print(cursor.fetchmany(4))
# ()
cursor.close()


# 插入操作
# 执行插入操作同样使用 execute() 方法，插入数据时的 SQL 语句中的新数据，可以使用传参的方式填入
# 参数可以使用 元组 或 列表 形式传入
# 在插入数据操作完成后，需要对所做的更改操作进行提交，提交操作使用 数据库连接对象.commit() 方法
cursor = db_connect.cursor()
values = [(5, '部门A', 'NameA', '城市A'), (6, '部门B', 'NameB', '城市B')]
result = cursor.execute(f"insert into department values {values[0]}, {values[1]};")
print(result) # 2 -- 表示 2 rows 数据被插入（被影响）
db_connect.commit()
cursor.close()


# 更新操作
# 更新操作同插入操作，只是 SQL 语句不同，操作完毕后，需要执行提交操作
cursor = db_connect.cursor()
result = cursor.execute("update department set dept_name = '部门C' where dept_id = 5;")
print(result) # 1 --- 表示 1 row 数据被更新（被影响）
db_connect.commit()
cursor.close()


# 删除操作
# 删除操作同插入操作和更新操作，只是 SQL 语句不同，操作完毕后，需要执行提交操作
cursor = db_connect.cursor()
result = cursor.execute("delete from department where dept_id = 6;")
print(result) # 1 --- 表示 1 row 数据被删除（被影响）
db_connect.commit()
cursor.close()

# 最后记得关闭数据库连接
db_connect.close()