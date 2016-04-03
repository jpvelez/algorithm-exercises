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

# Run online version of findstar program.
# Add working dir to system, so we can use python script as a shell command.
export PATH := $(pwd):$(PATH)
result: data/hygdb.gz findstar
	chmod 744 findstar # Make findstar into an executable.
	gunzip -c data/hygdb.gz | findstar #--k 5
