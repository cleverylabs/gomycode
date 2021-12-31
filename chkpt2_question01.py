# limites
begin = 2000
end = 3200

list_value = []

for value in range(begin, end+1):
    if (value % 7 == 0) and (value % 5 == 0):
        print(value)
        list_value.append(value)

print(list_value)