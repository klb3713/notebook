import os
import re
import time

root_dir = os.path.dirname(__file__)
root_dir = os.path.abspath(root_dir)

def getNewArticles():
    filenames = []
    print root_dir
    file_type = "rst"

    list_dirs = os.walk(root_dir)
    rr = re.compile( "\.%s$" %file_type , re.I )
    for root, dirs, files in list_dirs:
        for f in files:            
            if rr.search(f) and not f.startswith("index"):
                path = os.path.join(root,f)
                info = os.stat(path)
                filenames.append([path[len(root_dir)+1:], info.st_ctime])
    
    filenames.sort(key=lambda x:x[1])
    return [item[0] for item in filenames]

def writeArticle(filenames):
    index_file = open(os.path.join(root_dir, "index.rst"), 'r')
    #index = index_file.readlines()
    index = "".join(index_file.readlines())
    index_file.close()

    strs = re.split(r'news.+news', index)
    news = "\n.. toctree::\n   :maxdepth: 1\n\n"
    for article in filenames:
        news += "   "+article+'\n'
    index = strs[0]+'.. news\n'+news+'\n.. news'+strs[-1]
    print index
    index_file = open(os.path.join(root_dir, "index.rst"), 'w')
    #index_file.write(index)
    index_file.close()

if __name__ == '__main__':
     news = getNewArticles() 
     print news
     #writeArticle(news)
