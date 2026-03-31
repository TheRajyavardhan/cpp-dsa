def longest_repeating_char_placement(s,k):
    count = {}
    left = 0
    max_freq = 0
    max_length = 0

    for right in range(len(s)):
        char = s[right]
        count[char] = count.get(char,0) + 1

        max_freq = max(max_freq, count[char])

        if (right-left+1) - max_freq > k:
            left_char = s[left]
            count[left_char] -= 1
            left += 1

        max_length = max(max_length, right-left+1)

    return max_length


s = "AABABBA"
k = 1

print(longest_repeating_char_placement(s,k))