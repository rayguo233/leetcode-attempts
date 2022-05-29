import collections
from typing import List


class Solution:

    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]],
                       supplies: List[str]) -> List[str]:
        ingredients = [set(ing) for ing in ingredients]
        supp_to_rec = collections.defaultdict(list)
        for rec, ing in enumerate(ingredients):
            for supp in ing:
                supp_to_rec[supp].append(rec)
        res = []
        while supplies:
            supp = supplies.pop()
            for rec in supp_to_rec[supp]:
                ingredients[rec].remove(supp)
                if not ingredients[rec]:
                    res.append(recipes[rec])
                    supplies.append(recipes[rec])
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.removeDuplicateLetters('abaacbbca'))
    print(sol.removeDuplicateLetters('abadddacbddbc'))