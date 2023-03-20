<h1> Python - Object-relational mapping</h1>
<img src="https://miro.medium.com/v2/resize:fit:1200/0*UkOqM_a_agYwUOoV">
<p>Object-relational mapping (ORM) is a technique that allows developers to interact with a relational database using object-oriented programming (OOP) concepts. Python has several popular ORM frameworks, including:

</p>
<ol>
  <li>Django ORM: This is the built-in ORM that comes with the Django web framework. It provides a high-level interface for interacting with a database, making it easy to create, read, update, and delete records.</li>
  <li>SQLAlchemy: This is a popular ORM that can be used with a variety of databases, including MySQL, PostgreSQL, SQLite, and Oracle. SQLAlchemy provides a lot of flexibility and advanced features, such as support for complex queries and transactions.</li>
  <li>Peewee: This is a lightweight ORM that is easy to use and supports several databases, including MySQL, PostgreSQL, and SQLite. Peewee has a simple syntax and provides a lot of convenience methods for common database operations.</li>
</ol>
<p>With an ORM, you can define database tables as Python classes, and each instance of the class represents a row in the table. You can then interact with the database by creating, modifying, and deleting instances of the classes. The ORM handles the translation between the Python objects and the database tables, so you don't have to write raw SQL queries.</p>
For example, here's a simple Django model that defines a database table for storing blog posts:

python
Copy code
from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
This model defines a table with three columns: title, content, and pub_date. You can create a new blog post by instantiating the BlogPost class and saving it to the database:

python
Copy code
post = BlogPost(title='My First Post', content='Hello, world!')
post.save()
You can retrieve all blog posts with the following code:

python
Copy code
posts = BlogPost.objects.all()
for post in posts:
    print(post.title)
ORMs can make it easier to work with databases in Python, but they can also add complexity to your code. It's important to choose an ORM that fits your project's needs and to understand its strengths and limitations.
