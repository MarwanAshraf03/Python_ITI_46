from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Book(models.Model):
    desc = models.CharField(max_length=1000)
    title = models.CharField(max_length=50)
    rate = models.FloatField(validators=[MaxValueValidator(5), MinValueValidator(0)])
    views = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return self.title
    # __books = [{
    #     "id": 1,
    #     "title": "hello world",
    #     "description": "this is a book to say hello world",
    #     "price": 3.5
    # }]
    # __last_id = 2
    # @classmethod
    # def all(cls):
    #     return cls.__books.copy()
    
    # @classmethod
    # def one(cls, id):
    #     index = cls.__getIndex(id)
    #     if index is not None:
    #         return cls.__books[index]
    #     return None
    #     # raise http404
    
    # @classmethod
    # def create(cls, title, description, price):
    #     book = {
    #         "id": cls.__last_id,
    #         "title": title,
    #         "description": description,
    #         "price": price
    #     }
    #     cls.__books.append(book)
    #     cls.__last_id += 1
    #     return book
    
    # @classmethod
    # def update(cls, id, title, description, price):
    #     index = cls.__getIndex(id)
    #     book = None
    #     if index is not None:
    #         cls.__books[index]['title'] = title
    #         cls.__books[index]['description'] = description
    #         cls.__books[index]['price'] = price
    #         book = cls.__books[index]
    #     return book
    
    # @classmethod
    # def destroy(cls, id):
    #     index = cls.__getIndex(id)
    #     book = None
    #     if index is not None:
    #         book = cls.__books[index]
    #         del cls.__books[index]
    #     return book
    
    # @classmethod
    # def __getIndex(cls, id):
    #     return next((i for i in range(len(cls.__books)) if cls.__books[i]['id'] == id), None)
    # def __str__(self):
    #     return super().__str__()
