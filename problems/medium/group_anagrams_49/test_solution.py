from .solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def assert_anagram_groups_equal(self, result, expected):
        result_sets = [set(group) for group in result]
        expected_sets = [set(group) for group in expected]
        assert set(map(frozenset, result_sets)) == set(map(frozenset, expected_sets))

    def test_example_1_sorted_string(self):
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        result = self.solution.group_anagrams_sorted_string(strs)
        self.assert_anagram_groups_equal(result, expected)

    def test_example_2_sorted_string(self):
        strs = [""]
        expected = [[""]]
        result = self.solution.group_anagrams_sorted_string(strs)
        assert result == expected

    def test_example_3_sorted_string(self):
        strs = ["a"]
        expected = [["a"]]
        result = self.solution.group_anagrams_sorted_string(strs)
        assert result == expected

    def test_example_1_count(self):
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        result = self.solution.group_anagrams_sorted_string(strs)
        self.assert_anagram_groups_equal(result, expected)

    def test_example_2_count(self):
        strs = [""]
        expected = [[""]]
        result = self.solution.group_anagrams_count(strs)
        assert result == expected

    def test_example_3_count(self):
        strs = ["a"]
        expected = [["a"]]
        result = self.solution.group_anagrams_count(strs)
        assert result == expected
