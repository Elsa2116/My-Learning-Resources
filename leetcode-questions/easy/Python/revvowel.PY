def reverseVowels(self, s: str) -> str:
        VOWELS = ["a", "e", "i", "o", "u"]

        string = [x for x in s]
        letters = []
        for i in range(len(string)):
            if string[i].lower() in VOWELS:
                letters.append(string[i])
                string[i] = '*'

        for i in range(len(string)):
            if string[i] == '*':
                string[i] = letters.pop()

        return ''.join(string)