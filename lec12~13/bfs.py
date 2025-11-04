# pseudocode of BFS

# BFS(s):
#   vis[v] <- false for all v
#   L_0 <= {s}
#   for i = 0...n-1 do
#       if L_i is empty then exit
#       while L_i is not empty do
#           u <-L_i.pop()
#           foreach x in N(u) do
#               if vis[x] == false then
#                   vis[x] = true
#                   L_{i+1}.insert(x)
#                   p(x) <- u