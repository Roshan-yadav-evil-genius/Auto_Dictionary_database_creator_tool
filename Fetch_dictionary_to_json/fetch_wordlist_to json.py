import time
import json
from bs4 import BeautifulSoup
import requests

dict2a = 'https://www.mso.anu.edu.au/~ralph/OPTED/v003/wb1913_a.html'
dict2b = 'https://www.mso.anu.edu.au/~ralph/OPTED/v003/wb1913_b.html'
dict2c = 'https://www.mso.anu.edu.au/~ralph/OPTED/v003/wb1913_c.html'
dict2d = 'https://www.mso.anu.edu.au/~ralph/OPTED/v003/wb1913_d.html'
dict2e = 'https://www.mso.anu.edu.au/~ralph/OPTED/v003/wb1913_e.html'
dict2f = 'https://www.mso.anu.edu.au/~ralph/OPTED/v003/wb1913_f.html'
dict2g = 'https://www.mso.anu.edu.au/~ralph/OPTED/v003/wb1913_g.html'
dict2h = 'https://www.mso.anu.edu.au/~ralph/OPTED/v003/wb1913_h.html'
dict2i = 'https://www.mso.anu.edu.au/~ralph/OPTED/v003/wb1913_i.html'
dict2j = 'https://www.mso.anu.edu.au/~ralph/OPTED/v003/wb1913_j.html'
dict2k = 'https://www.mso.anu.edu.au/~ralph/OPTED/v003/wb1913_k.html'
dict2l = 'https://www.mso.anu.edu.au/~ralph/OPTED/v003/wb1913_l.html'
dict2m = 'https://www.mso.anu.edu.au/~ralph/OPTED/v003/wb1913_m.html'
dict2n = 'https://www.mso.anu.edu.au/~ralph/OPTED/v003/wb1913_n.html'
dict2o = 'https://www.mso.anu.edu.au/~ralph/OPTED/v003/wb1913_o.html'
dict2p = 'https://www.mso.anu.edu.au/~ralph/OPTED/v003/wb1913_p.html'
dict2q = 'https://www.mso.anu.edu.au/~ralph/OPTED/v003/wb1913_q.html'
dict2r = 'https://www.mso.anu.edu.au/~ralph/OPTED/v003/wb1913_r.html'
dict2s = 'https://www.mso.anu.edu.au/~ralph/OPTED/v003/wb1913_s.html'
dict2t = 'https://www.mso.anu.edu.au/~ralph/OPTED/v003/wb1913_t.html'
dict2u = 'https://www.mso.anu.edu.au/~ralph/OPTED/v003/wb1913_u.html'
dict2v = 'https://www.mso.anu.edu.au/~ralph/OPTED/v003/wb1913_v.html'
dict2w = 'https://www.mso.anu.edu.au/~ralph/OPTED/v003/wb1913_w.html'
dict2x = 'https://www.mso.anu.edu.au/~ralph/OPTED/v003/wb1913_x.html'
dict2y = 'https://www.mso.anu.edu.au/~ralph/OPTED/v003/wb1913_y.html'
dict2z = 'https://www.mso.anu.edu.au/~ralph/OPTED/v003/wb1913_z.html'

dict1 = [dict2a, dict2b, dict2c, dict2d, dict2e,
         dict2f, dict2g, dict2h, dict2i, dict2j, dict2k, dict2l, dict2m, dict2n, dict2o, dict2p, dict2q, dict2r, dict2s, dict2t, dict2u, dict2v, dict2w, dict2x, dict2y, dict2z]


def removt(soup):
    soup = f"{soup}"

    def strtobs4(data):
        soup = BeautifulSoup(data, 'html.parser')
        return soup
    soup = strtobs4(soup)
    list = [tag.name for tag in soup.findAll()]
    string = f"{soup.find(list[0])}"
    list.remove(list[0])
    for data in list:
        bind = f"{soup.find(data)}"
        lenbin = len(bind)
        pos = string.find(bind)
        string = string[:pos]+string[pos+lenbin:]
        soup = strtobs4(string)
    return soup


Word_list = []
for url in dict1:
    print(url)
    data = requests.get(url).content
    soup = BeautifulSoup(data, 'html.parser')
    listdict = soup.find('body').contents
    print(len(listdict))
    for x in range(len(listdict)):
        if len(listdict[x]) > 1:
            new_word = {}
            data = listdict[x]
            key = data.find('b')
            list = f"{removt(data).text}"
            new_word["key"] = f"{key.text}"
            new_word["defination"] = f"{list.strip(' ').strip('()').strip(' ')}"
            Word_list.append(new_word)

# generate a text file for create dictionary in future

with open('Dictionary.json', 'w') as file:
    file.write(json.dumps(Word_list))
