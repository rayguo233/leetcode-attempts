from collections import defaultdict
from typing import List


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        zipped = [(age, score) for score, age in zip(scores, ages)]
        zipped = sorted(zipped)
        scores = [score for age, score in zipped]
        max_score_to_total = defaultdict(int)
        for score in scores:
            total = score + max([subtotal if young_score <= score else 0 for young_score, subtotal in max_score_to_total.items()] + [0])
            max_score_to_total[score] = max(total, max_score_to_total[score])
        return max(total for score, total in max_score_to_total.items())

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sol = Solution()
    print(sol.bestTeamScore([1,2,5,3], [3,1,4,2]))
    # assert(sol.coin_change([1,2,5], 11) == 3)
    # assert(sol.coin_change([1], 11) == 11)
    # assert(sol.coin_change([2], 11) == -1)
    # assert(sol.coin_change([20], 11) == -1)