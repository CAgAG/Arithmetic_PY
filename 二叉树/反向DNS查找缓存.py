class TrieNode:
    def __init__(self):
        CHAR_COUNT = 11
        self.isLeaf = False
        self.url = None
        self.child = [None] * CHAR_COUNT

        i = 0
        while i < CHAR_COUNT:
            self.child[i] = None
            i += 1


def GetIndexFromChar(c: str):
    return 10 if c == '.' else (ord(c) - ord('0'))


def GetCharFromIndex(i: int):
    return '.' if i == 10 else '0' + str(i)


class DNSCache:
    def __init__(self):
        self.CHAR_COUNT = 11
        self.root = TrieNode()  # IP 地址最大长度

    def insert(self, ip: str, url: str):
        length = len(ip)
        pCrawl = self.root
        level = 0
        while level < length:
            index = GetIndexFromChar(ip[level])
            if pCrawl.child[index] == None:
                pCrawl.child[index] = TrieNode()

            pCrawl = pCrawl.child[index]
            pCrawl.isLeaf = True
            pCrawl.url = url
            level += 1

    def searchDNSCache(self, ip: str):
        pCrawl = self.root
        length = len(ip)

        level = 0
        while level < length:
            index = GetIndexFromChar(ip[level])
            if pCrawl.child[index] is None:
                return None
            pCrawl = pCrawl.child[index]
            level += 1

        if pCrawl is not None and pCrawl.isLeaf:
            return pCrawl.url
        return None
