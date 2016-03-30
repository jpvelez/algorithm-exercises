# 1. Increasing Subsequence Algorithm
# Compile source code.
findLIS.class: findLIS.java
	javac findLIS.java
	
# Run algorithm on sequence, save solution to disk.
lis_solution.txt: findLIS.class
	echo '2 4 3 5 1 7 6 9 8' | java findLIS > $@
