#cerner_2^5_2020
m, n = 5, 5
g = [[" " for a in range(6*m)] for b in range(m)]
for c, e in enumerate(g):
    for d, f in enumerate(range(len(e))):
        if (d%m == 0) or d == 3*m+3 or d == c+3*m and c != n-1 or (d == 2*m+3 or d == 5*m+3) and c != n-2 or (c == n-2 and ((d == 11) or (d == 26))) or (((d%m != m-1) and (((c == 0 or c == n-1) and not (3*m <= d <= 3*m+2) and not ((d == 2*m+1 or d == 5*m+1) and c == n-1)) or (c == n-3 and (d > m and not (3*m+1 <= d <= 3*m+2)))))):
            g[c][d] = "*"        
    print("".join(e))

'''
Prints:
**** **** **** *  * **** ****
*    *    *  * ** * *    *  *
*    **** **** * ** **** ****
*    *    **   *  * *    **
**** **** * ** *  * **** * **
'''
