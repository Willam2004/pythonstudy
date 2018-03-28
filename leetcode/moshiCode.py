'''
    https://leetcode.com/problems/unique-morse-code-words/description/
'''


def Mos(words):
    mors = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
            ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    a = set()
    for w in words:
        val = ""
        for d in w:
            val = val + mors[ord(d) - ord('a')]
        a.add(val)
    return len(a)


words = ["gin", "zen", "gig", "msg"]
le = Mos(words)
print(le)
