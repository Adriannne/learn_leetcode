class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for byte in magazine:
            if byte in ransomNote:
                ransomNote = ransomNote.replace(byte, '', 1)
        if ransomNote == '':
            return True
        return False

if __name__ == '__main__':
    s = Solution()
    result = s.canConstruct(ransomNote="aa", magazine="aab")
    print(result)