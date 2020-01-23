# f = open('ex_1.txt', 'r')
# print(f.read())
# # for line in f:
# #     print(line)
# f.close()


g = open('ex_2.txt', 'w')
for i in range(100):
    g.write(' {} : {} ;\n'.format(i, i ** 2))
g.close()
