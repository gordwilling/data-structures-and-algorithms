import sys
from typing import Dict, Tuple

from sortedcontainers import SortedList


class Huffman_Node(object):
    """
    A node in a Huffman Encoding Tree
    """

    def __init__(self, char=None, left=None, right=None, count=None):
        self.char = char
        self.count = count
        self.left = left
        self.right = right

    def is_leaf(self):
        return self.left is None and self.right is None


def _char_count_nodes(data: str) -> SortedList:
    """
    Builds a list of Huffman Nodes, each containing a character and its frequency in the data string

    Args:
        data (str): The string to encode

    Returns:
        a list of Huffman_Nodes sorted in ascending order by frequency
    """
    char_count_map = {}
    for char in data:
        if char in char_count_map:
            char_count_map[char] += 1
        else:
            char_count_map[char] = 1

    return SortedList([Huffman_Node(char=char, count=count) for char, count in char_count_map.items()],
                      key=lambda node: node.count)


def _build_huffman_tree(ordered_nodes: SortedList) -> Huffman_Node:
    """
    Builds the Huffman Tree from the bottom up

    Args:
        ordered_nodes (SortedList[Huffman_Node]): a list of Huffman_Nodes sorted in ascending order by frequency

    Returns:
        the root node of the Huffman Tree that was constructed from the list of nodes
    """
    while len(ordered_nodes) > 1:
        left, right = ordered_nodes[0], ordered_nodes[1]
        ordered_nodes.add(Huffman_Node(count=left.count + right.count, left=left, right=right))
        del ordered_nodes[0:2]

    return ordered_nodes[0]


def _generate_huffman_encodings(huffman_root: Huffman_Node) -> Dict[str, str]:
    """
    Generates a Huffman encoding map which can be used for encoding strings one character at a time

    Args:
        huffman_root (Huffman_Node): the root of the Huffman tree

    Returns:
        a map of character -> Huffman-encoding pairs
    """

    def loop(huffman_node: Huffman_Node, prefix: str, encodings: Dict[str, str]):
        if huffman_node.left:
            loop(huffman_node.left, prefix + "0", encodings)
        if huffman_node.right:
            loop(huffman_node.right, prefix + "1", encodings)
        if huffman_node.is_leaf():
            encodings[huffman_node.char] = prefix
        return encodings

    if huffman_root:
        return loop(huffman_root, "", {})


def huffman_encoding(data: str) -> Tuple[str, Huffman_Node]:
    """
    Huffman-encodes the given string

    Args:
        data (str): the string to encode

    Returns:
        The encoded string, and the Huffman tree required to decode the string
    """
    char_count_nodes = _char_count_nodes(data)
    huffman_tree = _build_huffman_tree(char_count_nodes)
    encodings = _generate_huffman_encodings(huffman_tree)
    encoded_data = "".join([encodings[char] for char in data])
    return encoded_data, huffman_tree


def huffman_decoding(encoded_data, huffman_root):
    """
    Decodes the given data using the supplied Huffman tree

    Args:
        encoded_data (str): the data to decode
        huffman_root (Huffman_Node): the root of the Huffman tree used to encode the data

    Returns:
        the decoded value
    """
    decoded_data = ""
    node = huffman_root
    for char in encoded_data:
        if char == "0" and node.left:
            node = node.left
        elif char == "1" and node.right:
            node = node.right

        if node.is_leaf():
            decoded_data += node.char
            node = huffman_root

    return decoded_data


if __name__ == "__main__":
    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_sentence, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_sentence, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_sentence))

    decoded_sentence = huffman_decoding(encoded_sentence, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_sentence)))
    print("The content of the encoded data is: {}\n".format(decoded_sentence))
