# Viết một chương trình để tạo ngẫu nhiên 3 câu khác nhau có chủ ngữ nằm trong ["Tôi","Bạn", “Cô ấy”],
# động từ nằm trong ["Học","Yêu", “Thích”]
# và tân ngữ là ["Nấu Ăn","Python", “Odoo”].
import random
a = ["Tôi","Bạn", "Cô ấy"]
b = ["Học","Yêu", "Thích"]
c = ["Nấu Ăn","Python", "Odoo"]

a = 'kjhakfhkajhdjaoisdjoiajsoidjejflkjdskfjkdsjfkjhdskjfhkdsjhfkjhdskjhfkjskfdajjkh'
# Viết một chương trình để phân loại và đếm ký tự theo loại 1 chuỗi 100 ký tự ngẫu nhiên,
# trả về dict 1 với các key loại ký tự, value là số ký tự;
# dict 2 thể hiện số lượng tối đa, tối thiểu và trung bình của dict 1
dem_str = 0
dem_int = 0
dict1 = {}
for i in a :
    if isinstance(i,str):
        dem_str += 1
    elif isinstance(i,int) :
        dem_int += 1

dict1['string'] = dem_str
dict1['int'] = dem_int
max = max(dict1.values())
min = min(dict1.values())
avg = max+min / 2
print(dict1)
print(max)
print(min)
print(avg)




