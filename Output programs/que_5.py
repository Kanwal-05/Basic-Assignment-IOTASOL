#........................................JAVA CODE.............................
# int p = 5;

# for (int i = 0; i < 5; i++) {
#     for (int j = i; j < 5; j++) {
#         p++;
#     }

#     System.out.print("p" + p + " ");

#     for (int k = 5; k > i; k--) {
#         System.out.print(p - k);
#         p--;
#     }

#     System.out.println("");
# }

#....................................PYTHON CONVERTED CODE....................
p = 5

for i in range(5):
    for j in range(i, 5):
        p += 1

    print("p" + str(p), end=" ")

    for k in range(5, i, -1):
        print(p - k, end="")
        p -= 1

    print()
