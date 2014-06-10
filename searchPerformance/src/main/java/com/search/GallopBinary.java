package com.search;

/*
 * Galloping search implementation with binary search fallback.
 * NOT production ready code, for performance test only.
 */
public class GallopBinary implements Search {
    public long accessed;
    private final Binary binary = new Binary();

    public int search(final int[] arr, final int val, int left, int right) {
        if (arr == null || arr.length == 0 || arr[left] > val || arr[right - 1] < val) {
            return -1;
        }

        int jump = 1;

        while (left <= right) {
            final int curr = arr[left];
            accessed++;

            if (curr == val) {
                return left;
            }

            final int next = left + jump;

            if (curr > val || next > right) {
                if (curr > val) {
                    right = left;
                }

                left -= jump / 2;
                left++;
                return binary.search(arr, val, left, right);
            }

            left = next;
            jump *= 2;
        }

        return -1;
    }

    public long getAccessed() {
        final long old = accessed;
        accessed = 0;
        return old;
    }
}
