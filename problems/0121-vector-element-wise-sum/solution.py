def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
	# Return the element-wise sum of vectors 'a' and 'b'.
	# If vectors have different lengths, return -1.
	
	if len(a) != len(b):
		return -1
	
	dim = len(a)
	sum = [0] * dim

	for i in range(dim):
		sum[i] = a[i] + b[i]

	return sum
