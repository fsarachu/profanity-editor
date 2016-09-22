def read_text():
    quotes = open("movie_quotes.txt")
    file_contents = quotes.read()
    print file_contents
    quotes.close()


read_text()
