class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letters.append(target)
        new_letters = sorted(list(set(letters)))
        if new_letters.index(target)+1 >= len(new_letters):
            return new_letters[0]
        return new_letters[new_letters.index(target) + 1]
