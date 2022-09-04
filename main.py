import sys
sys.setrecursionlimit(20000)
custom = []
current_rp = int(input("enter current RP: "))
rp = [0, 575]  # [575, 1380, 2800, 4500, 6500, 13500]
league = [-270, -585, -790, -880, -975, -260, -390, -438, -487, -520, -750, -975, -1350, -1820, -2775, -3250,
          -165, -225, -1125, -2250, -5625, -125, -125, -195, -975, -1950, -350, -195, -640, -250, -3450, -1850, -1020,
          -520, -290, -2440, -1590, -990, -670, -390, -290]
league_on_sale = [-487, -260, -300, -338, -390, -438, -487, -607, -877, -944, -975, -2500, -2650, -6520, -12500]
tft = [-260, -390, -490, -750, -925, -1900, -2450, -4900, -1380, -2900, -625, -2500, -5000]


master = []
# options +
master += league
master = [*set(master)]  # remove duplicates
master.sort()
master.reverse()
print("master" + str(master))


class Solution:
    def __init__(self, adjustment):
        self.adj = adjustment

    def combination_sum(self, candidates: list[int]) -> list[list[int]]:
        output = []
        self.find_target([], candidates, output)
        return output

    def find_target(self, current, candidates, output):
        if sum(current) + self.adj == 0:
            current.sort()
            output.append(current)
            return
        if sum(current) + self.adj < 0:
            return

        for loop in range(len(candidates)):
            self.find_target(current + [candidates[loop]], candidates[:loop + 1], output)


for add_rp in rp:
    adj = current_rp + add_rp
    solution_obj = Solution(adj)
    print(add_rp, "rp")
    for combination in solution_obj.combination_sum(master):
        print(combination)
