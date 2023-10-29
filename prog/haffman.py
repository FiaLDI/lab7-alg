#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from heapq import heappush, heappop


# Процедура построения дерева
def procedurehuffman(f):
    h = []
    buffer_fs = set() 
    for i in f:
        heappush(h, (f[i], i))
    while len(h) > 1:
        f1, i = heappop(h)
        f2, j = heappop(h)
        fs = f1 + f2
        ord_val = ord('a')
        fl = str(fs)
        while fl in buffer_fs:  
            letter = chr(ord_val)  
            fl = str(fs) + " " + letter
            ord_val += 1  
        buffer_fs.add(fl) 
        f[fl] = {f"{x}": f[x] for x in [i, j]}
        del f[i], f[j]
        heappush(h, (fs, fl))
    return f


# Создание словаря соответствия
def codecreate(tree, codes, path=''):
    for i, (node, child) in enumerate(tree.items()):
        if isinstance(child, int):
            codes[node] = path[1:] + str(abs(i-1))
        else:
            codecreate(child, codes, path + str(abs(i-1)))
    return codes


# Кодирование
def codingHuffman(sentence, dictionary):
    replaced_sentence = ''
    for char in sentence:
        if char in dictionary:
            replaced_sentence += dictionary[char]
        else:
            replaced_sentence += char
    return replaced_sentence


# Декодирование
def decodeHuffman(encoded_text, huffman_tree):
    decoded_text = ""
    key = list(huffman_tree.keys())[0]
    cur = huffman_tree[key]
    for bit in encoded_text:
        for i, (node, child) in enumerate(cur.items()):
            if str(i) != bit:
                if isinstance(child, int):
                    decoded_text += node
                    cur = huffman_tree[key]
                    break
                cur = child
                break
    return decoded_text


if __name__ == "__main__":
    sentence = input("Предложение: ")
    symbs = {}

    # Расчёт частоты символов
    for char in sentence:
        if char in symbs:
            symbs[char] += 1
        else:
            symbs[char] = 1
    for char, count in symbs.items():
        print(f"'{char}': {count} раз")
    
    # Процедура построения дерева
    tree = procedurehuffman(symbs)
    print(f"Дерево: {tree}")
    
    # Создание словаря соответствия
    codes = codecreate(tree, dict())
    print(f"Коды: {codes}")

    # Кодирование
    coding_sentence = str(codingHuffman(sentence, codes))
    print(f"Закодированное предложение:{coding_sentence}")

    # Декодирование
    decoded_text = decodeHuffman(coding_sentence, tree)
    print(f"Раскодированное предложение:{decoded_text}")