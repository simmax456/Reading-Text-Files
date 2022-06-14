# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    file = open(filename)
    file_read = file.read()
    line_split = file_read.split()
    return line_split

def count_words():
    text = read_file_content("./story.txt")

    count = dict()

    for word in text:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return print(count)

count_words()