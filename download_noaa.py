import os

def download(url):
    os.system("wget " + url)

def rm(name):
    print("------>","rm " + name)
    os.system("rm " + name)

def parse_file(name):
    subfiles = []
    if name.split('.')[-1] in ['pdf', 'csv']:
        return []
        
    try:
        file = open(name, 'r')
    except:
        name = 'index.html'
        file = open('index.html', 'r')

    key = '<tr><td><a href="'
    for line in file.readlines():
        line = line.strip()
        if line[:len(key)] == key:
            line = line[len(key):]
            line = line.split('"')[0]
            subfiles.append(line)
    file.close()
    rm(name)
    return subfiles

def download_sub_pages(main_url):
    download(main_url)
    name = main_url.split('/')[-1]
    subfiles = parse_file(name)
    
    if len(subfiles) == 0:
        return

    subfiles = [x for x in subfiles if x[0]!='/']
    for subfile in subfiles:
        download_sub_pages(main_url + '/' + subfile)

main_url = "https://www.ngdc.noaa.gov/stp/space-weather"
download_sub_pages(main_url)
