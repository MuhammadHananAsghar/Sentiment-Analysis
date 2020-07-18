
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

def strip_punctuation(para):
    for i in punctuation_chars:
        para = para.replace(i,'')
    return para
    
    
    
def get_pos(param):
    num = 0
    param = param.split(" ")
    param = [strip_punctuation(i) for i in param]
    for i in param:
        if i.lower() in positive_words:
            num += 1
    return num
    
    
    
def get_neg(param):
    num = 0
    param = param.split(" ")
    param = [strip_punctuation(i) for i in param]
    for i in param:
        if i.lower() in negative_words:
            num += 1
    return num



punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


def strip_punctuation(para):
    for i in punctuation_chars:
        para = para.replace(i,'')
    return para
def get_pos(param):
    num = 0
    param = param.split(" ")
    param = [strip_punctuation(i) for i in param]
    for i in param:
        if i.lower() in positive_words:
            num += 1
    return num

def get_neg(param):
    num = 0
    param = param.split(" ")
    param = [strip_punctuation(i) for i in param]
    for i in param:
        if i.lower() in negative_words:
            num += 1
    return num
fh = open('project_twitter_data.csv','r')
fh2 = open('resulting_data.csv','w')
for i in fh.readlines():
    i = i.split(',')
    fh2.write("{},{},{},{}".format(i[1],i[2],))
    
