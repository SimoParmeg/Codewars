def break_camelCase(s):
    ## PRIMA SOLUZIONE
    # for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    #     newchar = ' '+char
    #     s = s.replace(char, newchar)
    # return s

    ## SECONDA SOLUZIONE
    return ''.join(' ' + char if char.isupper() else char for char in s)

print(break_camelCase("helloWorld"))
print(break_camelCase("camelCase"))
print(break_camelCase("breakCamelCase"))
