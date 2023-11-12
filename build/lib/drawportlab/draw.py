# -*- coding: utf-8 -*-
"""
draw.py - general note taking on PDF 

@author: Morey 
"""
import math
from reportlab.lib.units import inch

#DRAW FUNCTIONS

def fracking(x): #takes float as input, returns ft & inches as string.
  xft=math.floor(x/12) #how many feet?
  xin=x-(xft*12) # how many inches?
  xin = round(.0625* round(float(xin)/.0625),4) #rounds to nearest sixteenth 
  xr=  math.floor(xin)
  base =16 #base of fraction
  xfr=(xin-xr)*16 # numerator of fraction
  for y in range(3):
      if xfr % 2 == 0: #can the numerator divide into the base? 
          xfr = xfr/2
          base = base/2
      else : break
  xfts = ""
  if xft != 0: xfts = str(int(xft)) + "' "
  if xfr == 0:
      x = xfts + str(int(xr))+'"'
      return x
  else :
      x = xfts+ str(int(xr)) +" " +str(int(xfr))+"/"+str(int(base))+'"'
      return x
  
def fracking2d(x, str= ""):#Returns string of 2 decimal places, + the string added
       x = "{:.2f}".format(x) + str
       return x

def optsize(Sqx, Sqy, rat, Sqxmax,Sqymax): #Change the dimensions to fit properly in the sections 
    ratc = 1 #how much is the ratio changing? 
    if Sqy > Sqymax: 
            ratc= Sqy/Sqymax # how much the ratio is changing
            rat = rat/ratc   # now change 
            Sqy = Sqymax     # reduce value to max value 
            Sqx = Sqx/ratc
    if Sqx > Sqxmax: 
            ratc= Sqx/Sqxmax # how much the ratio is changing
            rat = rat/ratc   # now change 
            Sqx = Sqxmax     # reduce value to max value 
            Sqy = Sqy/ratc
            
    return [Sqx,Sqy,rat]  
    
def lineends(c,x1,y1,x2,y2,n,fact = 1):#arrowheads at the the end of lines 
     # n can be 3 options. 1: arrow on one side.  2: arrow on both sides. 3: arrow on other,
     
     ffs = 1 
     if n == 3: 
         ffs = -1
     h=ffs * .0625*inch * fact #how far back to go
     b=.0625*inch/4 * fact#sides of arrow 
     
     if (x1-x2)== 0:
         slope = 90 
     else :
         slope =(y1-y2)/(x1-x2)
    
     hyp = math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
     theta=math.atan(slope)   
     if hyp <= h*2:
         h = -h
     #make new axis     
     p2x=-h*math.cos(theta)+b*math.sin(theta)
     p2y=-h*math.sin(theta)-b*math.cos(theta)
     p3x=-h*math.cos(theta)-b*math.sin(theta)
     p3y=-h*math.sin(theta)+b*math.cos(theta) 
     if slope == 90:
         p2x = b
         p3x = -b
         p2y = -h
         p3y = -h
     p = c.beginPath()
     p.moveTo(x1,y1)
     p.lineTo(x1-p2x,y1-p2y)
     p.lineTo(x1-p3x,y1-p3y)
     p.lineTo(x1,y1)
     p.close()
     c.drawPath(p,fill=1)
     if n==2 : 
         p = c.beginPath()
         p.moveTo(x2,y2)
         p.lineTo(x2+p2x,y2+p2y)
         p.lineTo(x2+p3x,y2+p3y)
         p.lineTo(x2,y2)
         p.close()
         c.drawPath(p,fill=1) 
         
def note (c, xm,ym,xb,yb,note): #its a note
    c.line(xm,ym,xb,yb-.025*inch)
    if xb >= xm:
        c.line(xb,yb-.025*inch, xb + c.stringWidth(note),yb-.025*inch)
        c.drawString(xb,yb,note)
        lineends(c,xm,ym,xb,yb-.025*inch,1)
    elif  xb < xm:
        lineends(c,xm,ym,xb,yb,3)
        c.line(xb,yb-.025*inch, xb - c.stringWidth(note),yb-.025*inch)
        c.drawRightString(xb,yb,note)   
         
def weldnote(c,xm,ym,xb,yb,size,field): # field: if zero, field weld not shown 
    c.setFillColorRGB(0,0,0)
    for x in range(len(xm)):
        c.line(xm[x],ym[x],xb,yb)
        lineends(c,xm[x],ym[x],xb,yb,1)
        
    c.line(xb,yb,xb+inch,yb)#horz
    c.line(xb+.5*inch,yb,xb+.5*inch,yb-.1875*inch)
    c.line(xb+.5*inch,yb-.1875*inch,xb+.6875*inch,yb)
    c.line(xb+inch,yb,xb+1.168*inch,yb-.168*inch)
    c.line(xb+inch,yb,xb+1.168*inch,yb+.168*inch)
    c.drawString(xb+1.125*inch,yb-3/72*inch,"E7018")
    c.drawRightString(xb+.4875*inch,yb-0.15*inch,size)
    if field ==1:
        c.line(xb,yb,xb,yb-.25*inch)
        p = c.beginPath()
        p.moveTo(xb,yb-.25*inch)
        p.lineTo(xb+.25*inch,yb-(.25+2.5/32)*inch)#right
        p.lineTo(xb,yb-(.25+5/32)*inch)#right
        p.lineTo(xb,yb-.25*inch)
        p.close()
        c.drawPath(p,fill=1)   
    
def centDim(c,x1,y1,x2,y2,dim): #places a dimension line spanning from [x1,y1] to [x2,y2]
    c.line(x1,y1,x2,y2)
    c.setStrokeColorRGB(0,0,0)
    c.setFillColorRGB(0,0,0)        
    lineends(c,x1,y1,x2,y2,2)
    c.setStrokeColorRGB(1,1,1) #TIME FOR DIMS 
    c.setFillColorRGB(1,1,1)
    c.rect((x1+(x2-x1)/2)-c.stringWidth(dim)/2,(y1+(y2-y1)/2-6/72*inch),c.stringWidth(dim),14/72*inch,fill=1) #changed .7/72 to 7/72. is it still working? 
    c.setStrokeColorRGB(0,0,0)
    c.setFillColorRGB(0,0,0)
    c.drawCentredString(x1+(x2-x1)/2,y1+(y2-y1)/2-.04*inch,dim)#mf Clear width        
    
def typDim(c,x1,y1,x2,y2,xstr,dim): #similar to centdim but allows you to locate dim - in progress


    c.line(x1,y1,x2,y2)
    c.setStrokeColorRGB(0,0,0)
    c.setFillColorRGB(0,0,0)    
    lineends(c,x1,y1,x2,y2,2)
    
    f=1 # is it to the left? 
    if xstr > x2: 
            c.line(x2,y2,xstr-.0625*inch,y2)    
    elif xstr < x1: 
            c.line(xstr+.0625*inch,y1,x1,y2)
            f= -1
    c.setStrokeColorRGB(1,1,1) #TIME FOR DIMS 
    c.setFillColorRGB(1,1,1)
    c.rect((xstr),(y1+(y2-y1)/2-6/72*inch),(f)*c.stringWidth(dim),12/72*inch,fill=1)
    c.setStrokeColorRGB(0,0,0)
    c.setFillColorRGB(0,0,0)
    c.drawString((xstr-((1-f)/2*c.stringWidth(dim))),y1+(y2-y1)/2-.04*inch,dim)#mf Clear width

def sectview(c,x1,y1,x2,y2,ori,str): #section view line from (x1,y1) to (x2,y2) 

    sp = .125 * inch
    if y1 == y2:
        if x1 > x2: # ensure X1 is furthest left on page
            (x1, y1), (x2, y2) = (x2, y2), (x1, y1)
        if ori == 1  : oriv = 1 
        elif ori == 2: oriv = -1
        else: 
             raise ValueError("sectview - ori (aka orientation) must be integer 1 or 2")
        c.setDash([6,3,15,3],0)
        c.line(x1-sp,y1,x2+sp,y2)  
        c.setDash([],0)

        c.line(x1,y1,x1,y1 - oriv * .5*inch ) # important - not the oriv changes the direction of this. 
        c.drawCentredString(x1,y1 - oriv * .625*inch,str)
        lineends(c,x1,y1,x1,y1 - oriv * .625*inch ,3,fact = 3)
        c.line(x2,y1,x2,y1 - oriv * .5*inch ) 
        c.drawCentredString(x2,y1 - oriv * .625*inch,str)
        lineends(c,x2,y1,x2,y1 - oriv * .5*inch ,3,fact = 3)
        

    
    else:
        raise ValueError("sectview - non-horizontal section views not in scope. consider making your own, apologies.")
    
def orsline(c,coord1,coord2,origin): # just a line, with origin translated [U_x,U_y], [x1,y1],[x2,y2]
    [U_x,U_y] = origin
    [x1,y1] = coord1
    [x2,y2] = coord2
    c.line(U_x + x1, U_y + y1, U_x + x2, U_y + y2)

def orsrect(c,coord1 ,dims,origin,x = 0): # just a rect,  with origin translated  
    [U_x,U_y] = origin
    [x1,y1] = coord1
    [width, height] = dims
    c.rect(U_x + x1, U_y + y1, width, height, fill = x )

def crossect(c,U_x,U_y,Sqx,Sqy,spd,ang): #makes a square box of diagonals. clear out the negative space to leave yourself with a crossection
    xe = .125 * inch 
    ye = Sqy
    xa = xe - Sqy * math.tan(ang)
    ya = 0


    while True:
        if xa < 0:# CASE 1
                xa = 0 
                ya = ye - xe * math.tan(ang)
        elif xa > 0 and xe < Sqx : # CASE 2 
            xa = xe - Sqy * math.tan(ang)
            ya = 0

        elif xe > Sqx :
            break        
        orsline(c,[xa,ya],[xe,ye],[U_x,U_y])        
        xe = xe + spd
        xa = xe - Sqy * math.tan(ang)
        ya = 0

    xa = xe - Sqy * math.tan(ang)
    ya = 0
    xe = Sqx
    while True: # CASE 3
        ye = (Sqx - xa) * math.tan(ang)
        orsline(c,[xa,ya],[xe,ye],[U_x,U_y])   
        xa = xa + spd
        if xa > Sqx :
            break  