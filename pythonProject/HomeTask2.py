minutes = int(input("Input minutes: "))

days = minutes // (24 * 60)
hours = (minutes % (24 * 60)) // 60
minutes = minutes % 60

print((days, hours, minutes))

