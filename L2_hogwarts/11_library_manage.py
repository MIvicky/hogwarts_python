#【练习】图书管理系统

# 知识点
# 类和对象
# 对象的属性和方法

# 作业要求
# 编写一个Python程序，创建一个图书管理系统，实现以下功能：
# 1. 图书类 Book：属性包括书名（title）、作者（author）和出版日期（publish_date）
# 方法包括获取书名、获取作者和获取出版日期的方法。
# 2. 图书馆类 Library：属性包括图书列表（books）
# 方法包括添加图书、借出图书、归还图书和显示所有图书的方法。
# 3. add_book 方法：接受一个 Book 类型的参数，将其添加到图书列表中。
# 4. borrow_book 方法：接受一个字符串类型的参数（书名），找到对应书名的图书，并将其从图书列表中移除。
# 5. return_book 方法：接受一个 Book 类型的参数，将其添加到图书列表中。
# 6. show_books 方法：输出当前图书馆中所有图书的书名、作者和出版日期。

class Book:
    def __init__(self, title, author, publish_date):
        self.title = title
        self.author = author
        self.publish_date = publish_date

    # 获取书名
    def get_title(self):
        return self.title

    # 获取作者
    def get_author(self):
        return self.author

    # 获取出版日期
    def get_publish_date(self):
        return self.publish_date

class Library:
    def __init__(self):
        self.books = []

    # 添加图书
    def add_book(self, book: Book):
        title = book.get_title()
        author = book.get_author()
        publish_date = book.get_publish_date()
        self.books.append({"title":title, "author":author, "publish_date":publish_date})

    # 借出图书
    def borrow_book(self, title: str):
        for book in self.books:
            if title == book["title"]:
                self.books.remove(book)
                return book

    # 归还图书
    def return_book(self, book: Book):
        self.add_book(book)

    # 显示所有图书
    def show_books(self):
        for book in self.books:
            print(f"书名：{book['title']}, 作者：{book['author']}, 出版日期：{book['publish_date']}")


# 测试
# 创建一个图书馆实例
library = Library()

# 创建几本图书并添加到图书馆中
book1 = Book("Python编程入门", "张三", "2021-01-01")
book2 = Book("Java编程基础", "李四", "2021-02-01")
book3 = Book("C++高级编程", "王五", "2021-03-01")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# 显示所有图书
library.show_books()
# 书名：Python编程入门, 作者：张三, 出版日期：2021-01-01
# 书名：Java编程基础, 作者：李四, 出版日期：2021-02-01
# 书名：C++高级编程, 作者：王五, 出版日期：2021-03-01

# 借出一本图书并打印出借出的书名
borrowed_book = library.borrow_book("Java编程基础")
print(borrowed_book)
# {'title': 'Java编程基础', 'author': '李四', 'publish_date': '2021-02-01'}
if borrowed_book:
    print("借出的书：", borrowed_book["title"])
    # 借出的书： Java编程基础

# 再次显示所有图书
library.show_books()
# 书名：Python编程入门, 作者：张三, 出版日期：2021-01-01
# 书名：C++高级编程, 作者：王五, 出版日期：2021-03-01

# 归还图书并打印出归还的书名
library.return_book(book2)
print("归还书籍：", book2.get_title())
# 归还书籍： Java编程基础

# 最后再次显示所有图书
library.show_books()
# 书名：Python编程入门, 作者：张三, 出版日期：2021-01-01
# 书名：C++高级编程, 作者：王五, 出版日期：2021-03-01
# 书名：Java编程基础, 作者：李四, 出版日期：2021-02-01