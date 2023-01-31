class Document:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def show(self):
        return f"Title: {self.title}, Author: {self.author}"

class PDF(Document):
    def __init__(self, title, author, password):
        super().__init__(title, author)
        self.password = password

    def show(self):
        return f"{super().show()}, Password: {self.password}"

class Word(Document):
    def __init__(self, title, author, font_size):
        super().__init__(title, author)
        self.font_size = font_size

    def show(self):
        return f"{super().show()}, Font size: {self.font_size}"

def show_documents(docs):
    for doc in docs:
        print(doc.show())

pdf = PDF("Report", "John Doe", "secret")
word = Word("Resume", "Jane Doe", 12)

docs = [pdf, word]
show_documents(docs)
