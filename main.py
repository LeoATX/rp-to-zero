#
# custom = []
# current = int(input("enter current RP: "))
# rp = [575, 1380, 2800, 4500, 6500, 13500]
# league = [-270, -585, -790, -880, -975, -260, -300, -390, -438, -487, -520, -750, -975, -1350, -1820, -2775, -3250,
#           -165, -225, -1125, -2250, -5625, -125, -125, -195, -975, -1950, -350, -195, -640, -250, -3450, -1850, -1020,
#           -520, -290, -2440, -1590, -990, -670, -390, -290]
# league_on_sale = [-487, -260, -300, -338, -390, -438, -487, -607, -877, -944, -975, -2500, -2650, -6520, -12500]
# tft = [-260, -390, -490, -750, -925, -1900, -2450, -4900, -1380, -2900, -625, -2500, -5000]
#
#
# master = list()
# # options +
# master += rp + league + league_on_sale
# master = [*set(master)]
# master.sort()


class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        output = list()
        candidates = candidates

        output.append(self.find_target(candidates, target))

        return output

    def find_target(self, current, target):
        print(current, target)
        print(sum(current))
        if sum(current) == target:
            return current
        if sum(current) > target:
            return

        for number in candidates:
            current.append(number)

        print(current)
        self.find_target(current, target)


solution_obj = Solution()
solution_obj.combinationSum([2, 3, 6, 7], 7)

