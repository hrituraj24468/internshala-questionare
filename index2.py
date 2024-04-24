def longest_subarray(A, K):
    n = len(A)
    max_len = 0
    curr_sum = 0
    sum_dict = {0: -1}
    
    for i in range(n):
        curr_sum += A[i]
        if curr_sum - K in sum_dict:
            max_len = max(max_len, i - sum_dict[curr_sum - K])
        if curr_sum not in sum_dict:
            sum_dict[curr_sum] = i
    
    return max_len

N = 5
K = 4
A = [1, 2, 1, 0, 1]
print(longest_subarray(A, K))  