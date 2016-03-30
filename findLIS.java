class findLIS{

    // Binary Search algorithm.
    // Time complexity: O(logn); Space complexity: O(n)
    // Returns array index where search value is located if it
    // exists in array, or where it should be placed to keep array
    // ordered, and thus be findable in the future.
    private static int rank(int[] a, int lo, int hi, int val)
	{ // Array must be sorted!
		while (lo <= hi)
		{
			int mid = lo + (hi - lo) / 2;
			if      (val < a[mid]) hi = mid - 1;
			else if (val > a[mid]) lo = mid + 1;
			else return mid; // If you find the value.
		}
		return lo;           // If you don't.
	}

    // Longest Increasing Subsequence algorithm.
    // Time complexity: O(nlogn); Space complexity: O(n)
    // Most efficient known solution to LIS problem, using arrays and binary search.
    private static int findLengthofLIS(int[] S)
    {
        int lengthOfLIS = 0;  // Longest LIS seen so far.

        // Create second array to track intermediate results.
        // As we loop through S, we're going to be finding subsequences of
        // different lengths, and using M to store the minimum value observed
        // of the last element of these subsequences.
        int[] M = new int[S.length];
        int k = 0;  // index for M.

        // Set the min value of subsequence of length 1 to the first
        // value in the sequence. Required for loop to work properly!
        M[k] = S[k]; lengthOfLIS++;

        // Loop through the Sequence S..
        for (int i = 1; i < S.length; i++)
        {   // If element extends current LIS...
            if (S[i] > M[k])
            {   // Append element to M. Si is now the min value observed as the
                // last element of subsequences of length k + 1.
                k++; M[k] = S[i];
                lengthOfLIS++;     // Increment "longest LIS observed" tracker.
            }
            // If it doesn't, but potentially starts new LIS...
            else
            {   // Use BinarySearch to find the subsequence length for which
                // this element should become the new "last element min value".
                int lo = 0; int hi = k; // Constrain search to array section with values.
                int ix = rank(M, lo, hi, S[i]);
                M[ix] = S[i];  // Replace last element min val for subsequence
                               // of length ix + 1.
            }
        }
        return lengthOfLIS;
    }

    // LIS algorithm client. Handles I/O.
    public static void main(String[] args)
    {   // Spool Sequence into memory from standard in.
        int[] S = StdIn.readAllInts();
        // Find length of longest increasing subsequence of Sequence S.
        int lengthOfLIS = findLengthofLIS(S);
        // Report LIS length through standard out.
        StdOut.println("The length of the longest increasing subsequence is " + lengthOfLIS);
    }
}
