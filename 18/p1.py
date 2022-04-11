PATH = "day18/data.txt"

def calculate(expr):
    #find top level bracket expressions and call recursively
        #iterate over space split list
    for pos in range(len(expr)):
        char = expr[pos]
        if not char is None:
            if char[0] == "(":
                level = 0
                end = 0
                finished = False
                index = 0
                while not finished:
                    unit = expr[pos:][index]
                    for op in unit:
                        if op == "(":
                            level += 1
                        elif op == ")":
                            level -= 1
                        if level == 0:
                            end = index + pos
                            finished = True
                    index += 1
                
                subexpr = expr[pos:end + 1]
                subexpr[0] = subexpr[0][1:]; subexpr[-1] = subexpr[-1][:-1]

                expr[pos] = str(calculate(subexpr))
                for scan in range(pos + 1, end + 1):
                    expr[scan] = None
    expr = list(filter(lambda x : not x is None, expr))
    #at this point list which is all single numbers and operators
    #pair operators and numbers skipping first item
    op = ""
    for i in range(1, len(expr)):
        if i % 2 == 1:
            op = expr[i]
            expr[i] = None
        else:
            expr[i] = [op, int(expr[i])]
        i += 1
    expr = list(filter(lambda x : not x is None, expr))
    
    res = int(expr[0])        
    #eval left to right
    for i in range(1, len(expr)):
        if expr[i][0] == "+":
            res += expr[i][1]
        else:
            res *= expr[i][1]
    
    return res
    #return result

input = [x[:-1] for x in open(PATH).readlines()]

answers = []

for line in input:
    answers.append(calculate(line.split(" ")))

print(sum(answers))
