#........................................JAVA CODE.............................
# int arr[] = new int[]{0, 1, 1, 6, 6};

# for (int i = 0; i < arr.length; i++) {
#     if (arr[i] < 2) {
#         arr[i + 1] += 1;
#     }

#     System.out.print(arr[i] + " ");
# }

#....................................PYTHON CONVERTED CODE....................
arr = [0, 1, 1, 6, 6]

for i in range(len(arr)):
    if arr[i] < 2:
        arr[i + 1] += 1

    print(arr[i], end=" ")



# output : 0 2 7 7 6 