class Calcul:
    OPERATORS = {'+': (1, lambda x, y: x + y), '-': (1, lambda x, y: x - y),
                '*': (2, lambda x, y: x * y), '/': (2, lambda x, y: x / y),
                '%': (2, lambda x, y: x % y)
                }
    
    @staticmethod
    def parse(line):
        num = ''
        for i in line:
            if i in '1234567890.':
                num += i
            elif num:
                yield float(num) #генератор
                num = ''
            if i in Calcul.OPERATORS or i in '()':
                yield i #кортеж из приоритета + функции
        if num:
            yield float(num)
    
    @staticmethod
    def sort(parsed):
        tmp = []
        for i in parsed:
            if i in Calcul.OPERATORS:
                while tmp and tmp[-1] != '(' and Calcul.OPERATORS[i][0] <= Calcul.OPERATORS[tmp[-1]][0]:
                    yield tmp.pop()
                tmp.append(i)
            elif i == ')':
                while tmp:
                    x = tmp.pop()
                    if x == '(':
                        break
                    yield x
            elif i == '(':
                tmp.append(i)
            else:
                yield i
        while tmp:
            yield tmp.pop()
    
    @staticmethod
    def calc(sort):
        tmp = []
        for i in sort:
            if i in Calcul.OPERATORS:
                y = tmp.pop()
                x = tmp.pop()
                tmp.append(Calcul.OPERATORS[i][1](x, y))
            else:
                tmp.append(i)
        return tmp[0]
    
    @staticmethod
    def calc_vivod(exp):
        return Calcul.calc(Calcul.sort(Calcul.parse(exp)))

# while True:
#     gen = list(Calcul.parse(input()))
#     print(gen)



if __name__ == '__main__':
    inp = input('Calculate: ')
    calc = Calcul()
    print(calc.calc_vivod(inp))

# gen = calc.parse(inp)
# for i in gen:
#     print(i)
