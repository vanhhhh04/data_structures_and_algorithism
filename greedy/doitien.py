# Bài 3: Đổi tiền
# Trong máy ATM có sẵn các loại tiền với mệnh giá khác nhau, giả sử mỗi loại mệnh
# giá có số tờ tiền là vô hạn. Anh An cần rút một khoản tiền m từ cây ATM. Hãy xác
# định số tờ tiền ít nhất mà cây ATM cần trả cho anh An để anh An có được khoản
# tiền m.
# Yêu cầu giải quyết bài toán bằng chiến lược tham lam:
# - Lấy ví dụ và mô tả một phương án giải quyết bài toán.
# - Thiết kế giải thuật theo chiến lược tham lam.
# - Cài đặt chương trình ứng dụng giải thuật.
def doitien(n):
    soluong = 0
    tien = [500,200,100,50,20,10,5,2,1]
    for i in tien :
        if n >= i :
            soluong += n // i
            n %= i
    return soluong
n = 210
print(doitien(n))

