# Function to find number of unique BST based on n
def unique_binary_search_trees(n): 

	# DP to store the number of unique 
	# BST with key i 
	unique_tree = [0] * (n + 1) 

	# Base case 
	unique_tree[0], unique_tree[1] = 1, 1

	# fill the unique_tree table in top-down 
	# approach. 
	for i in range(2, n + 1): 
		for j in range(1, i + 1): 

			# n-i in right * i-1 in left 
			unique_tree[i] = unique_tree[i] + (unique_tree[i - j] *
							unique_tree[j - 1]) 

	return unique_tree[n] 


n = 3
print(unique_binary_search_trees(n)) 

