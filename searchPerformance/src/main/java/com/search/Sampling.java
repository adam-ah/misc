package com.search;

/*
 * Sampling search implementation.
 * NOT production ready code, for performance test only.
 */
public class Sampling implements Search {
    public long accessed;
    private final int sampleCount;
    Binary binary;

    public Sampling(final int sampleCount) {
        this.sampleCount = sampleCount;
        binary = new Binary();
    }

    public int search(final int[] arr, final int val, int left, int right) {
        if (arr == null || arr.length == 0 || arr[left] > val || arr[right - 1] < val) {
            return -1;
        }

        final int SAMPLECOUNT = sampleCount;
        final int MINSIZE = 100 * SAMPLECOUNT;

        while (left + MINSIZE < right) {
            final int[] samples = new int[SAMPLECOUNT];
            final int[] positions = new int[SAMPLECOUNT];
            final int jumpsize = (right - left) / SAMPLECOUNT;

            for (int i = 0; i < samples.length - 1; i++) {
                final int pos = left + i * jumpsize;
                samples[i] = arr[pos];
                accessed++;
                positions[i] = pos;
            }

            samples[samples.length - 1] = Integer.MAX_VALUE;
            positions[samples.length - 1] = right;

            int upper = 0;
            while (upper < samples.length && samples[upper] <= val) {
                upper++;
            }

            final int lower = upper - 1;

            left = positions[lower];
            right = positions[upper];
        }

        return binary.search(arr, val, left, right);
    }

    public long getAccessed() {
        final long old = accessed;
        accessed = 0;
        return old;
    }
}
