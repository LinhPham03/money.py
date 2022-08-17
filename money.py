USD = int(input("Nhập số tiền đôla: "))
ti_gia = int(input ("Nhập tỉ giá USD/VND: "))
VND = USD*ti_gia
print("{USD} USD quy đổi thành {VND} VND".format (USD=USD, VND=VND))
