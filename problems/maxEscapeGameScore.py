"""
Problem: Maximum Escape Game Score
Platform: Hackerrank
Difficulty: Medium
Topics: [Topics]

Description:
In an escape game, players must solve puzzles to earn points and progress. One puzzle involves an array of integers and specific rules for earning points. Here are the rules:

1. Select a value v. Remove all occurrences of that value from the array and add their sum to your score.
2. Remove all elements equal to v + 1 or v - 1 without scoring points.
3. Repeat steps 1 and 2 until the array is empty.

Determine the maximum score that can be obtained by following these rules.

Approach:
- We want to continue until the elements array is empty.
- Selection of integers within the arrya comes down to 
    1. Select

Time Complexity: O(?)
Space Complexity: O(?)

Notes:
- [What you learned or what to improve]
"""

class Solution:
    def maxEscapeGameScore(self, elements: list[int]) -> int:
        # TODO Implemnent Replace with problem signature
        # TODO Solution Here

        if not elements:
            return 0

        scores = {}
        for elem in elements:
            if elem in scores:
                scores[elem] += elem
            else:
                scores[elem] = elem

        dp = []

        prev_best = 0
        prev_prev_best = 0
        prev_elem = None

        for elem in sorted(scores):
            if prev_elem is not None and elem == prev_elem + 1:
                take = scores[elem] + prev_prev_best
            else:
                take = scores[elem] + prev_best

            skip = prev_best
            current_best = max(take, skip)

            prev_prev_best = prev_best
            prev_best = current_best
            prev_elem = elem

            dp[elem] = current_best

        return prev_best



if __name__ == "__main__":
    solution = Solution()