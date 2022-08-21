import collections
def solution(phone_book):
    p_map = collections.defaultdict(int)
    for p in phone_book:
        p_map[p] = 1
    for nums in phone_book:
        for i in range(1, len(nums)):
            if p_map[nums[:i]]:
                return False
    return True

phone_book = ["119", "97674223", "1195524421"]
print(solution(phone_book))