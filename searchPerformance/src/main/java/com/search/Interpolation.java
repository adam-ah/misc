package com.search;

/*
 * Interpolation search implementation.
 * NOT production ready code, for performance test only.
 */
public class Interpolation implements Search {
    public long accessed;

    public int search(final int[] arr, final int val, int left, int right) {
        if (arr == null || arr.length == 0 || arr[left] > val || arr[right - 1] < val) {
            return -1;
        }

        while (left < right && left >= 0 && right <= arr.length) {
            final int leftValue = arr[left];
            accessed++;
            final int rightValue = arr[right - 1];
            accessed++;

            final float average = ((float) rightValue - leftValue) / (right - left);
            int midpoint = left;
            if (average != 0) {
                final int diff = val - leftValue;
                final int steps = (int) (diff / average);
                midpoint = left + steps;

                // Overshoots.
                if (midpoint >= right) {
                    midpoint = (left + right) / 2;
                }
            }

            final int mid = arr[midpoint];
            accessed++;

            if (mid == val) {
                return midpoint;
            } else if (val < mid) {
                right = midpoint - 1;
            } else {
                left = midpoint + 1;
            }
        }

        if (arr[left] == val) {
            return left;
        }

        return -1;
    }

    public long getAccessed() {
        final long old = accessed;
        accessed = 0;
        return old;
    }
}
