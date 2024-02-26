# 332. Reconstruct Itinerary

# You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

# All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

# For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

import collections


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.graph = collections.defaultdict(list)
        for orig, dest in tickets:
            self.graph[orig].append(dest)
        
        for _, dests in self.graph.items():
            dests.sort(reverse=True)
        
        self.result = []
        self.dfs('JFK')

        return self.result[::-1]
    
    def dfs(self, origin):
        dests = self.graph[origin]
        while dests:
            next_dest = dests.pop()
            self.dfs(next_dest)
        self.result.append(origin)