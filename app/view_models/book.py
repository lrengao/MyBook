
#处理一本书
class BookViewModel:
    def __init__(self,book):
        self.title = book['title']
        self.publisher = book['publisher']
        self.author = '、'.join(book['author'])
        self.image = book['image']
        self.price = '￥'+book['price']
        self.binding = book['binding']
        self.pubdate = book['pubdate']
        self.isbn = book['isbn']
        self.summary = book['summary']
        self.pages = book['pages']


    #页面的展示裁切
    @property
    def intro(self):
        intros = filter(lambda x:True if x else False,
                        [self.author,self.publisher,self.price])
        return '/'.join(intros)

#处理多本书籍
class BookCollection:
    def __init__(self):
        self.total = 0
        self.keyword = ''
        self.books = []

    def fill(self,yushu_book,keyword):
        self.total = yushu_book.total
        self.keyword = keyword
        self.books = [BookViewModel(book) for book in yushu_book.books]
