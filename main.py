import re, os, httpx
from fake_headers import Headers


proxfile = 'Source.txt'
file2 = 'all.txt'
prox = list(map(lambda x:x.strip(),open(proxfile)))
pattern = re.compile(r"(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}:\d{2,5})")
count = 0
    
def main():
    os.remove(file2) 
    os.system('cls' if os.name == 'nt' else 'clear')
    headers = Headers(headers=True).generate()
    with httpx.Client(http2=True,headers =headers) as client:
        for proxy in range(len(prox)):
                    try:
                        try:                    
                            r = client.get(prox[proxy],headers=headers)
                            print(prox[proxy],r)
                        except httpx.HTTPError as exc:
                            print(exc)
                    except:
                        pass
                    for line in pattern.findall(r.text):
                        f = open(file2, "a")
                        f.write(line+'\n')
                        f.close()
        file = open(file2, "r")
        mylist = list(map(lambda x:x.strip(),open(file2)))
        mylist = list(dict.fromkeys(mylist))
        line_count = 0
        for line in file:
            if line != "\n":
                line_count += 1
        file.close()
        print(line_count, 'Proxies scraped, duplicates are removed')
                    
if __name__ == '__main__':
    main()
