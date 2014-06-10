package com.search;

/*
 * Common interface for search performance testing.
 */
public interface Search {
    int search(final int[] arr, final int val, final int left, final int right);

    long getAccessed();
}
