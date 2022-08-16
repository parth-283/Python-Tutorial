def searcher():
    import time
    book = ["Ravi","Prayag","Rakesh","Chirag","parth"]
    time.sleep(4)
    while True:
        text = (yield)
        if text in book:
            print("Your text is in the book")
        else:
            print("Text is not in the book")


search = searcher()
print("Running...")
name = input("Enter your name : ")
print("Searching...")
next(search)
search.send(name)
