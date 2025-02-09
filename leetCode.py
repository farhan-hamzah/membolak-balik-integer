nums = int(input())
hasil = 0 
hasil2 = 0
akhir1 = nums
while nums > 0:
    i = nums%10
    hasil = (hasil*10) + i
    nums = nums//10
while hasil > 0:
    p = hasil%10
    hasil2 = (hasil2*10) + p
    hasil = hasil//10
if akhir1 == hasil2:
    print(True)
else:
    print(False)

