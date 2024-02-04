class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        calc_stack = []

        for item in tokens:
            if item not in ["+", "-", "*", "/"]:
                calc_stack.append(item)
            else:
                later = calc_stack.pop()
                former = calc_stack.pop()
                res = self.calc(former, later, item)
                calc_stack.append(str(res))
        
        return int(calc_stack[0])
    
    def calc(self, former, later, item):
        former, later = int(former), int(later)
        if item == '+':
            return former + later
        elif item == '-':
            return former - later
        elif item == '*':
            return former * later
        elif item == '/':
            if former / later < 0:
                return -1 * int(abs(former)/abs(later))
            return former / later

        
