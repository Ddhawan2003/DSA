class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_to_letters = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        result = ['']  # Start with an empty string

        for digit in digits:
            temp = []
            for prefix in result:
                for letter in digit_to_letters[digit]:
                    temp.append(prefix + letter)
            result = temp  # Move to the next digit

        return result
