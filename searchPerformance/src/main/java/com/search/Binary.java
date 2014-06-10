package com.search;

/*
 * Binary search implementation. 
 * NOT production ready code, for performance test only.
 */
public class Binary implements Search {
    public long accessed;

    public int search(final int[] arr, final int val, int left, int right) {
        if (arr == null || arr.length == 0 || arr[left] > val || arr[right - 1] < val) {
            return -1;
        }

        while (left <= right) {
            final int midpoint = (left + right) / 2;
            final int mid = arr[midpoint];
            accessed++;

            if (val < mid) {
                right = midpoint - 1;
            } else if (mid == val) {
                return midpoint;
            } else {
                left = midpoint + 1;
            }
        }

        return -1;
    }

    public long getAccessed() {
        final long old = accessed;
        accessed = 0;
        return old;
    }
}
