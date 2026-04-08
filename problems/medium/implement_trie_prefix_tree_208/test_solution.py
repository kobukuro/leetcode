from .solution import Trie


class TestSolution:

    def call(self, methods, params, expected):
        results = []
        obj = None
        for method, param in zip(methods, params):
            if method == "Trie":
                obj = Trie()
                results.append(None)
            else:
                result = getattr(obj, method)(*param)
                results.append(result)
        assert results == expected

    def test_example_1(self):
        """
        Example 1:
        Input: ["Trie", "insert", "search", "search", "starts_with", "insert", "search"]
               [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
        Output: [null, null, true, false, true, null, true]

        Explanation:
        Trie trie = new Trie();
        trie.insert("apple");
        trie.search("apple");   // return True
        trie.search("app");     // return False
        trie.starts_with("app"); // return True
        trie.insert("app");
        trie.search("app");     // return True
        """
        self.call(
            ["Trie", "insert", "search", "search", "starts_with", "insert", "search"],
            [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]],
            [None, None, True, False, True, None, True],
        )
