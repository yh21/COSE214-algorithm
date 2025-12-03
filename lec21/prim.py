# Prim's Algorithm
# key[v] ← ∞ for all v (the minimum weight of edge connecting v to the tree)
# key[r] ← 0
# Q ← (key[v], v) for all v (priority queue)
# p[v] ← NIL for all v (parent of v in the tree)
# A ← ∅
# while Q not empty:
#   u ← ExtractMin(Q)
#   if u ≠ r:
#       A ← A ∪ {(p[u], u)}
#   for each neighbor v of u:
#       if v ∈ Q and w(u,v) < key[v]:
#           key[v] ← w(u,v)
#           DecreaseKey(Q, v)
#           p[v] ← u
# return A