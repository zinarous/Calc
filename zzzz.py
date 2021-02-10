class Calcul:
    OPERATORS = {'+': (1, lambda x, y: x + y), '-': (1, lambda x, y: x - y),
                '*': (2, lambda x, y: x * y), '/': (2, lambda x, y: x / y),
                '%': (2, lambda x, y: x % y)
                }
    
    def parse(self, line):
        num = ''
        for i in line:
            if i in '1234567890.':
                num += i
            elif num:
                yield float(num)
                num = ''
            if i in Calcul.OPERATORS or i in '()':
                yield i
        if num:
            yield float(num)
    
    def sort(self, parsed):
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
    
    def calc(self, sort):
        tmp = []
        for i in sort:
            if i in Calcul.OPERATORS:
                y = tmp.pop()
                x = tmp.pop()
                tmp.append(Calcul.OPERATORS[i][1](x, y))
            if i not in Calcul.OPERATORS:
                return 'Неправильно введенное выражение'
            else:
                tmp.append(i)
        return tmp[0]
    
    
    def calc_vivod(self, exp):
        return self.calc(self.sort(self.parse(exp)))


inp = input('Calculate: ')
calc = Calcul()
print(calc.calc_vivod(inp))
