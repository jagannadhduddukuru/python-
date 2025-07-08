rows = 5
mid = (rows//2)+1
for i in range (1,rows+1):
    res=" "
    for j in range (1,rows+1):
      if i <=mid:
        if i == 1 or i == mid or j==rows:
           res+="*"+" "
        else:
           res+=" "+" "
      else:
        if i==rows or j ==1:
           res+="*"+" "
        else:
           res+=" "+" "
    print(res)

rows = 5
mid = (rows // 2) + 1   # mid = 3
for i in range(1, rows + 1):  # i from 1 to 5
    res = " "
    for j in range(1, rows + 1):  # j from 1 to 5
        if i == 1 or i == mid or i == rows or j == rows:
            res += "*" + " "
        else:
            res += " " + " "
    print(res)


       
          
           
