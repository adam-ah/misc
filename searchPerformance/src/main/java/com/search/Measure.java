package com.search;

import java.util.Arrays;
import java.util.Random;

public class Measure {
    private final int[] arr;

    public Measure(final int n) {
        arr = getArray(n);
    }

    public static void start() {
        final int n = 110 * 1000 * 1000;

        for (int i = 10000; i < n; i *= 2) {
            System.out.println("Size " + i);
            new Measure(i).measureAll();
        }
    }

    private void measureAll() {
        final int distance = 10;
        final int sampleCount = 20;
        final int times = 10;

        final Search binaryarraybin = new BinaryArraysBinary();
        final Search interseq = new InterpolationSequential(distance);
        final Search inter = new Interpolation();
        final Search sampling = new Sampling(sampleCount);
        final Search binary = new Binary();
        final Search gallop = new Gallop();
        final Search gallopbin = new GallopBinary();

        measure(binaryarraybin, times);
        measure(interseq, times);
        measure(inter, times);
        measure(sampling, times);
        measure(binary, times);
        measure(gallop, times);
        measure(gallopbin, times);
    }

    private static int[] getArray(final int n) {
        final int[] arr = new int[n];
        final Random rnd = new Random();

        for (int i = 0; i < arr.length; i++) {
            arr[i] = rnd.nextInt(n * 5);
        }

        Arrays.sort(arr);
        return arr;
    }

    public void measure(final Search search, final int TIMES) {
        final long pre = System.currentTimeMillis();
        for (int i = 0; i < TIMES; i++) {
            for (final int val : arr) {
                final int pos = search.search(arr, val, 0, arr.length);
                if (val != arr[pos]) {
                    throw new IllegalArgumentException("Incorrect value found: " + val
                            + " instead of " + arr[pos]);
                }
            }
        }
        final long post = System.currentTimeMillis();
        System.out.println(post - pre);
        System.out.println("#" + search.getAccessed());
    }
}
