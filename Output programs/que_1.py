
#........................................JAVA CODE.............................

# abc(0, 5);

# public void abc(int i, int j) {
#     if (i < 6) {
#         i++;
#         j--;
#         abc(i, j);
#     }

#     System.out.print(i);

#     if (j < 0) {
#         return;
#     }

#     System.out.println(j);
# }

#....................................PYTHON CONVERTED CODE....................
def abc(i, j):
    if i < 6:
        i += 1
        j -= 1
        abc(i, j)

    print(i, end="")

    if j < 0:
        return

    print(j)


abc(0, 5)
