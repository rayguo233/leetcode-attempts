from collections import defaultdict
from typing import List, Tuple
import bisect
import sys


class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        winning_pers = []  # type: List[Tuple[int, int]]
        person_to_num_votes = defaultdict(int)
        max_num_votes_and_person = (-1, -1)
        for person, time in zip(persons, times):
            person_to_num_votes[person] += 1
            if person_to_num_votes[person] >= max_num_votes_and_person[0]:
                max_num_votes_and_person = (person_to_num_votes[person], person)
            winning_pers.append((time, max_num_votes_and_person[1]))
        self.winning_pers = winning_pers

    def q(self, t: int) -> int:
        i = bisect.bisect_right(self.winning_pers, (t, sys.maxsize)) - 1
        return self.winning_pers[max(i, 0)][1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)


if __name__ == '__main__':
    tvc = TopVotedCandidate([1,1,4,5,2,2,2,2], [1,2,3,4,5,6,7,8])
    print(tvc.winning_pers)
    print(tvc.q(9))
    # assert(sol.rob([2,4]) == 4)
    # assert(sol.rob([2,1,4,8]) == 9)
    # assert(sol.rob([2,1,4,8,9]) == 13)
