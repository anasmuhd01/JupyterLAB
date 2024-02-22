# mylist = [1, "jack", 5.0, 6, 9, 13]
#
# for i, entry in enumerate(mylist):
#     print(i, entry)
#

#
# x = [num for num in range(2, 20+1) if num % 2 == 0]
# print(x)

# result = [(i, i ** 2) for i in range(1, 10+1)]
# print(result)

# x =[num for num in range(1, 36+1) if 36%num == 0]
# print(x)
#

# ------------------> Below is importent <-----------------------------------
# result = [(i,j) for i in range(1, 10+1) for j in range(1, 10+1) if i+j <= 50  if i%j == 0 and j%i == 0]
# print(result)
# ----------------------------------------------------------------------------

# ------------------> Below is importent <-----------------------------------
# mylist = [2, 3, 5, 3.0, 7, 3, 9, 3.0]
# new_list = [val for val in mylist if float(val) == 3]
# print(new_list)
# ----------------------------------------------------------------------------

# def modify(li):
#     li[-1] = 'modified'
#     return li
# #>>-----NO, a function does not always have to have /
# # an explicit return statement---------------------<<
# lis = [1,2,3,4,5]
# modify(lis)
# print(modify(lis))

# a =3
# def chek(a):
#     print(a)
# print(chek(2))


# >>>-----------------------------------------------------------------<<<<<<<
# def left():
#     print("left")
# def right():
#     print("right")
# def walk_1():
#     print("walk 1")
# for i in range(0,10,2):
# # each iteration prints twice, so we step twice
#     left()
#     right()
# def walk_2():
#     print("walk 2")
# # try without printing twice
# # use an indicator whether we print left or right. We cannot call
# # it "left", or it will override the global name "left"
#     lft = True
#     for i in range(0,10):
# # every iteration once, no double-step
#         if lft:
#             left()
#         else:
#             right()
# # every iteration prints only once!
#         lft = not lft # but we must switch each time
# def walk_3():
#     print("walk 3")
# # again without printing twice, but we use function variables
# this_step, next_step = left, right
# for i in range(0, 10):
#     this_step() # yes, this calls the current function
# this_step, next_step = next_step, this_step
#
# walk_1()
# walk_2()
# walk_3()
# >>>-----------------------------------------------------------------<<<<<<<

# <<<<<------------------------------------------------------------->>>>>>>>>>
#
# def test(a,b,c,d):
#     if a>b:
#         a,b = b,a
#     if c>d:
#         c,d = d,c
#     if b>d:
#         b,d = d,b
#     if a>c:
#         a,c = c,a
#
#     return a,b,c,d
#
#
# print(test(876,342,223,56))
# <<<<<------------------------------------------------------------->>>>>>>>>>
A = [4,3,10,1,9,7,8,6,2,5]

for i in range(len(A)-1):
    if A[i] > A[i+1]:
        A[i], A[i+1] = A[i+1], A[i]
print(A)

for i in range(len(A)-1, 0, -1):
    if A[i] < A[i-1]:
        A[i],A[i-1] = A[i-1], A[i]
print(A)

for j in range(0, len(A)):
    for i in range(len(A)-1, j, -1):
        if A[i] < A[i-1]:
            A[i],A[i-1] = A[i-1], A[i]
print(A)

for i in range(0, len(A)):
    for j in range(0, len(A)-1-i):
        if A[j]> A[j+1]:
            A[j], A[j+1] = A[j+1], A[i]
print(A)