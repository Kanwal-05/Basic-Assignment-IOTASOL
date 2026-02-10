#........................................JAVA CODE.............................

# int k = 0;

# for (int i = 0; i < 5; i++) {
#     for (int j = i; j < 6; j++) {
#         System.out.print("i ");
#         k++;
#     }

#     if (k > 3) {
#         System.out.println("Iotasol");
#     }
# }

#....................................PYTHON CONVERTED CODE....................
k = 0

for i in range(5):
    for j in range(i, 6):
        print("i ", end="")
        k += 1

    if k > 3:
        print("Iotasol")
