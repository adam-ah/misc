package com.search;

import java.util.Arrays;

/*
 * Simple wrapper for Arrays.binarySearch.
 * NOT production ready code, for performance test only.
 */
public class BinaryArraysBinary implements Search {
    public int search(final int[] arr, final int val, final int left, final int right) {
        return Arrays.binarySearch(arr, left, right, val);
    }

    public long getAccessed() {
        return 0;
    }
}
