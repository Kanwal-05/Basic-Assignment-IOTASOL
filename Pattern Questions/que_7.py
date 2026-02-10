rows=25
cols=50
canvas=[]
for i in range(rows):
    canvas.append([" "]*cols)

def diamond(row,column,size):
    for i in range(-size,size+1):
        for j in range(-size,size+1):
             if abs(i)+abs(j)<=size:
                 r=row+i
                 c=column+j

                 if 0<=r<rows and 0<=c<cols:
                     canvas[r][c]="*"

diamond(4,25,4)
diamond(10,10,4)
diamond(10,40,4)
diamond(18,25,4)

for row in canvas:
    print(" ".join(row))