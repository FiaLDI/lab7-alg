def build_huffman_tree(frequencies):
    nodes = [(freq, [(char, "")]) for char, freq in frequencies.items()]
    while len(nodes) > 1:
        nodes.sort(key=lambda x: x[0])
        left = nodes.pop(0)
        right = nodes.pop(0)
        for pair in left[1]:
            pair = (pair[0], '0' + pair[1])
        for pair in right[1]:
            pair = (pair[0], '1' + pair[1])
        merged_node = (left[0] + right[0], left[1] + right[1])
        print(merged_node)
        nodes.append(merged_node)
    print(nodes[0][1])
    return nodes[0][1]

def huffma(frequencies):
    H = [(freq, [0, char]) for char, freq in frequencies.items()]
    print(H)
# Пример использования
frequencies = {'a': 21, 'b': 10, 'c': 5, 'd': 3}
huffman_tree = build_huffman_tree(frequencies)
huffma(frequencies)
# Вывод дерева
for char, code in huffman_tree:
    print(f"Character: {char}, Code: {code}")