#........................................JAVA CODE.............................
# abc(0, 5);

# public void abc(int i, int j) {
#     System.out.print(i);

#     if (i < 6) {
#         i++;
#         j--;
#         abc(i, j);
#     }

#     if (j < 0) {
#         return;
#     }

#     System.out.println(j);
# }


#....................................PYTHON CONVERTED CODE....................
def abc(i, j):
    print(i, end="")

    if i < 6:
        i += 1
        j -= 1
        abc(i, j)

    if j < 0:
        return

    print(j)


abc(0, 5)
