import turtle

t = turtle.Turtle()
t.speed(0)
n=int(input("stargon vertices? = "))
dict = {}
j=int(input("stargon skips? = "))
while j <= n/2:
  #get points on the circle for making the stargon
  for i in range(n):
    t.circle(3.14*20,360/n)
    dict[str(i)] = [t.xcor(),t.ycor()]
  h= dict[str(j)]
  i=-1
  #connects points to the stargon based on the skip number
  while i< n:
    i=i+j
    i%=n
    
    try:
      if dict[str(i)]== 0 and list(dict.values()).count(0)!=n:
        t.penup()
        t.goto(dict[str(i+1)][0],dict[str(i+1)][1])
        
        t.pendown()
        
        dict[str(i)]=0
        i+=1
      else:
        t.goto(dict[str(i)][0],dict[str(i)][1])
        dict[str(i)]=0
      
    except:
      pass
    if list(dict.values()).count(0)==n:
      break
  #QOL stuff so that you can run it multiple times for the same side numbers
  t.penup()
  t.goto(0,0)
  print("stargon number",str(n)+", skip number",j, "(and", str(n-j)+")")
  print("interior: ",((n-2)*180-(360/n)*(-abs(j-n/2)+n/2-1)*n))
  if(n/2==j):
    print("exterior: ",360.0)
  else:
    print("exterior: ",180*n-((n-2)*180-(360/n)*(-abs(j-n/2)+n/2-1)*n))
  print("{PRESS ENTER TO GENERATE MORE}")
  j+=1
  input()
  t.clear()
  t.pendown()
print("there are no more unique stargons with this side length")