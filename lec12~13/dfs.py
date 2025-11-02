# pseudocode of DFS

# DFS(s, t)
#   color(s) <- gray
#   d(s) <- t
#   t += 1
#   foreach v in N(s) do
#       if color(v) == white
#           p(v) <- s
#           t <- DFS(v, t)
#           t += 1
#   f(s) <- t
#   color(s) <- green
#   return f(s)