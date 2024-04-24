def can_generate(A, E, B):

    A_set = set(a + E for a in A) | set(a - E for a in A)
    
    for b in B:
        if b not in A_set:
            return False
    
    return True

A = [1, 2, 3, 4, 5]
E = 2
B = [5, 3, 6, 3, 0]
print(can_generate(A, E, B))  