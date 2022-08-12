import requests


def prose(article, project='pt.wikipedia.org'):
    url = f'https://xtools.wmflabs.org/api/page/prose/{project}/{article}'
    data = requests.get(url).json()
    page = data['page']
    characters = data['characters']
    words = data['words']
    references = data['references']
    unique_references = data['unique_references']
    return page, characters, words, references, unique_references


def articleinfo(article, project='pt.wikipedia.org'):
    url = f'https://xtools.wmflabs.org/api/page/articleinfo/{project}/{article}'
    data = requests.get(url).json()
    author = data['author']
    print(f'{article}\t{author}')


def top_editors(article, project='pt.wikipedia.org'):
    url = f'https://xtools.wmflabs.org/api/page/top_editors/{project}/{article}?nobots=1'
    data = requests.get(url).json()
    page = data['page']
    editors = data['top_editors']
    print('page\trank\tusername\tcount')
    for payload in editors:
        rank = payload['rank']
        username = payload['username']
        count = payload['count']
        print(f'{page}\t{rank}\t{username}\t{count}')


def count_files_in_category(category):
    url = f"https://petscan.wmflabs.org/?max%5Fage=&page%5Fimage=any&links%5Fto%5Fall=&ns%5B0%5D=1&wpiu=any&sitelinks" \
          f"%5Fno=&namespace%5Fconversion=keep&referrer%5Furl=&outlinks%5Fyes=&wikidata%5Fsource%5Fsites=&output" \
          f"%5Flimit=&ores%5Ftype=any&templates%5Fno=&outlinks%5Fno=&wikidata%5Fitem=no&templates%5Fyes=&langs" \
          f"%5Flabels%5Fno=&project=wikimedia&smaller=&min%5Fsitelink%5Fcount=&before=&labels%5Fno=&show" \
          f"%5Fdisambiguation%5Fpages=both&manual%5Flist=&negcats=&cb%5Flabels%5Fyes%5Fl=1&wikidata%5Flabel" \
          f"%5Flanguage=&depth=20&since%5Frev0=&show%5Fsoft%5Fredirects=both&ores%5Fprediction=any&links%5Fto%5Fno" \
          f"=&larger=&max%5Fsitelink%5Fcount=&common%5Fwiki%5Fother=&show%5Fredirects=both&sparql=&outlinks%5Fany" \
          f"=&output%5Fcompatability=catscan&cb%5Flabels%5Fany%5Fl=1&langs%5Flabels%5Fyes=&search%5Ffilter=&sortorder" \
          f"=ascending&sitelinks%5Fany=&referrer%5Fname=&maxlinks=&pagepile=&edits%5Banons%5D=both&subpage%5Ffilter" \
          f"=either&edits%5Bflagged%5D=both&ores%5Fprob%5Fto=&labels%5Fany=&doit=Do%20it%21&ores%5Fprob%5Ffrom" \
          f"=&search%5Fquery=&format=json&links%5Fto%5Fany=&sortby=none&min%5Fredlink%5Fcount=1&after=&combination" \
          f"=subset&edits%5Bbots%5D=both&search%5Fmax%5Fresults=500&ns%5B6%5D=1&source%5Fcombination=&regexp%5Ffilter" \
          f"=&langs%5Flabels%5Fany=&common%5Fwiki=auto&active%5Ftab=tab%5Foutput&language=commons&templates%5Fany" \
          f"=&sitelinks%5Fyes=&labels%5Fyes=&categories={category}&minlinks=&manual%5Flist%5Fwiki=&search%5Fwiki" \
          f"=&wikidata%5Fprop%5Fitem%5Fuse=&cb%5Flabels%5Fno%5Fl=1&interface%5Flanguage=en "
    data = requests.get(url).json()
    count_files = len(data["*"][0]["a"]["*"])  # array
    values = ''
    for payload in data["*"][0]["a"]["*"]:
        title = payload['title']
        value = f'{category}\t{title}'
        values += value + '\n'
        print(value)

    return values


if __name__ == '__main__':
    with open('input.txt') as file:
        file = file.readlines()
    for line in file:
        line = line.replace('\n', '')
        # top_editors(line, project='commons.wikimedia')
        articleinfo('File:'+line, project='commons.wikimedia')

