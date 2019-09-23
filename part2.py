2. Find the number of duplicate words and words that are unique. 

fin=open(r'C:\Users\student\Desktop\book.txt')
l=dict()
d=dict()

def count_unique_words():
    for i in fin:
        word=i.strip()
        l=word.split(" ")
        for k in l:
            if k not in d:
                d[k] = 1
            else:
                 d[k] = d[k] + 1
    return len(d)
  
def words_that_appear_once():
    for i in fin:
        word=i.strip()
        b=word.split(" ")
        for k in b:
            if k not in l:
                l[k] = 1
    return len(l)

def count_word():
    fin = open(r"C:\Users\student\Desktop\book.txt")
    count=0
    for i in fin:
        word=i.strip()
        l=word.split(" ")
        for k in l:
            count=count+1
    return count

print("Total unique words ",count_unique_words())
print("Total number of duplicate words ",count_word()-words_that_appear_once())
