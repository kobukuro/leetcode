# Hash Table, String, Design, Hash Function
class Codec:
    def __init__(self):
        self.map = {}
        self.init_url = 'http://tinyurl.com/'

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        num = random.getrandbits(128)
        while num in self.map:
            num = random.getrandbits(128)
        self.map[str(num)] = longUrl
        print(self.map)
        return f'{self.init_url}{num}'

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        print(self.map)
        return self.map[shortUrl.replace(self.init_url, '')]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
