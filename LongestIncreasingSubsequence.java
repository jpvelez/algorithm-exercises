class LongestIncreasingSubsequence{

    // Binary search method.
    // Takes in a stored array and a value, returns array index where
    // value is located, or should be located to keep array ordered.
    private static int rank(int val, int[] a)
	{ // Array must be sorted!
		int lo = 0;
		int hi = a.length - 1;
		while (lo <= hi)
		{
			int mid = lo + (hi - lo) / 2;
			if (val < a[mid]) hi = mid - 1;
			else if (val > a[mid]) lo = mid + 1;
			else return mid;
		}
		return lo;
	}

    private static int findLengthofLIS(int[] a)
    {
        int lengthOfLIS = 0;
        // Start the minimum value of the last number of
        // longest increasing sequences of different lengths.
        int[] M = new int[a.length]; int k = 0;
        for (int i = 0; i < a.length; i++)
        {
            if (a[i] > M[k])
            { k++; M[k] = a[i]; lengthOfLIS++; }
            else
            { // Find index of smallest int >= a[i].
                int ix = rank(a[i], a);
                M[ix] = a[i];
            }
        }

        for (int i = 0; i < M.length; i++)
        {  StdOut.println(M[i]); }

        return lengthOfLIS;
    }

    public static void main(String[] args)
    {
        int[] a = StdIn.readAllInts();
        int lengthOfLIS = findLengthofLIS(a);
        StdOut.println("The length of the longest increase subsequence is " + lengthOfLIS);
    }
}
