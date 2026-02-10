#........................................JAVA CODE.............................
# int arr[] = new int[]{0, 1, 1, 6, 6};
# int arr2[] = new int[]{2, 3, 1, 4, 6, 1};

# for (int i = 0; i < arr.length; i++) {
#     if (arr[i] < arr2[i]) {
#         arr[i] = arr2[i] * 2;
#     } else if (i < arr.length - 1) {
#         arr2[i] = arr[i + 1] * 2;
#     }

#     System.out.print(arr[i] * arr2[i] + " ");
# }

#....................................PYTHON CONVERTED CODE....................
arr = [0, 1, 1, 6, 6]
arr2 = [2, 3, 1, 4, 6, 1]

for i in range(len(arr)):
    if arr[i] < arr2[i]:
        arr[i] = arr2[i] * 2
    elif i < len(arr) - 1:
        arr2[i] = arr[i + 1] * 2

    print(arr[i] * arr2[i], end=" ")
