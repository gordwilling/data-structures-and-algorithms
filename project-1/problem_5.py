import hashlib
import os
import textwrap
from datetime import datetime


class Block:
    def __init__(self, data: str, previous_hash="0"):
        self.timestamp = datetime.utcnow().strftime("%H:%M %m/%d/%Y")
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self._calc_hash()

    def _calc_hash(self):
        sha = hashlib.sha256()
        hash_string = f"{self.timestamp}{self.data}{self.previous_hash}".encode("utf-8")
        sha.update(hash_string)
        return sha.hexdigest()

    def __str__(self):
        return textwrap.dedent(f"""\
                timestamp: {self.timestamp}
                     data: {self.data}
            previous_hash: {self.previous_hash}
                     hash: {self.hash}""")


class Node:
    def __init__(self, block: Block):
        self.value = block
        self.next = None


class BlockChain:
    def __init__(self):
        self.head = None

    def add(self, value: str):
        if self.head is None:
            self.head = Node(Block(value))
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(Block(value, node.value.hash))

    def __str__(self):
        if self.head:
            node = self.head

            block_sep = os.linesep + \
                "--------------------------------------------------------------------------------" + \
                os.linesep

            s = block_sep + str(node.value)
            while node.next:
                node = node.next
                s += block_sep + str(node.value)
            return s
        return ""


if __name__ == '__main__':
    block_chain = BlockChain()
    block_chain.add("This is the first link in the chain")
    block_chain.add("This is the second link in the chain")
    block_chain.add("This is the third link in the chain")
    print(block_chain)
