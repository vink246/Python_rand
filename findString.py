def count_substring(string, sub_string):
    length = len(sub_string)
    count = 0
    for i in range(0,len(string)-length+1):
        if i+length == len(string):
            check = string[i:]
        else:
            check = string[i:i+length]
        if check == sub_string:
            count += 1
    return count

x = count_substring('hellollo','llo')
print(x)
