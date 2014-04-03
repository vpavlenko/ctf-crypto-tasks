data = "find_me"
result = ""
magic_list = [313, 547, 89]
magic_summ = 62292
for i in range(0,len(data),2):
    num = int( ''.join([str(ord(k)) for k in data[i:i+2]]))
    if num<magic_summ:
        num += magic_summ
    result += str([num%magic_num for magic_num in magic_list])
print result