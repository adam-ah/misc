package com.search;

/*
 * Interpolation search implementation with linear search fallback.
 * NOT production ready code, for performance test only.
 */
public class InterpolationSequential implements Search {
    public long accessed;
    private final int distance;

    public InterpolationSequential(final int distance) {
        this.distance = distance;
    }

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

            final int err = val - mid;

            if (Math.abs(err) < distance * average) {
                return sequential(arr, val, midpoint, err);
            }

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

    private int sequential(final int[] arr, final int val, final int start, final int sign) {
        final int step = sign < 0 ? -1 : 1;

        for (int i = start; i < arr.length && i >= 0; i += step) {
            final int curr = arr[i];
            accessed++;
            if (curr == val) {
                return i;
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
