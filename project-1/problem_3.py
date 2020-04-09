import heapq
import sys
from typing import Dict, Tuple, List


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

    def __lt__(self, other):
        return self.count < other.count


def _char_count_nodes(data: str) -> List[Huffman_Node]:
    """
    Builds a list of Huffman Nodes, each containing a character and its frequency in the data string

    Args:
        data (str): The string to encode

    Returns:
        a priority queue of Huffman_Nodes ordered by frequency
    """

    char_count_map = {}
    for char in data:
        if char in char_count_map:
            char_count_map[char] += 1
        else:
            char_count_map[char] = 1

    if len(char_count_map) == 1:
        raise ValueError("Will not Huffman encode a string with only one character type")

    nodes = [Huffman_Node(char=char, count=count) for char, count in char_count_map.items()]
    heapq.heapify(nodes)
    return nodes


def _build_huffman_tree(q) -> Huffman_Node:
    """
    Builds the Huffman Tree from the bottom up

    Args:
        q (): the Huffman_Nodes priority-queued in ascending order by frequency

    Returns:
        the root node of the Huffman Tree that was constructed from the queue
    """

    if len(q) < 1:
        raise ValueError("Cannot build a tree from an empty list")

    while len(q) > 1:
        left, right = heapq.heappop(q), heapq.heappop(q)
        heapq.heappush(q, Huffman_Node(count=left.count + right.count, left=left, right=right))

    return heapq.heappop(q)


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


def test(data: str):
    print("The size of the data is: {}\n".format(sys.getsizeof(data)))
    print("The content of the data is: {}\n".format(data))

    encoded_data, huffman_root = huffman_encoding(data)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, huffman_root)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))
    print("--------------------------------------------------------------------------------")


if __name__ == "__main__":
    test("The bird is the word")
    # The size of the data is: 45
    # The content of the data is: The bird is the word
    # The size of the encoded data is: 22
    # The content of the encoded data is: 1110111111101010001100110000101100101101101011111101010000111001100001
    # The size of the decoded data is: 45
    # The content of the encoded data is: The bird is the word

    test("The quick brown fox jumps over the lazy dog")
    # The size of the data is: 68
    # The content of the data is: The quick brown fox jumps over the lazy dog
    # The size of the encoded data is: 38
    # The content of the encoded data is: 11010011011101000111010100010011101100110011001111101111001011000010111100100100101011010001111100001110110010111111000101110111010111100001101110111010000110011100111100011000100110101010101110
    # The size of the decoded data is: 68
    # The content of the encoded data is: The quick brown fox jumps over the lazy dog

    test("abcdefghijklmnopqrstuvwxyz")
    # The size of the data is: 51
    # The content of the data is: abcdefghijklmnopqrstuvwxyz
    # The size of the encoded data is: 30
    # The content of the encoded data is: 1010100001010011101111100111001101010110010101111101101111100000010011001100010011111111100111100010010001110100011101100001
    # The size of the decoded data is: 51
    # The content of the encoded data is: abcdefghijklmnopqrstuvwxyz

    # test("")
    # ValueError: Cannot build a tree from an empty list

    # test("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    # ValueError: Will not Huffman encode a string with only one character type
