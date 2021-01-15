def dashatize(num):
    ## PRIMA SOLUZIONE
    # if not num and not (num == 0):
    #     return 'None'
    #
    # numlist = '-'.join(str(abs(num)))
    # result = numlist[:]
    # counter = 0
    #
    # for i, v in enumerate(numlist):
    #     if v == '-':
    #         #  check if the '-' is correct here
    #         if int(numlist[i-1]) % 2 == 0 and int(numlist[i+1]) % 2 == 0:
    #             result = result[:i - counter] + result[i + 1 - counter:]
    #             counter += 1
    # return result

    ## SECONDA SOLUIONE (SMART)
    num_string = str(num)
    for i in ['1', '3', '5', '7', '9']:
        num_string = num_string.replace(i, '-' + i + '-')
    return num_string.strip('-').replace('--', '-')

print(dashatize(274))
print(dashatize(5311))
print(dashatize(86320))
print(dashatize(974302))
print(dashatize(-28369))
