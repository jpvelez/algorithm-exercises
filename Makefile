# 1. Increasing Subsequence Algorithm
# Compile source code.
findLIS.class: findLIS.java
	javac findLIS.java

# Run algorithm on sequence, save solution to disk.
lis_solution.txt: findLIS.class
	echo '2 4 3 5 1 7 6 9 8' | java findLIS > $@

# 2. Nearest Stars.
# Download zipped data.
data/hygdb.gz:
	mkdir -p data
	curl http://www.astronexus.com/files/downloads/hygdata_v3.csv.gz > $@

# Find 5 nearest neighbors stars to Sol using online K-Nearest-Neighbors algorithm.
export PATH := $(pwd):$(PATH)  # Execute working dir scripts as shell commands.
knn_online_solution.txt: data/hygdb.gz findstar
	chmod 744 findstar # Make script executable.
	gunzip -c data/hygdb.gz | findstar -k 5 > $@

# Find 10 nearest neighbors to Sol and arbitrary point in space,
# using KDTree and offline KNN algorithm.
knn_offline_solution.txt: data/hygdb.gz findstar
	chmod 744 findstar
	gunzip -c data/hygdb.gz | findstar -k 10 --search-points 0,0,0 128,-123,0294 > $@
