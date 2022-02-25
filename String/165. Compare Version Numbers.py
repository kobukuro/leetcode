# Two Pointers, String
class Solution:
    def delete_leading_zero(self, s):
        res = ''
        end_leading_zero = False
        for char in s:
            if not end_leading_zero:
                if char != '0' and not end_leading_zero:
                    res += char
                    end_leading_zero = True
            else:
                res += char
        return res

    def compareVersion(self, version1: str, version2: str) -> int:
        ver1 = version1.split('.')
        ver2 = version2.split('.')
        ver1 = [self.delete_leading_zero(v1) for v1 in ver1]
        ver2 = [self.delete_leading_zero(v2) for v2 in ver2]
        t = 1
        i = 0
        j = 0
        while i < len(ver1) or j < len(ver2):
            if i < len(ver1):
                temp1 = ver1[i]
            else:
                temp1 = '0'

            if j < len(ver2):
                temp2 = ver2[j]
            else:
                temp2 = '0'
            if temp1 == '':
                temp1 = '0'
            if temp2 == '':
                temp2 = '0'
            temp1 = int(temp1)
            temp2 = int(temp2)
            if temp1 > temp2:
                return 1
            if temp1 < temp2:
                return -1
            i += 1
            j += 1
        return 0


if __name__ == '__main__':
    version1 = "1.01"
    version2 = "1.001"
    print(Solution().compareVersion(version1=version1, version2=version2))
    version1 = "1.0"
    version2 = "1.0.0"
    print(Solution().compareVersion(version1=version1, version2=version2))
    version1 = "0.1"
    version2 = "1.1"
    print(Solution().compareVersion(version1=version1, version2=version2))
    version1 = "1.0.1"
    version2 = "1"
    print(Solution().compareVersion(version1=version1, version2=version2))  # 1
