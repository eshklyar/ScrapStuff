def nb_year(p0, percent, aug, p):
    i = 0
    while p0 < p:
        p0+=p0*percent/100 + aug
        i+=1

    return i

# def nb_year(p0, percent, aug, p):
#     sum(1 for )
#     i = 0
#     while p0 < p:
#         p0+=p0*percent/100 + aug
#         i+=1
#
#     return i

# 1000 + 1000 * 0.02 + 50 => 1070 inhabitants

print(nb_year(1000,2,50,1200))