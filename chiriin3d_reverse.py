# -*- coding: utf-8 -*-
import sys
   
def write_square(v1,v2,v3,v4):
   print "facet normal " + "1" + " " + "1" + " " + "1"
   print "outer loop"
   print "vertex" + " " + str(v1[0]) + " " + str(v1[1]) + " " + str(v1[2])
   print "vertex" + " " + str(v2[0]) + " " + str(v2[1]) + " " + str(v2[2])
   print "vertex" + " " + str(v3[0]) + " " + str(v3[1]) + " " + str(v3[2])
   print "endloop"
   print "endfacet"
   print "facet normal " + "1" + " " + "1" + " " + "1"
   print "outer loop"
   print "vertex" + " " + str(v1[0]) + " " + str(v1[1]) + " " + str(v1[2])
   print "vertex" + " " + str(v3[0]) + " " + str(v3[1]) + " " + str(v3[2])
   print "vertex" + " " + str(v4[0]) + " " + str(v4[1]) + " " + str(v4[2])
   print "endloop"
   print "endfacet"
   
def write_triangle(v1,v2,v3):
   print "facet normal " + "1" + " " + "1" + " " + "1"
   print "outer loop"
   print "vertex" + " " + str(v1[0]) + " " + str(v1[1]) + " " + str(v1[2])
   print "vertex" + " " + str(v2[0]) + " " + str(v2[1]) + " " + str(v2[2])
   print "vertex" + " " + str(v3[0]) + " " + str(v3[1]) + " " + str(v3[2])
   print "endloop"
   print "endfacet"


argvs = sys.argv
filename = argvs[1]
if argvs[2]=="left":
   out="left"
elif argvs[2]=="right":
   out="right"
else:
   out="all"
   
### calc max_height   
f = open(filename,"r")
k=0
max_height=0

while True:
   l = f.readline()
   if "facet normal" in l:
      f.readline()
      v1 = [float(s) for s in f.readline().split()[1:4]]
      v2 = [float(s) for s in f.readline().split()[1:4]]
      v3 = [float(s) for s in f.readline().split()[1:4]]
      f.readline()
      f.readline()
      k=k+1
      if 1<= k and k<= 255*2*255:
         max_height = max([max_height,v1[1],v2[1],v3[1]])
      if k==1:
         x1=v1[0]
         z1=v1[2]
      elif k==255*2:
         x2=v3[0]
      elif k==255*2*127:
         z2=v2[2]
         y5=v3[1]
      elif k==255*2*126+1:
         y2=v2[1]
      elif k==255*2*255:
         z3=v2[2]
      elif k==255*2*255+1:
         y=v2[1]
   elif k>255*2*255+1:
      break
f.close()

### set value
h_offset=max_height*1.2
w_offset=10
edge=3

### writeout stl
f = open(filename,"r")
k=0

print "solid 3d_data_reverse"
while True:
   l = f.readline()
   if "facet normal" in l:
      k=k+1
      f.readline()
      v1 = [float(s) for s in f.readline().split()[1:4]]
      v2 = [float(s) for s in f.readline().split()[1:4]]
      v3 = [float(s) for s in f.readline().split()[1:4]]
      f.readline()
      f.readline()
      #起伏
      if (out=="all" or out=="left") and 0< k and k<= 255*2*127:
         write_triangle([v2[0],v2[1],v2[2]-w_offset],[v1[0],v1[1],v1[2]-w_offset],[v3[0],v3[1],v3[2]-w_offset])
      elif (out=="all" or out=="right") and 255*2*127< k and k<= 255*2*255:
         write_triangle([v2[0],v2[1],v2[2]+w_offset],[v1[0],v1[1],v1[2]+w_offset],[v3[0],v3[1],v3[2]+w_offset])
      #横壁の奥1
      elif (out=="all" or out=="left") and 255*2*255< k and k<= 255*2*255+127*3 and k%3!=0:
         write_triangle([v2[0],v2[1],v2[2]-w_offset],[v1[0],v1[1],v1[2]-w_offset],[v3[0],v3[1],v3[2]-w_offset])
         if k%3==1:
            write_triangle([x1-edge,y,z2-w_offset],[v1[0],y,v1[2]-w_offset],[v3[0],y,v3[2]-w_offset])
      elif (out=="all" or out=="right") and 255*2*255+127*3< k and k<= 255*2*255+255*3 and k%3!=0:
         write_triangle([v2[0],v2[1],v2[2]+w_offset],[v1[0],v1[1],v1[2]+w_offset],[v3[0],v3[1],v3[2]+w_offset])
         if k%3==1:
            write_triangle([x1-edge,y,z2+w_offset],[v1[0],y,v1[2]+w_offset],[v3[0],y,v3[2]+w_offset])
      #横壁の手前1
      elif (out=="all" or out=="left") and 255*2*255+255*3< k and k<= 255*2*255+255*3+127*3 and k%3!=0:
         write_triangle([v2[0],v2[1],v2[2]-w_offset],[v1[0],v1[1],v1[2]-w_offset],[v3[0],v3[1],v3[2]-w_offset])
         if k%3==1:
            write_triangle([x2+edge,y,z2-w_offset],[v2[0],y,v2[2]-w_offset],[v1[0],y,v1[2]-w_offset])
      elif (out=="all" or out=="right") and 255*2*255+255*3+127*3< k and k<= 255*2*255+255*3+255*3 and k%3!=0:
         write_triangle([v2[0],v2[1],v2[2]+w_offset],[v1[0],v1[1],v1[2]+w_offset],[v3[0],v3[1],v3[2]+w_offset])
         if k%3==1:
            write_triangle([x2+edge,y,z2+w_offset],[v2[0],y,v2[2]+w_offset],[v1[0],y,v1[2]+w_offset])
      #横壁の横1
      elif (out=="all" or out=="left") and 255*2*255+255*3+255*3< k and k<= 255*2*255+255*3+255*3+255*3 and k%3!=0:
         write_triangle([v2[0],v2[1],v2[2]-w_offset],[v1[0],v1[1],v1[2]-w_offset],[v3[0],v3[1],v3[2]-w_offset])
         if k%3==1:
            write_triangle([x1,y,z1-w_offset-edge],[v2[0],y,v2[2]-w_offset],[v1[0],y,v1[2]-w_offset])
      elif (out=="all" or out=="right") and 255*2*255+255*3+255*3+255*3< k and k<= 255*2*255+255*3+255*3+255*3+255*3 and k%3!=0:
         write_triangle([v2[0],v2[1],v2[2]+w_offset],[v1[0],v1[1],v1[2]+w_offset],[v3[0],v3[1],v3[2]+w_offset])
         if k%3==1:
            write_triangle([x1,y,z3+w_offset+edge],[v2[0],y,v2[2]+w_offset],[v3[0],y,v3[2]+w_offset])
      #断面1
      if (out=="all" or out=="left") and 255*2*126 < k and k <= 255*2*127:
         if k%2 == 0:
            write_square([v2[0],v2[1],v2[2]-w_offset],[v3[0],v3[1],v3[2]-w_offset],[v3[0],max_height,v3[2]-w_offset],[v2[0],max_height,v2[2]-w_offset])
            write_triangle([v3[0],max_height,v3[2]-w_offset],[x2,max_height+1,z2-w_offset],[v2[0],max_height,v2[2]-w_offset])
      if (out=="all" or out=="right") and 255*2*127 < k and k <= 255*2*128 :
         if k%2 == 1:
            write_square([v3[0],v3[1],v3[2]+w_offset],[v1[0],v1[1],v1[2]+w_offset],[v1[0],max_height,v1[2]+w_offset],[v3[0],max_height,v3[2]+w_offset])
            write_triangle([v1[0],max_height,v1[2]+w_offset],[x2,max_height+1,z2+w_offset],[v3[0],max_height,v3[2]+w_offset])
   elif not l:
      break
   else:
      pass
f.close()
'''
 z1   z2   z3
1 _________
 |    |    |
 |    |    |
 |____|____|
2
(height) 
 
'''

if (out=="all" or out=="left"):
   #上壁の奥1
   v1=[x1-edge,y,z1-w_offset-edge]
   v2=[x1,y,z1-w_offset]
   v3=[x1-edge,y,z2-w_offset]
   write_triangle(v1,v2,v3)
   v1=[x1-edge,y,z1-w_offset-edge]
   v2=[x1,y,z1-w_offset-edge]
   v3=[x1,y,z1-w_offset]
   write_triangle(v1,v2,v3)
if (out=="all" or out=="right"):
   #上壁の奥2
   v1=[x1-edge,y,z3+w_offset+edge]
   v2=[x1,y,z3+w_offset]
   v3=[x1-edge,y,z2+w_offset]
   write_triangle(v3,v2,v1)
   v1=[x1-edge,y,z3+w_offset+edge]
   v2=[x1,y,z3+w_offset+edge]
   v3=[x1,y,z3+w_offset]
   write_triangle(v3,v2,v1)
if (out=="all" or out=="left"):
   #上壁の手前1
   v1=[x2,y,z1-w_offset]
   v2=[x2+edge,y,z1-w_offset-edge]
   v3=[x2+edge,y,z2-w_offset]
   write_triangle(v1,v2,v3)
   v1=[x2,y,z1-w_offset]
   v2=[x2,y,z1-w_offset-edge]
   v3=[x2+edge,y,z1-w_offset-edge]
   write_triangle(v1,v2,v3)
if (out=="all" or out=="right"):
   #上壁の手前2
   v1=[x2,y,z3+w_offset]
   v2=[x2+edge,y,z3+w_offset+edge]
   v3=[x2+edge,y,z2+w_offset]
   write_triangle(v3,v2,v1)
   v1=[x2,y,z3+w_offset]
   v2=[x2,y,z3+w_offset+edge]
   v3=[x2+edge,y,z3+w_offset+edge]
   write_triangle(v3,v2,v1)
if (out=="all" or out=="left"):
   #上壁の横1
   v1=[x2,y,z1-w_offset]
   v2=[x1,y,z1-w_offset-edge]
   v3=[x2,y,z1-w_offset-edge]
   write_triangle(v1,v2,v3)
if (out=="all" or out=="right"):
   #上壁の横2
   v1=[x2,y,z3+w_offset]
   v2=[x1,y,z3+w_offset+edge]
   v3=[x2,y,z3+w_offset+edge]
   write_triangle(v3,v2,v1)
if (out=="all" or out=="left"):
   #横壁の奥1
   v1=[x1-edge,y,z2-w_offset]
   v2=[x1-edge,h_offset,z2-w_offset]
   v3=[x1-edge,h_offset,z1-w_offset-edge]
   v4=[x1-edge,y,z1-w_offset-edge]
   write_square(v1,v2,v3,v4)
if (out=="all" or out=="right"):   
   #横壁の奥2
   v1=[x1-edge,y,z2+w_offset]
   v2=[x1-edge,h_offset,z2+w_offset]
   v3=[x1-edge,h_offset,z3+w_offset+edge]
   v4=[x1-edge,y,z3+w_offset+edge]
   write_square(v4,v3,v2,v1)
if (out=="all" or out=="left"):
   #横壁の手前1
   v1=[x2+edge,y,z1-w_offset-edge]
   v2=[x2+edge,h_offset,z1-w_offset-edge]
   v3=[x2+edge,h_offset,z2-w_offset]
   v4=[x2+edge,y,z2-w_offset]
   write_square(v1,v2,v3,v4)
if (out=="all" or out=="right"):
   #横壁の手前2
   v1=[x2+edge,y,z3+w_offset+edge]
   v2=[x2+edge,h_offset,z3+w_offset+edge]
   v3=[x2+edge,h_offset,z2+w_offset]
   v4=[x2+edge,y,z2+w_offset]
   write_square(v4,v3,v2,v1)
if (out=="all" or out=="left"):   
   #横壁の横1
   v1=[x1-edge,y,z1-w_offset-edge]
   v2=[x1-edge,h_offset,z1-w_offset-edge]
   v3=[x1,y,z1-w_offset-edge]
   write_triangle(v1,v2,v3)
   v1=[x1,y,z1-w_offset-edge]
   v2=[x1-edge,h_offset,z1-w_offset-edge]
   v3=[x2,y,z1-w_offset-edge]
   write_triangle(v1,v2,v3)
   v1=[x2,y,z1-w_offset-edge]
   v2=[x1-edge,h_offset,z1-w_offset-edge]
   v3=[x2+edge,y,z1-w_offset-edge]
   write_triangle(v1,v2,v3)
   v1=[x2+edge,y,z1-w_offset-edge]
   v2=[x1-edge,h_offset,z1-w_offset-edge]
   v3=[x2+edge,h_offset,z1-w_offset-edge]
   write_triangle(v1,v2,v3)
if (out=="all" or out=="right"):
   #横壁の横2
   v1=[x1-edge,y,z3+w_offset+edge]
   v2=[x1-edge,h_offset,z3+w_offset+edge]
   v3=[x1,y,z3+w_offset+edge]
   write_triangle(v3,v2,v1)
   v1=[x1,y,z3+w_offset+edge]
   v2=[x1-edge,h_offset,z3+w_offset+edge]
   v3=[x2,y,z3+w_offset+edge]
   write_triangle(v3,v2,v1)
   v1=[x2,y,z3+w_offset+edge]
   v2=[x1-edge,h_offset,z3+w_offset+edge]
   v3=[x2+edge,y,z3+w_offset+edge]
   write_triangle(v3,v2,v1)
   v1=[x2+edge,y,z3+w_offset+edge]
   v2=[x1-edge,h_offset,z3+w_offset+edge]
   v3=[x2+edge,h_offset,z3+w_offset+edge]
   write_triangle(v3,v2,v1)
if (out=="all" or out=="left"):   
   #断面の奥1
   v1=[x1,y,z2-w_offset]
   v2=[x1-edge,h_offset,z2-w_offset]
   v3=[x1-edge,y,z2-w_offset]
   write_triangle(v1,v2,v3)
   v1=[x1,y,z2-w_offset]
   v2=[x1,y2,z2-w_offset]
   v3=[x1-edge,h_offset,z2-w_offset]
   write_triangle(v1,v2,v3)
   v1=[x1,y2,z2-w_offset]
   v2=[x1,max_height,z2-w_offset]
   v3=[x1-edge,h_offset,z2-w_offset]
   write_triangle(v1,v2,v3)
   v1=[x1,max_height,z2-w_offset]
   v2=[x1,max_height+1,z2-w_offset]
   v3=[x1-edge,h_offset,z2-w_offset]
   write_triangle(v1,v2,v3)
   v1=[x1,max_height+1,z2-w_offset]
   v2=[x1,h_offset,z2-w_offset]
   v3=[x1-edge,h_offset,z2-w_offset]
   write_triangle(v1,v2,v3)
if (out=="all" or out=="right"):   
   #断面の奥2
   v1=[x1,y,z2+w_offset]
   v2=[x1-edge,h_offset,z2+w_offset]
   v3=[x1-edge,y,z2+w_offset]
   write_triangle(v3,v2,v1)
   v1=[x1,y,z2+w_offset]
   v2=[x1,y2,z2+w_offset]
   v3=[x1-edge,h_offset,z2+w_offset]
   write_triangle(v3,v2,v1)
   v1=[x1,y2,z2+w_offset]
   v2=[x1,max_height,z2+w_offset]
   v3=[x1-edge,h_offset,z2+w_offset]
   write_triangle(v3,v2,v1)
   v1=[x1,max_height,z2+w_offset]
   v2=[x1,max_height+1,z2+w_offset]
   v3=[x1-edge,h_offset,z2+w_offset]
   write_triangle(v3,v2,v1)
   v1=[x1,max_height+1,z2+w_offset]
   v2=[x1,h_offset,z2+w_offset]
   v3=[x1-edge,h_offset,z2+w_offset]
   write_triangle(v3,v2,v1)
if (out=="all" or out=="left"):   
   #断面の手前1
   v1=[x2,y,z2-w_offset]
   v2=[x2+edge,h_offset,z2-w_offset]
   v3=[x2+edge,y,z2-w_offset]
   write_triangle(v3,v2,v1)
   v1=[x2,y,z2-w_offset]
   v2=[x2,y5,z2-w_offset]
   v3=[x2+edge,h_offset,z2-w_offset]
   write_triangle(v3,v2,v1)
   v1=[x2,y5,z2-w_offset]
   v2=[x2,max_height,z2-w_offset]
   v3=[x2+edge,h_offset,z2-w_offset]
   write_triangle(v3,v2,v1)
   v1=[x2,max_height,z2-w_offset]
   v2=[x2,max_height+1,z2-w_offset]
   v3=[x2+edge,h_offset,z2-w_offset]
   write_triangle(v3,v2,v1)
   v1=[x2,max_height+1,z2-w_offset]
   v2=[x2,h_offset,z2-w_offset]
   v3=[x2+edge,h_offset,z2-w_offset]
   write_triangle(v3,v2,v1)
if (out=="all" or out=="right"):
   #断面の手前2
   v1=[x2,y,z2+w_offset]
   v2=[x2+edge,h_offset,z2+w_offset]
   v3=[x2+edge,y,z2+w_offset]
   write_triangle(v1,v2,v3)
   v1=[x2,y,z2+w_offset]
   v2=[x2,y5,z2+w_offset]
   v3=[x2+edge,h_offset,z2+w_offset]
   write_triangle(v1,v2,v3)
   v1=[x2,y5,z2+w_offset]
   v2=[x2,max_height,z2+w_offset]
   v3=[x2+edge,h_offset,z2+w_offset]
   write_triangle(v1,v2,v3)
   v1=[x2,max_height,z2+w_offset]
   v2=[x2,max_height+1,z2+w_offset]
   v3=[x2+edge,h_offset,z2+w_offset]
   write_triangle(v1,v2,v3)
   v1=[x2,max_height+1,z2+w_offset]
   v2=[x2,h_offset,z2+w_offset]
   v3=[x2+edge,h_offset,z2+w_offset]
   write_triangle(v1,v2,v3)
if (out=="all" or out=="left"):   
   #底1 
   v1=[x1-edge,h_offset,z1-w_offset-edge]
   v2=[x1,h_offset,z2-w_offset]
   v3=[x1-edge,h_offset,z2-w_offset]
   write_triangle(v3,v2,v1)
   v1=[x1-edge,h_offset,z1-w_offset-edge]
   v2=[x2,h_offset,z2-w_offset]
   v3=[x1,h_offset,z2-w_offset]
   write_triangle(v3,v2,v1)
   v1=[x1-edge,h_offset,z1-w_offset-edge]
   v2=[x2+edge,h_offset,z2-w_offset]
   v3=[x2,h_offset,z2-w_offset]
   write_triangle(v3,v2,v1)
   v1=[x1-edge,h_offset,z1-w_offset-edge]
   v2=[x2+edge,h_offset,z1-w_offset-edge]
   v3=[x2+edge,h_offset,z2-w_offset]
   write_triangle(v3,v2,v1)
   
if (out=="all" or out=="right"):   
   #底2
   v1=[x1-edge,h_offset,z3+w_offset+edge]
   v2=[x1,h_offset,z2+w_offset]
   v3=[x1-edge,h_offset,z2+w_offset]
   write_triangle(v1,v2,v3)
   v1=[x1-edge,h_offset,z3+w_offset+edge]
   v2=[x2,h_offset,z2+w_offset]
   v3=[x1,h_offset,z2+w_offset]
   write_triangle(v1,v2,v3)
   v1=[x1-edge,h_offset,z3+w_offset+edge]
   v2=[x2+edge,h_offset,z2+w_offset]
   v3=[x2,h_offset,z2+w_offset]
   write_triangle(v1,v2,v3)
   v1=[x1-edge,h_offset,z3+w_offset+edge]
   v2=[x2+edge,h_offset,z3+w_offset+edge]
   v3=[x2+edge,h_offset,z2+w_offset]
   write_triangle(v1,v2,v3)
if (out=="all" or out=="left"):   
   ###凸
   v1=[x2,max_height+1,z2-w_offset]
   v2=[x2-1,max_height+1+(h_offset-max_height)/2,z2-w_offset+2]
   v3=[x1+1,max_height+1+(h_offset-max_height)/2,z2-w_offset+2]
   v4=[x1,max_height+1,z2-w_offset]
   write_square(v1,v2,v3,v4)
   
   v1=[x2-1,max_height+1+(h_offset-max_height)/2,z2-w_offset+2]
   v2=[x2,h_offset,z2-w_offset]
   v3=[x1,h_offset,z2-w_offset]
   v4=[x1+1,max_height+1+(h_offset-max_height)/2,z2-w_offset+2]
   write_square(v1,v2,v3,v4)
   
   v1=[x2-1,max_height+1+(h_offset-max_height)/2,z2-w_offset+2]
   v2=[x2,max_height+1,z2-w_offset]
   v3=[x2,h_offset,z2-w_offset]
   write_triangle(v1,v2,v3)
   
   v1=[x1+1,max_height+1+(h_offset-max_height)/2,z2-w_offset+2]
   v2=[x1,h_offset,z2-w_offset]
   v3=[x1,max_height+1,z2-w_offset]
   write_triangle(v1,v2,v3)
if (out=="all" or out=="right"):   
   ###凹
   v1=[x2,max_height+1,z2+w_offset]
   v2=[x2,max_height+1+(h_offset-max_height)/2,z2+w_offset+3]
   v3=[x1,max_height+1+(h_offset-max_height)/2,z2+w_offset+3]
   v4=[x1,max_height+1,z2+w_offset]
   write_square(v4,v3,v2,v1)
   
   v1=[x2,max_height+1+(h_offset-max_height)/2,z2+w_offset+3]
   v2=[x2,h_offset,z2+w_offset]
   v3=[x1,h_offset,z2+w_offset]
   v4=[x1,max_height+1+(h_offset-max_height)/2,z2+w_offset+3]
   write_square(v4,v3,v2,v1)
   
   v1=[x2,max_height+1+(h_offset-max_height)/2,z2+w_offset+3]
   v2=[x2,max_height+1,z2+w_offset]
   v3=[x2,h_offset,z2+w_offset]
   write_triangle(v3,v2,v1)
   
   v1=[x1,max_height+1+(h_offset-max_height)/2,z2+w_offset+3]
   v2=[x1,h_offset,z2+w_offset]
   v3=[x1,max_height+1,z2+w_offset]
   write_triangle(v3,v2,v1)
if (out=="all" or out=="left"):   
   #断面埋め1
   v1=[x2,max_height+1,z2-w_offset]
   v2=[x1,max_height+1,z2-w_offset]
   v3=[x1,max_height,z2-w_offset]
   write_triangle(v1,v2,v3)
if (out=="all" or out=="right"):   
   #断面埋め2
   v1=[x2,max_height+1,z2+w_offset]
   v2=[x1,max_height+1,z2+w_offset]
   v3=[x1,max_height,z2+w_offset]
   write_triangle(v3,v2,v1)

print "endsolid"

