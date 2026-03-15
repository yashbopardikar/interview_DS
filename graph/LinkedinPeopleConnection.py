"""LinkedIn is designed to connect people together, so that in people search and other related areas and LinkedIn will show a connection distance between two users.

E.g., Bob connects with Alice, and Alice connects with Frank, assuming there is no other connections, then Bob and Frank's connection distance is 2.

Examples:
Bob: ["Alice", "John"]
Alice: ["Bob", "Frank", "Lucy"]
Frank: ["Alice"]
John: ["Bob", "Jenny"]
Jenny: ["John", "Lucy"]
Lucy: ["Jenny", "Alice"]

The connection distance between Bob and Frank is 2
the connection distance between Lucy and Bob is 2, although there is a connection chain for Bob → John → Jenny → Lucy, but Bob → Alice → Lucy is shorter"""
import collections


class Solution:
    def propleDistance(self, graph, start, end):
        que = collections.deque()

        que.append([start, 0])
        visited = set(start)

        while que:
            srt, dist = que.popleft()
            for nei in graph.get(srt, []):
                if nei == end:
                    return dist+1

                if nei not in visited:
                    visited.add(nei)
                    que.append((nei, dist +1))
        return -1

sol = Solution()
linkedin_graph = {
    "Bob": ["Alice", "John"],
    "Alice": ["Bob", "Frank", "Lucy"],
    "Frank": ["Alice"],
    "John": ["Bob", "Jenny"],
    "Jenny": ["John", "Lucy"],
    "Lucy": ["Jenny", "Alice"]
}

print(sol.propleDistance(linkedin_graph, "Bob", "Lucy"))



