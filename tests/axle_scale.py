
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from drawportlab import SheetFormat
from drawportlab import draw


c = canvas.Canvas("axle_scale.pdf",pagesize =(17*inch, 11*inch)) #page format

matrix = ["projectno.", "customer", "location", "project" ]
Page = "S-1"
Title = "title"
SheetFormat.sheetformat(c, Page,Title, matrix)   

## axle properties---------------------------------------------
s1x = 2.25 #Section 1 x size
s2x = 3.5  #Section 2 x size
s3x = 4    #Section 3 x size
s4x = 2.25 #Section 4 x size

s1y = 2   #Section 1 Diameter
s2y = 3.5 #Section 2 Diameter
s3y = 2.5 #Section 3 Diameter
s4y = 2   #Section 4 Diameter

maxy = max(s1y,s2y,s3y, s4y)
axlelen = s1x + s2x + s3x + s4x

##----------------------------------------------------------------------

Sqxmax = 10 * inch  # Best case x dimension
Sqymax = 5  * inch  # Best case y dimensionlineends
U_x    = 1 * inch  # Origin _ x dimension
U_y    = 4.5  * inch  # Origin _ y dimension  

rat = Sqxmax/axlelen # real/page
Sqx = axlelen * rat
Sqy = maxy * rat

[Sqx,Sqy,rat] = draw.optsize(Sqx, Sqy, rat, Sqxmax,Sqymax)

##drawing goes here -----------------------------------------------------

locx = 0 * inch * rat
locy = (Sqy - (s1y * rat))/2
c.rect(U_x + locx, U_y + locy, s1x * rat, s1y * rat) #section 1

locx = locx + s1x * rat
locy = (Sqy - (s2y * rat))/2
c.rect(U_x + locx, U_y + locy, s2x * rat, s2y * rat) #section 2

locx = locx + s2x * rat  
locy = (Sqy - (s3y * rat))/2
c.rect(U_x + locx, U_y + locy, s3x * rat, s3y * rat) #section 3

locx = locx + s3x * rat 
locy = (Sqy - (s4y * rat))/2
c.rect(U_x + locx, U_y + locy, s4x * rat, s4y * rat) #section 4

locx = locx + s3x * rat  

c.setFont("Times-Roman", 16)  #set font size for dims 

## dimensions, first view  -----------------------------------------------------

locx = 0 * inch * rat
sp = .5 * inch
ndg = 3 #nudge some pixels
leny = (Sqy - (s1y * rat))/2
draw.centDim(c, U_x + locx, U_y - sp, U_x + locx + s1x * rat, 
                        U_y - sp, draw.fracking2d(s1x,'"')) #horz dim, S1
draw.centDim(c, U_x + locx + sp, U_y + leny + ndg, U_x + locx + sp, 
                U_y + leny + s1y * rat- ndg , draw.fracking2d(s1y,'"')) # vertical, segment 1
c.line(U_x + locx, U_y - sp-.125*inch,U_x + locx, U_y + leny - .125 * inch) 

locx = locx + s1x  * rat
leny = (Sqy - (s2y * rat))/2
draw.centDim(c, U_x + locx, U_y - sp, U_x + locx + s2x  * rat, 
                    U_y - sp, draw.fracking2d(s2x,'"')) #horizontal, segment 2
c.line(U_x + locx, U_y - sp-.25*inch,U_x + locx, U_y + leny - .125 * inch)
draw.centDim(c, U_x + locx + sp, U_y + leny, U_x + locx + sp, 
                U_y + leny + s2y * rat - ndg, draw.fracking2d(s2y,'"'))  # vertical, segment 2

locx = locx + s2x * rat
draw.centDim(c, U_x + locx, U_y - sp, U_x + locx + s3x * rat, 
                    U_y - sp, draw.fracking2d(s3x,'"')) #horizontal, segment 3
c.line(U_x + locx, U_y - sp-.25*inch,U_x + locx, U_y + leny - .125 * inch)
leny = (Sqy - (s3y * rat))/2
draw.centDim(c, U_x + locx + sp, U_y + leny + ndg, U_x + locx + sp, 
                U_y + leny + s3y  * rat- ndg, draw.fracking2d(s3y,'"'))  # vertical, segment 3

locx = locx + s3x * rat
draw.centDim(c, U_x + locx, U_y - sp, U_x + locx + s4x  * rat, 
                    U_y - sp, draw.fracking2d(s4x,'"')) #horizontal, segment 4
c.line(U_x + locx, U_y - sp-.25*inch,U_x + locx, U_y + leny - .125 * inch)
leny = (Sqy - (s4y * rat))/2
draw.centDim(c, U_x + locx + sp, U_y + leny + ndg, U_x + locx + sp, 
                U_y + leny + s4y * rat - ndg, draw.fracking2d(s4y,'"'))  # vertical, segment 4

locx = locx + s4x * rat

c.line(U_x + locx, U_y - sp-.25*inch,U_x + locx, U_y + leny - .125 * inch)

##----------------------------------------------------------------------

#define dimensions and locxation of the detail 1. 
U_x    = U_x + Sqxmax + .5 * inch  # Origin _ x dimension - pulls from previous detail.
U_y    = U_y # Origin _ y dimension  

x_cen = U_x + (maxy * rat)/2
y_cen = U_y + (maxy) * rat/2

#c.circle(x_cen, y_cen, s1y*rat / 2 , fill=0) will never need 
c.circle(x_cen, y_cen, s2y * rat/ 2 , fill=0)
c.circle(x_cen, y_cen, s3y * rat/ 2 , fill=0)
c.circle(x_cen, y_cen, s4y * rat/ 2 , fill=0)

c.showPage()
c.save()


