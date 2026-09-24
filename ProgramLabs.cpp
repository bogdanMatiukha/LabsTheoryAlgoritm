#include <iostream>
using namespace std;

void printArray(int arr[], int n)
{
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";

    cout << endl;
}

// Linear search
int linearSearch(int arr[], int n, int key, int& actions)
{
    actions = 0;

    for (int i = 0; i < n; i++)
    {
        actions++;

        if (arr[i] == key)
            return i;
    }

    return -1;
}

// Binary search
int binarySearch(int arr[], int n, int key, int& actions)
{
    actions = 0;

    int left = 0;
    int right = n - 1;

    while (left <= right)
    {
        actions++;

        int middle = left + (right - left) / 2;

        if (arr[middle] == key)
            return middle;

        if (arr[middle] < key)
            left = middle + 1;
        else
            right = middle - 1;
    }

    return -1;
}

// Bubble sort
void bubbleSort(int arr[], int n)
{
    int totalActions = 0;

    cout << "\n--- Bubble Sort ---\n";

    cout << "Initial array: ";
    printArray(arr, n);

    for (int i = 0; i < n - 1; i++)
    {
        int actions = 0;

        for (int j = 0; j < n - 1 - i; j++)
        {
            actions++;

            if (arr[j] > arr[j + 1])
            {
                swap(arr[j], arr[j + 1]);
                totalActions++;
            }
        }

        cout << "Step " << i + 1 << ": ";
        printArray(arr, n);

        cout << "Number of comparisons at this step: "
            << actions << endl;

        cout << "Total number of swaps: "
            << totalActions << endl;
    }
}

// Selection sort
void selectionSort(int arr[], int n)
{
    int totalActions = 0;

    cout << "\n--- Selection Sort ---\n";

    cout << "Initial array: ";
    printArray(arr, n);

    for (int i = 0; i < n - 1; i++)
    {
        int actions = 0;
        int minIndex = i;

        for (int j = i + 1; j < n; j++)
        {
            actions++;
            totalActions++;

            if (arr[j] < arr[minIndex])
                minIndex = j;
        }

        if (minIndex != i)
            swap(arr[i], arr[minIndex]);

        cout << "Step " << i + 1 << ": ";
        printArray(arr, n);

        cout << "Number of comparisons at this step: "
            << actions << endl;

        cout << "Total number of comparisons: "
            << totalActions << endl;
    }
}

int main()
{
    const int n = 10;

    int arr[n] = { 37, 12, 85, 4, 56, 23, 91, 18, 7, 64 };

    cout << "Initial array:\n";
    printArray(arr, n);

    // Linear search
    int key;

    cout << "\nEnter an element to search: ";
    cin >> key;

    int actions;

    int result = linearSearch(arr, n, key, actions);

    if (result != -1)
    {
        cout << "Linear search: element found at position "
            << result << endl;
    }
    else
    {
        cout << "Linear search: element not found." << endl;
    }

    cout << "Number of performed actions: "
        << actions << endl;

    int bubbleArray[n];
    int selectionArray[n];

    for (int i = 0; i < n; i++)
    {
        bubbleArray[i] = arr[i];
        selectionArray[i] = arr[i];
    }

    // Sorting
    bubbleSort(bubbleArray, n);
    selectionSort(selectionArray, n);

    // Binary search
    cout << "\n--- Binary Search ---\n";

    cout << "Sorted array: ";
    printArray(selectionArray, n);

    cout << "Enter an element for binary search: ";
    cin >> key;

    result = binarySearch(selectionArray, n, key, actions);

    if (result != -1)
    {
        cout << "Binary search: element found at position "
            << result << endl;
    }
    else
    {
        cout << "Binary search: element not found." << endl;
    }

    cout << "Number of performed actions: "
        << actions << endl;

    return 0;
}