
Бинарный поиск на:

Prolog
```
binary_search(_, [], 0).
binary_search(X, [X|_], 1).
binary_search(X, [H|T], N) :- X < H, binary_search(X, [], N).
binary_search(X, [H|T], N) :- X > H, binary_search(X, T, N).
binary_search(X, [H|T], N) :- X = H, N is 1.

Пример использования:
binary_search(3, [1, 2, 3, 4, 5], X).
Результат:
X = 1.
```
Python
```def binary_search(x, arr):
    if len(arr) == 0:
        return 0
    if x == arr[0]:
        return 1
    if x < arr[0]:
        return binary_search(x, arr[:len(arr)//2])
    if x > arr[0]:
        return binary_search(x, arr[len(arr)//2:])
    return 0

result = binary_search(3, [1, 2, 3, 4, 5])
print(result) # Output: 1
```
Java

```
public class BinarySearch {
    public static int binarySearch(int x, int[] arr) {
        int left = 0;
        int right = arr.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (arr[mid] == x) {
                return 1;
            }
            if (arr[mid] < x) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return 0;
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int x = 3;
        int result = binarySearch(x, arr);
        System.out.println(result); // Output: 1
    }

```