class Solution:
    def isPalindrome(self, s: str) -> bool:
        last = len(s) - 1
        first = 0
        while first <= last:
            a,b = s[last].isalnum(), s[first].isalnum()
            print(f"first: {s[first].lower()} {first} last: {s[last].lower()} {last}")
            if not a and not b:
                first += 1
                last -= 1
                continue
            if a and b:
                if s[first].lower() != s[last].lower():
                    return False
            if first <= last and a:
                first += 1
            if last >= first and b:
                last -= 1
        return True