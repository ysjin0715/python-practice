#2.
print('방문을 환영합니다!')
print('방문을 환영합니다!')
print('방문을 환영합니다!')
print('방문을 환영합니다!')
print('방문을 환영합니다!')

# for i in range(1000):
#     print('방문을 환영합니다!')

#4.
for i in [1, 2, 3, 4, 5]:
    print('방문을 환영합니다')

#5.
for i in [1, 2, 3, 4, 5]:
    print("i=",i)

for a in [1, 2, 3, 4, 5]:
    print("9*",a,"=",9*a)

#6.
for b in range(5):
    print('방문을 환영합니다')

print(list(range(10)))

#7.
for i in range(1,6,1):
    print(i,end="")

for i in range(10,0,-1):
    print(i,end="")

#8.
import turtle
t=turtle.Turtle()
t.shape('turtle')

for count in range(6):
    t.circle(100)
    t.left(360/6)