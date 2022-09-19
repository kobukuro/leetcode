# Hash Table, String, Counting
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_hash_map = {}
        for ran in ransomNote:
            if ran not in r_hash_map:
                r_hash_map[ran] = 1
            else:
                r_hash_map[ran] += 1
        m_hash_map = {}
        for ma in magazine:
            if ma not in m_hash_map:
                m_hash_map[ma] = 1
            else:
                m_hash_map[ma] += 1
        print(r_hash_map)
        print(m_hash_map)
        for key, value in r_hash_map.items():
            if key in m_hash_map:
                if value > m_hash_map[key]:
                    return False
            else:
                return False
        return True
