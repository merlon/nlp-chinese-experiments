import numpy as np
import lxml

def list2seg(s):
    seg=[]
    if len(s)<=1:
        return seg
    so_far=0
    for i in s[:-1]:
        so_far+=len(i)
        seg.append(so_far)
    return seg

def segmentation_distance(s,t):
    s_seg=list2seg(s)
    t_seg=list2seg(t)
    return edit_distance(s_seg,t_seg)

def edit_distance(s,t):
   # For all i and j, d[i,j] will hold the Levenshtein distance between
   # the first i characters of s and the first j characters of t.
   # Note that d has (m+1) x (n+1) values.
   #let d be a 2-d array of int with dimensions [0..m, 0..n]
   m=len(s)+1
   n=len(t)+1
   d=np.empty(shape=(m,n),dtype=int) 
   
   for i in range(m):
     d[i, 0] = i # the distance of any first string to an empty second string
                 # (transforming the string of the first i characters of s into
                 # the empty string requires i deletions)
   for j in range(n):
     d[0, j] = j # the distance of any second string to an empty first string
  
   for j in range(1,n):
     for i in range(1,m):
       if s[i-1] == t[j-1]:  
         d[i, j] = d[i-1, j-1]        # no operation required
       else:
         d[i, j] = min(d[i-1, j] + 1,  # a deletion
                       d[i, j-1] + 1,  # an insertion
                       d[i-1, j-1] + 1) # a substitution
  
   return d[m-1,n-1]

#print edit_distance([],[])
#print edit_distance([1],[])
#print edit_distance([1],[2])
#print edit_distance([1],[2,3])
#print edit_distance([1,2,3,4,5],[1,1,2,3,5])
