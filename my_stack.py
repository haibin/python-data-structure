class Stack:
    def __init__(self):
        self.array = list()

    def push(self, val):
        self.array.append(val)

    def pop(self):
        if len(self.array) == 0:
            return None

        return self.array.pop()

    def __len__(self):
        return len(self.array)



def is_valid(s):
    """ Returns boolean
    """
    stack = Stack()
    for x in s:
        if x in ['(', '[', '{']:
            stack.push(x)
            continue
        if x in [')', ']', '}']:
            val = stack.pop()
            if val is None:
                return False
            if val == '(' and x != ')':
                return False
            if val == '[' and x != ']':
                return False
            if val == '{' and x != '}':
                return False
            continue
    # check the stack
    if len(stack) == 0:
        return True
    return False

s = '( var x = { y: [1, 2, 3] } )'

print(is_valid(s))

s = '( var x = { y: [1, 2, 3] ) }'

print(is_valid(s))

s = '( var x = { y: [1, 2, 3] }'

print(is_valid(s))
