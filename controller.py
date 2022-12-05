from methods import add, sub, div, mult

def parseable_data(data):
    math_equation =[]
    math_elem = []
    for i in data:
        if i.isdigit():
            math_elem.append(i)
        elif (not i.isdigit()) and math_elem:
            math_equation.append(int(''.join(math_elem)))
            math_equation.append(i)
            math_elem = []
        elif (not i.isdigit()) and math_elem:
            math_equation.append(i)
    if math_elem:
        math_equation.append(int(''.join(math_elem)))
    return math_equation

def calculate(part_list):
    result = 0 
    if len(part_list) == 1:
        return part_list[0]
    for s in part_list:
        if s == '*' or s == '/':
            if s == '*':
                index = part_list.index(s)
                result = mult(part_list[index - 1], part_list[index + 1])
                part_list = part_list[:index - 1] + [result] + part_list[index + 2:]
            else:
                index = part_list.index(s)
                result = div(part_list[index - 1], part_list[index + 1])
                part_list = part_list[:index - 1] + [result] + part_list[index + 2:]
    for s in part_list:
        if s == '+' or s == '-':
            if s == '+':
                index = part_list.index(s)
                result = add(part_list[index - 1], part_list[index + 1])
                part_list = part_list[:index - 1] + [result] + part_list[index + 2:]
            else:
                index = part_list.index(s)
                result = sub(part_list[index - 1], part_list[index + 1])
                part_list = part_list[:index - 1] + [result] + part_list[index + 2:]                
    return result

def solution_equation(lst):
    flag = 1
    while flag == 1:
        if ')' in lst:
            for i in range(lst.index(')'), -1, -1):
                if lst[i] == '(':
                    idx = lst.index(')')
                    elem = calculate(lst[i * 1:idx])
                    lst = lst[:i] + [elem] + lst[idx + 1:]
        elif ')' not in lst:
            flag = 0
    return calculate(lst)