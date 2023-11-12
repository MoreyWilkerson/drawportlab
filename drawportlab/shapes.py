"""
Shapes.py - general steel shapes for drawing. 

@author: Morey 
"""

import math
from reportlab.lib.units import inch


def angle(c,U_x,U_y,x,y,t):
  
     p = c.beginPath()
     p.moveTo(U_x,U_y)
     p.lineTo(U_x+x,U_y)#right
     p.lineTo(U_x+x,U_y-y) #up
     p.lineTo(U_x+x-t,U_y-y+.5*t)# back and down
     p.lineTo(U_x+x-t,U_y-1.5*t)
     p.lineTo(U_x+x-1.5*t,U_y-t)
     p.lineTo(U_x+.5*t,U_y-t)
     p.lineTo(U_x,U_y)
     p.close()
     c.drawPath(p,fill=0)
     
def wf(c,U_x,U_y,x,y,tf,tw):
     p = c.beginPath()
     p.moveTo(U_x,U_y)
     p.lineTo(U_x+x,U_y)#right
     p.lineTo(U_x+x,U_y+tf)#Up
     p.lineTo(U_x+x-x/2+tw/2,U_y+tf)#Left
     p.lineTo(U_x+x-x/2+tw/2,U_y+y-tf)#Up
     p.lineTo(U_x+x,U_y+y-tf)#right
     p.lineTo(U_x+x,U_y+y)#up
     p.lineTo(U_x,U_y+y)#left
     p.lineTo(U_x,U_y+y-tf)#down
     p.lineTo(U_x+x/2-tw/2,U_y+y-tf)#right
     p.lineTo(U_x+x/2-tw/2,U_y+tf)#down
     p.lineTo(U_x,U_y+tf)#left
     p.lineTo(U_x,U_y) #down
     p.close()
     c.drawPath(p,fill=0)
     
def rail(c,U_x,U_y,rat): ## this is a typical 30# rail.
    
    p = c.beginPath()
    p.moveTo(U_x+0.06*rat,U_y+0*rat)
    p.lineTo(U_x+3.065*rat,U_y+0*rat)  #node 2
    p.lineTo(U_x+3.125*rat,U_y+0.06*rat)  #node 3
    p.lineTo(U_x+3.125*rat,U_y+0.1228*rat)  #node 4
    p.lineTo(U_x+3.0785*rat,U_y+0.1813*rat)  #node 5
    p.lineTo(U_x+1.9414*rat,U_y+0.4438*rat)  #node 6
    p.lineTo(U_x+1.8067*rat,U_y+0.526*rat)  #node 6a 
    p.lineTo(U_x+1.7481*rat,U_y+0.6724*rat)  #node 7
    p.lineTo(U_x+1.7481*rat,U_y+2.1088*rat)  #node 8
    p.lineTo(U_x+1.8067*rat,U_y+2.2553*rat)  #node 8a
    p.lineTo(U_x+1.9414*rat,U_y+2.3374*rat)  #node 9
    p.lineTo(U_x+2.3578*rat,U_y+2.4335*rat)  #node 10
    p.lineTo(U_x+2.4062*rat,U_y+2.4944*rat)  #node 11
    p.lineTo(U_x+2.4062*rat,U_y+2.8003*rat)  #node 12
    p.lineTo(U_x+2.3197*rat,U_y+3.0163*rat)  #node 12A
    p.lineTo(U_x+2.1079*rat,U_y+3.1125*rat)  #node 13
    p.lineTo(U_x+1.017*rat,U_y+3.1125*rat)  #node 12
    p.lineTo(U_x+0.8053*rat,U_y+3.0163*rat)  #node 12A
    p.lineTo(U_x+0.7187*rat,U_y+2.8003*rat)  #node 11
    p.lineTo(U_x+0.7187*rat,U_y+2.4944*rat)  #node 10
    p.lineTo(U_x+0.7671*rat,U_y+2.4335*rat)  #node 9
    p.lineTo(U_x+1.1835*rat,U_y+2.3374*rat)  #node 8
    p.lineTo(U_x+1.3183*rat,U_y+2.2553*rat)  #node 8a
    p.lineTo(U_x+1.3768*rat,U_y+2.1088*rat)  #node 7
    p.lineTo(U_x+1.3768*rat,U_y+0.6724*rat)  #node 6
    p.lineTo(U_x+1.3183*rat,U_y+0.526*rat)  #node 6a
    p.lineTo(U_x+1.1835*rat,U_y+0.4438*rat)  #node 5
    p.lineTo(U_x+0.0464*rat,U_y+0.1813*rat)  #node 4
    p.lineTo(U_x+0*rat,U_y+0.1228*rat)  #node 3
    p.lineTo(U_x+0*rat,U_y+0.06*rat)  #node 2
    p.lineTo(U_x+0.06*rat,U_y+0*rat)  #node 1

    p.close()

    c.drawPath(p,fill=1)             

def fillet(c,x1,y1,x2,y2,quad): # does a fillet. warning: only works on 90 degree fillets.
     #based on the arc command in reportlab, which is extremely Jank. play around with it to figure out the reasoning behind this section. 
     #this may be inefficient. it can be done in fewer lines. to bad! 
     if quad not in (1,2,3,4):
          raise ValueError("invalid input for quad (quadrant): must be 1,2,3, or 4")
     
     if quad == 1:
          if x1 < x2: # if (x1,y1) are at 90 and (x2,y2) are at 0, flip  
               (x1, y1), (x2, y2) = (x2, y2), (x1, y1)
          #set up arc. 
          flt = abs(x2-x1) # radius of fillet
          ax1 = x2 - flt  # bottom left corner coords, for arc command.
          ay1 = y1 - 2*flt
          c.setStrokeColorRGB(1,1,1)
          c.setFillColorRGB(1,1,1)
          c.rect(ax1 +flt + .03*inch,ay1+flt + .03*inch,flt,flt,fill = 1) # this is jank. makes inside white 
          c.setStrokeColorRGB(0,0,0)
          c.setFillColorRGB(0,0,0)
          c.arc(ax1, ay1, ax1 + 2*flt, ay1 + 2 * flt, startAng = 0,extent = 90) 
 
     elif quad == 2:
          if x1 < x2: # if (x1,y1) are at 180 and (x2,y2) are at 90, flip  
               (x1, y1), (x2, y2) = (x2, y2), (x1, y1)
          #set up arc. 
          flt = abs(x2-x1) # radius of fillet
          ax1 = x2  # bottom left corner coords, for arc command.
          ay1 = y1 - 2*flt
          c.setStrokeColorRGB(1,1,1)
          c.setFillColorRGB(1,1,1)
          c.rect(ax1 - .03*inch,ay1+flt + .03*inch,flt,flt,fill = 1) # this is jank. makes inside white 
          c.setStrokeColorRGB(0,0,0)
          c.setFillColorRGB(0,0,0)
          c.arc(ax1, ay1, ax1 + 2*flt, ay1 + 2 * flt, startAng = 90,extent = 90) 
    
     elif quad == 3:
          if x1 > x2: # if (x1,y1) are at 270 and (x2,y2) are 180, flip  
               (x1, y1), (x2, y2) = (x2, y2), (x1, y1)
          #set up arc. 
          flt = abs(x2 - x1) # radius of fillet
          ax1 = x1 
          ay1 = y1 # bottom left corner, for arc command.
          c.setStrokeColorRGB(1,1,1)
          c.setFillColorRGB(1,1,1)
          c.rect(ax1-.03*inch,ay1-.03*inch,flt,flt,fill = 1) # this is jank. makes inside white 
          c.setStrokeColorRGB(0,0,0)
          c.setFillColorRGB(0,0,0)
          
          c.arc(ax1, ay1, ax1 + 2*flt, ay1 + 2 * flt, startAng = 180,extent = 90) 

     elif quad == 4:
          if x1 > x2: # if (x1,y1) are at 360 and (x2,y2) are at 270, flip  
               (x1, y1), (x2, y2) = (x2, y2), (x1, y1)
          #set up arc. 
          flt = abs(x2-x1) # radius of fillet
          ax1 = x1 - flt  # bottom left corner coords, for arc command.
          ay1 = y1
          c.setStrokeColorRGB(1,1,1)
          c.setFillColorRGB(1,1,1)
          c.rect(ax1 + flt + .03*inch,ay1-.03*inch,flt,flt,fill = 1) # this is jank. makes inside white 
          c.setStrokeColorRGB(0,0,0)
          c.setFillColorRGB(0,0,0)
          c.arc(ax1, ay1, ax1 + 2*flt, ay1 + 2 * flt, startAng = 270,extent = 90) 