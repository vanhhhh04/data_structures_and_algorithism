# Bài 2: Xếp ba lô
# Một chiếc ba lô có thể chứa được các đồ vật với tổng khối lượng tối đa là w. Có n
# đồ vật ký hiệu v1, ..., vn, mỗi đồ vật vi (i = 1, ..., n) có khối lượng là mi và giá trị là
# ci. Hãy xếp các đồ vật vào ba lô sao cho giá trị đạt được là lớn nhất.
# Yêu cầu:
# - Mô tả quá trình xếp các đồ vật vào ba lô theo chiến lược tham lam.
# - Thiết kế giải thuật giải quyết bài toán theo chiến lược tham lam.
# - Cài đặt chương trình ứng dụng.
# Hướng dẫn
# - Sắp xếp danh sách các đồ vật giảm dần theo tỷ lệ giá trị / khối lượng;
# - Duyệt toàn bộ danh sách đồ vật v[] từ đầu danh sách về cuối.
# - Mỗi đồ vật vi
class dovat:
    def __init__(self, price, weight):
        self.price = price
        self.weight = weight
    def caculate_dongia(self):
        self.dongia = self.price / self.weight
        return self.dongia
dovat1 = dovat(30,15)
dovat2 = dovat(25,10)
dovat3 = dovat(2,2)
dovat4 = dovat(6,4)


def knapsack_greedy(items, capacity):
    ratios = [(item['value'] / item['weight'], item) for item in items]
    ratios.sort(reverse=True, key=lambda x: x[0])  # Sort ratios in descending order

    max_value = 0
    selected_items = []

    for ratio, item in ratios:
        if item['weight'] <= capacity:
            max_value += item['value']
            selected_items.append(item)
            capacity -= item['weight']

    return max_value, selected_items

# Example usage
items = [
    {'weight': 10, 'value': 60},
    {'weight': 20, 'value': 100},
    {'weight': 30, 'value': 120}
]
capacity = 50

max_value, selected_items = knapsack_greedy(items, capacity)
print("Max value achievable:", max_value)
print("Selected items:", selected_items)