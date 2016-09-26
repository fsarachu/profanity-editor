import urllib


def read_text():
    quotes = open("movie_quotes.txt")
    file_contents = quotes.read()
    quotes.close()
    return file_contents


def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.purgomalum.com/service/containsprofanity?text=" + text_to_check)
    response = connection.read()
    connection.close()
    print response


check_profanity(read_text())
