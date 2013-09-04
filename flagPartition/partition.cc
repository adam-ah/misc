#include <iostream> // cout
#include <stdlib.h> // rand srand
#include <time.h> // time

using namespace std;

int partition(int array[], int n, int* left, int* right)
{
    if(!array || !n)
    {
        return 0;
    }

    int small = array[0];
    int large = array[n-1];
    if(small > large)
    {
        int tmp = large;
        large = small;
        small = tmp;
    }

    int wr = n-1;
    int wl = 0;

    for(int reader = 0; reader <= wr; )
    {
        int v = array[reader];

        if(v < small)
        {
            array[reader] = array[wl];
            array[wl] = v;
            wl++;
        }
        else if(v > large)
        {
            array[reader] = array[wr];
            array[wr] = v;
            wr--;
        }
        else
        {
            reader++;
        }
    }
    *left = wl;
    *right = wr;

    return 1;
}

void print(int array[], int n)
{
    for(int i=0; i < n; i++)
    {
        cout << array[i] << " ";
    }
    cout << "\n";
}

int main()
{
    int n = 10;
    int b[n];
    srand(time(NULL));

    int start = clock();
    for(int j = 0; j < 1000 * 1000; j++)
    {
        for(int i = 0; i < n; i++)
        {
            b[i] = rand() % n;
        }
        // print(b, n);
        int l, r;
        partition(b, n, &l, &r);
        // print(b, n);
    }
    int end = clock();
    cout << ((float)end - start)/CLOCKS_PER_SEC;

    // cout << l << " " << r;
}
