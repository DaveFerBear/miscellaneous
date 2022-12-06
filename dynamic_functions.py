'''

This file implement dynamic formulas.

'''


class Node(object):
    def __init__(self, function=None):
        self.function = function
        self.children = []

    def __str__(self) -> str:
        return 'Node {} has children {}'.format(self.function, [c.__str__() for c in self.children])


def is_int(s):
    try:
        int(s)
        return True
    except TypeError:
        return False
    except ValueError:
        return False

# Converts 'A(B(1), C(2))' -> 'A', ['B(1)', 'C(2)']
# or 'A(B(C))' -> 'A', ['B(C)']


def parse_input_str(s: str):
    func_name = s[:s.index('(')]
    inner_args = s[len(func_name)+1:-1]
    if not inner_args:
        return func_name, []

    inner_args = list(map(str.strip, inner_args.split(',')))
    return func_name, inner_args


'''
Converts 'A(B(1), C(2))' into a tree like:
     A
  B     C
  1     2
'''


def build_graph(s: str) -> Node or int:
    if is_int(s):  # Base Case
        return int(s)

    function, args = parse_input_str(s)
    node = Node(function)
    children = []
    for arg in args:
        children.append(build_graph(arg))
    node.children = children
    return node


def compute_graph(root: Node or int, fmap: map) -> int:
    if is_int(root):
        return root

    computed_children = []
    for c in root.children:
        cc = compute_graph(c, fmap)
        computed_children.append(cc)

    print('Running Function: {}({})'.format(root.function, *computed_children))
    return fmap[root.function](*computed_children)


input_str = 'A(B(1), C(2))'
input_str_2 = 'A(B(C(D(5)))'

function_map = {
    'A': lambda x, y: int(x+y),
    'B': lambda x: 3*x+1,
    'C': lambda x: x/2
}

print("BUILDING GRAPH")
root = build_graph(input_str)
print(root)

print("COMPUTING GRAPH")
print(compute_graph(root, function_map))
