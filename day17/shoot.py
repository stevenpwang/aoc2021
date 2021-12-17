c =0
x1 = 175
x2 = 227
y1 = -134
y2 = -79
for x in range(0,x2+1):
    for y in range(y1, -y1+1):
        xacc = x
        yacc = y
        px = 0
        py = 0
        while px <= x2 and py >= y1:
            
            px += xacc
            py += yacc
            if x1 <= px and px<= x2 and y1 <= py and py <= y2:
                #print(str(x)+","+str(y))
                c+=1
                break
            if xacc > 0:
                xacc = xacc -1
            yacc = yacc -1
                
print(c)