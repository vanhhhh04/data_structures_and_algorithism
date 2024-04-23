# Bài 1: Đổi tiền
# Bài toán: Cho 5 loại tiền mệnh giá 10000 đồng, 5000 đồng, 2000 đồng, 1000 đồng
# và 500 đồng với số lượng tờ tiền của mỗi loại không hạn chế. Cho trước một số tiền
# m. Hỏi cần lấy ít nhất bao nhiêu tờ tiền trong 5 loại mệnh giá trên để được số tiền
# m?
# - Mô tả phương án giải quyết bài toán theo chiến lược tham lam.
# - Thiết kế giải thuật theo chiến lược tham lam.
# - Cài đặt chương trình ứng dụng.
def doitien(n):
    soluong = 0
    tien = [5000,2000,1000,500]
    for i in tien :
        if n >= i :
            soluong += n // i
            n %= i
    return soluong
n = 210
print(doitien(n))
