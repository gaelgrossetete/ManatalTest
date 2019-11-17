'''Exercise 3: Algorithmic Test'''

separator=''
equi_dict={'integer': [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1], 'roman' :['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']}


def integer_to_roman(n):
    output=[]
    while n>0:
        if n>=4000:
            return('number too high')
        for i in range(len(equi_dict['integer'])):
            m = n//equi_dict['integer'][i]
            if 0<m<4:
                output.append(m*equi_dict['roman'][i])
            n-=m*equi_dict['integer'][i]
    return separator.join(output)

print(integer_to_roman(1235))
