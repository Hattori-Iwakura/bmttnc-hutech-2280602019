print("Nhap van ban (Nhap 'done' de ket thuc): ")
lines = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)
    
print("Output: ")
for line in lines:
    print(line.upper())