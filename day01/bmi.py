can_nang = float(input("Nhap can nang (kg): "))
chieu_cao = float(input("Nhap chieu cao(m): "))
bmi = can_nang/ chieu_cao**2
print (f"BMI cua ban la: {bmi:.2f}")
if bmi<18.5:
    print ("Gay")
elif bmi >=18.5 and bmi<25:
    print ("Binh thuong")
else:
    print ("Thua can")

