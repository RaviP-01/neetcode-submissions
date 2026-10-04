class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = s.replace(" ", "").lower()
        last = len(new_s) - 1
        first = 0
        while first <= last:
            a,b = new_s[last].isalnum(), new_s[first].isalnum()
            print(f"first: {new_s[first]} {first} last: {new_s[last]} {last}")
            if not a and not b:
                first += 1
                last -= 1
                continue
            if a and b:
                if new_s[first] != new_s[last]:
                    return False
            if first <= last and a:
                first += 1
            if last >= first and b:
                last -= 1
        return True