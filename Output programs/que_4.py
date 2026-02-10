#........................................JAVA CODE.............................
# for (int i = 0; i < 5; i++) {
#     int k = 0;

#     for (int j = i; j < 6; j++) {
#         System.out.print("i ");
#         k++;
#     }

#     if (k > 3) {
#         System.out.println("Iotasol");
#     }
# }

#....................................PYTHON CONVERTED CODE....................
for i in range(5):
    k = 0

    for j in range(i, 6):
        print("i ", end="")
        k += 1

    if k > 3:
        print("Iotasol")
