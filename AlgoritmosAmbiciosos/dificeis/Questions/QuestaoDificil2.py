import sys

def chiefHopper_coinChange(heights):
    n = len(heights)
    dp = [0] * (n + 1)
    dp[n] = 0
    for i in range(n - 1, -1, -1):
        x = dp[i + 1] + heights[i]
        dp[i] = (x + 1) // 2
    return dp[0]

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    heights = list(map(int, data[1:]))
    print(chiefHopper_coinChange(heights))

if __name__ == "__main__":
    main()