def ips_between(start, end):
    start_num = start.split('.')
    end_num = end.split('.')
    return sum((int(end_num[i]) - int(start_num[i])) * 256**(3-i) for i in range(4))


print(ips_between("10.0.0.0", "10.0.0.50"))  # 50
print(ips_between("20.0.0.10", "20.0.1.0"))  # 246