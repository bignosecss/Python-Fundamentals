read_f = open("../bill.txt", "r", encoding="UTF-8")

write_f = open("../bill.txt.bak", "w", encoding="UTF-8")

for line in read_f:
    if "测试" in line:
        continue
    else:
        write_f.write(line)

read_f.close()
write_f.close()
