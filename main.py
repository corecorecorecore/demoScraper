import re, os, httpx
from fake_useragent import UserAgent


proxfile = 'Source.txt'
file2 = 'all.txt'
prox = list(map(lambda x:x.strip(),open(proxfile)))
pattern = re.compile(r"(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}:\d{2,5})")
ua = UserAgent()
def main():
    if os.path.exists(file2):
        os.remove(file2)
    else:
        pass
    os.system('cls' if os.name == 'nt' else 'clear')
    headers = {'User-Agent':str(ua.chrome)}
    with httpx.Client(http2=True,headers = headers) as client:
        for proxy in range(len(prox)):
                    line_count = 0
                    try:
                        try:                    
                            r = client.get(prox[proxy])
                            for line in pattern.findall(str(r.content)):
                                f = open(file2, "a+")
                                f.write(line+'\n')
                                f.close()
                                if line != "\n":
                                    line_count += 1
                            print(line_count, 'proxies gotten from source',prox[proxy],r)
                            if line_count <= 1:
                                r = client.get(prox[proxy],headers=headers)
                                for line in pattern.findall(r.text):
                                    f = open(file2, "a+")
                                    f.write(line+'\n')
                                    f.close()
                                    if line != "\n":
                                        line_count += 1
                                print(line_count, 'proxies gotten from source',prox[proxy],r)
                        except httpx.HTTPError as exc:
                            print(exc, prox[proxy])
                    except:
                        pass
        file = open(file2, "r")
        mylist = list(map(lambda x:x.strip(),open(file2)))
        mylist = list(set(mylist))
        result = "\n".join(mylist[0:])
        f = open(file2, "w")
        f.write(result)
        f.close()
        line_count = 0
        for line in file:
            if line != "\n":
                line_count += 1
        file.close()
        print(line_count, 'Proxies scraped, duplicates are removed')
                    
if __name__ == '__main__':
    main()
