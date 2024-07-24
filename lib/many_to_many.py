class Author:
    all = []
    def __init__(self, name):
        self.name = name
        Author.all.append(self)


    def contracts(self):
        return_l = []
        for each in Contract.all:
            if each.author == self:
                return_l.append(each)
        return return_l
    
    def books(self):
        return_l = []
        for each in Contract.all:
            if each.author == self:
                return_l.append(each.book)
        return return_l
    def sign_contract(self, book, date, royalties):
        q = Contract(self, book, date, royalties)
        return q
    
    def total_royalties(self):
        count = 0
        for each in Contract.all:
            if each.author == self:
                count += each.royalties
        return count
    
class Book:
    all = []
    def __init__(self, title):
        self.title = title
        Book.all.append(self)
    def contracts(self):
        list_b = []
        for each in Contract.all:
            if each.book == self:
                list_b.append(each)
        return list_b
    def authors(self):
        list_b = []
        for each in Contract.all:
            if each.book == self:
                list_b.append(each.author)
        return list_b


class Contract:
    all = []
    def __init__(self, author, book, date, royalties):
        if isinstance(author, Author):
            self._author = author
        else: raise Exception("Error")
        if isinstance(book, Book):
            self._book = book
        else: raise Exception("Error")
        if isinstance(date, str):
            self._date = date
        else: raise Exception("Error")
        if isinstance(royalties, int):
            self._royalties = royalties
        else: raise Exception("Error")
        Contract.all.append(self)
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if isinstance(value, Author):
            self._author = value
        else:
            raise Exception("Bepsi")
    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, value):
        if value is Book:
            self._book = value
        else:
            raise TypeError("wrong type")
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, value):
        if value is str:
            self._date = value
        else:
            raise TypeError("wrong type")
        
    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, value):
        if value is int:
            self._royalties = value
        else:
            raise TypeError("wrong type")
        
    def contracts_by_date(date):
        c_list = []
        for each in Contract.all:
            if each.date == date:
                c_list.append(each)
        return c_list