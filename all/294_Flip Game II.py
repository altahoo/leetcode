# 294. Flip Game II

# You are playing a Flip Game with your friend.

# You are given a string currentState that contains only '+' and '-'. You and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move, and therefore the other person will be the winner.

# Return true if the starting player can guarantee a win, and false otherwise.

class Solution:
    def canWin(self, currentState: str) -> bool:
        @lru_cache(None)
        def dfs(s):
            if '++' not in s:
                return False
            
            for i in range(len(s) - 1):
                if s[i:i + 2] == '++' and not dfs(s[:i] + '--' + s[i+2:]):
                    return True
            return False
        
        return dfs(currentState)