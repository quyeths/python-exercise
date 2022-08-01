word = "AABBBABBBB"
stack = []


def solution(word):
    wordLength = len(word)
    if wordLength == 1:
        return 1
    if not word:
        return 0
    for i in range(wordLength):
        stack.append(word[i])
        if len(stack) >= 2 and (
            (stack[-2] == "A" or stack[-2] == "B") and stack[-1] == "B"
        ):
            stack.pop()
            stack.pop()
    return len(stack)


print(solution(word))
