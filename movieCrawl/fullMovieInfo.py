import json
from pprint import pprint
import sys
reload(sys)
sys.setdefaultencoding('utf8')
data = []

file_name1 = 'data/data.json'
file_name2 = 'movieInfo.json'
with open(file_name1) as f:
    movie = json.load(f)
with open(file_name2) as f:
    movieInfo = json.load(f)
print movie['movie'][0]
print movieInfo[0]
for i in range(len(movie['movie'])):
    print 'movie ', i
    for j in range(len(movieInfo)):
        print 'movieInfo ', j
        if(movie['movie'][i]['title'] == movieInfo[j]['title']):
            print 'movie ', i, '=== movieInfo ', j
            print type(movie['movie'][i]['title'])
            print movieInfo[j]['title']
            data.append({
                'category': movie['movie'][i]['category'],
                'linkPhim':movie['movie'][i]['linkPhim'],
                'linkBackgrounds': movie['movie'][i]['linkBackgrounds'],
                'title':movie['movie'][i]['title'].encode('utf8', 'ignore'),
                'engTitle': movie['movie'][i]['engTitle'],
                'linkWatch': movieInfo[j]['linkWatch'],
                'country': movieInfo[j]['country'],
                'imdb': movieInfo[j]['imdb'],
                'year': movieInfo[j]['year']
            })
            break
print len(data)
with open('data/fullMovieInfo.json', 'w') as outfile:  
    json.dump(data, outfile)
# for i in range(len(phim)):
#     print 'i',i
#     print type(phim[i]['title'])
#     print phim[i]['title']
#     data['movie'].append({
#         'category': movie,
#         'linkPhim':phim[i]['linkMovie'],
#         'linkBackgrounds': phim[i]['linkBackground'],
#         'title':phim[i]['title'],
#         'engTitle': phim[i]['engTitle']
#     })
# print len(data['movie'])
# with open('data/data.json', 'w') as outfile:  
#     json.dump(data, outfile)
 