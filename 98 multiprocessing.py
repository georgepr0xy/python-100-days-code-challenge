import multiprocessing
import requests



def downloadFile(url,name):
    print(f"start download {name}")
    r = requests.get(url)
    open(F'files/photo{name}.jpg', 'wb').write(r.content)
    print(f"finished downloading {name}")
    


if __name__=="__main__":

 url="https://picsum.photos/2000/3000"
 pros=[]
 for i in range(50):
    # downloadFile(url,i)
    p = multiprocessing.Process(target=downloadFile, args=[url,i])
    p.start()
    pros.append(p)

 for p in pros:
    p.join()    