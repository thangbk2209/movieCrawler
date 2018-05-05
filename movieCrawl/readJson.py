import json
from pprint import pprint
movieType = ['phim_co_trang','phim_hai',
'phim_hanh_dong','phim_kinh_di','phim_phieu_luu','phim_tai_lieu',
'phim_tam_ly','phim_tinh_cam','phim_vien_tuong']
data = {}
data['movie'] = [] 
for movie in movieType:
    file_name = movie+'.json'
    with open(file_name) as f:
        phim = json.load(f)
    
    for i in range(len(phim)):
        print 'i',i
        print type(phim[i]['title'])
        print phim[i]['title']
        data['movie'].append({
            'category': movie,
            'linkPhim':phim[i]['linkMovie'],
            'linkBackgrounds': phim[i]['linkBackground'],
            'title':phim[i]['title'],
            'engTitle': phim[i]['engTitle']
        })
print len(data['movie'])
with open('data/data.json', 'w') as outfile:  
    json.dump(data, outfile)
 