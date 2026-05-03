# (first (list 1 (+ 2 3) 9))
# ["first", ["list", 1, ["+", 2, 3], 9]]
# (define (factorial n) (if (= n 0) 1 (* n (factorial (- n 1)))))
# ['define', ['factorial', 'n'], ['if', ['=', 'n', '0'], '1', ['*', 'n', ['factorial', ['-', 'n', '1']]]]]



def main():
    print(parse_call("['define', ['factorial', 'n'], ['if', ['=', 'n', '0'], '1', ['*', 'n', ['factorial', ['-', 'n', '1']]]]]"))
    

def parse_call(inp):
    res = []
    inp = inp[1:-1]
    op, *operands = inp.split(" ")
    operands = " ".join(operands)
    res.append(op)
    res.extend(split_operands(operands))
    return res
    

def split_operands(operand):
    operands = []
    i = 0
    stack = 0
    while i < len(operand):
        char = operand[i]
        curr = ""
        if char == "(":
            stack = 1
            curr += char
            while stack != 0:
                i+=1
                char = operand[i]
                curr += char
                if char == ")":
                    stack -= 1
                    if stack == 0: break
                if char == "(":
                    stack += 1
            operands.append(parse_call(curr))        
        elif char != " ":
            curr += char
            while i + 1 < len(operand) and operand[i+1] != " " :
                i += 1
                char = operand[i]
                curr += char
            operands.append(curr) 
        i+=1
    return operands
                  
                
   

if __name__ == "__main__":
    main()