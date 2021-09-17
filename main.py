from stack import Stack


def is_balanced(brackets):
    brackets_s = Stack()

    brackets_dict = {')': '(',
                     '}': '{',
                     ']': '['
                     }

    for bracket in brackets:
        if bracket in brackets_dict.values():
            brackets_s.push(bracket)
        elif bracket in brackets_dict.keys():
            if brackets_dict[bracket] == brackets_s.peek():
                brackets_s.pop()
            else:
                brackets_s.push(None)
                break
    return 'Сбалансированно' if brackets_s.is_empty() else 'Несбалансированно'


if __name__ == '__main__':
    test_strings = ['(((([{}]))))', '[([])((([[[]]])))]{()}',
                    '{{[()]}}', '}{}', '{{[(])]}}', '[[{())}]'
                    ]

    for test_str in test_strings:
        print(is_balanced(test_str))
