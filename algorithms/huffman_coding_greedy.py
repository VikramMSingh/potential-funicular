# Creating tree nodes
string = "GDGHSGGGGHSGF"
class NodeTree(object):
    def __init__(self,left=None, right=None):
        self.left = left
        self.right = right 

    def children(self):
        return (self.left, self.right)
    
    def nodes(self):
        return (self.left, self.right)
    
    def __str__(self):
        return '%s_%s' %(self.left, self.right)

# Implement huffman coding 
def huffman_code_tree(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    (l,r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, True, binString + '0'))
    d.update(huffman_code_tree(r, False, binString + '1'))
    return d

# Calculate frequency 
freq = {}
for c in string: 
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1
freq = sorted(freq.items(), key = lambda x:x[1], reverse=True)
nodes = freq 

print(nodes)

while len(nodes) > 1:
    (key1, c1) = nodes[-1]
    (key2, c2) = nodes[-2]
    nodes = nodes[:-2]
    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))

    nodes = sorted(nodes, key=lambda x:x[1], reverse=True)

huffmanCode = huffman_code_tree(nodes[0][0])

print(' Char | Huffman code ')
print('-----------------------')
huffman_bit = 0 
chars_byte = 0
huff_code_bit = 0
for (char, frequency) in freq:
    print(' %-4r |%12s ' % (char, huffmanCode[char]))
    huffman_bit += frequency * len(huffmanCode[char])
    chars_byte += 8
    huff_code_bit += len(huffmanCode[char])

    

original_bytes = len(string) * 8 
huffman_size = huff_code_bit + huffman_bit + chars_byte
print(f"Huffman only word : {huffman_bit}")
print(f"Original bytes : {original_bytes}")
print(f"Huffman: {huffman_size}")