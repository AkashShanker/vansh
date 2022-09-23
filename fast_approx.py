def acc_approx_ln(n):
    k=0
    mat= []
    for i in range(0,n):
        sub = []
        for j in range(0,n):
            sub.append(0)
            k += 1
        mat.append(sub)
    return(mat)
print (acc_approx_ln(5))