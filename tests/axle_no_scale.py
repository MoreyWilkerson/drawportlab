
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from drawportlab import SheetFormat
from drawportlab import draw


c = canvas.Canvas("axle_noscale.pdf",pagesize =(17*inch, 11*inch)) #page format

matrix = ["projectno.", "customer", "location", "project" ]
Page = "S-1"
Title = "title"
SheetFormat.sheetformat(c, Page,Title, matrix)   

## axle properties---------------------------------------------
s1x = 2.25 * inch #Section 1 x size
s2x = 3.5 * inch #Section 2 x size
s3x = 4 * inch #Section 3 x size
s4x = 2.25 * inch #Section 4 x size

s1y = 2 * inch #Section 1 Diameter
s2y = 3.5 * inch #Section 2 Diameter
s3y = 2.5 * inch #Section 3 Diameter
s4y = 2 * inch #Section 4 Diameter

maxy = max(s1y,s2y,s3y, s4y)
axlelen = s1x + s2x + s3x + s4x

##----------------------------------------------------------------------

U_x    = 1 * inch  # Origin _ x dimension
U_y    = 4.5  * inch  # Origin _ y dimension  

##drawing goes here -----------------------------------------------------
Sqy = maxy

locx = 0 * inch
locy = (Sqy - (s1y))/2
c.rect(U_x + locx, U_y + locy, s1x, s1y) #section 1

locx = locx + s1x 
locy = (Sqy - (s2y))/2
c.rect(U_x + locx, U_y + locy, s2x, s2y) #section 2

locx = locx + s2x  
locy = (Sqy - (s3y))/2
c.rect(U_x + locx, U_y + locy, s3x, s3y) #section 3

locx = locx + s3x  
locy = (Sqy - (s4y))/2
c.rect(U_x + locx, U_y + locy, s4x, s4y) #section 4

locx = locx + s3x  

c.setFont("Times-Roman", 16)  #set font size for dims 

## dimensions, first view  -----------------------------------------------------
locx = 0 * inch
sp = .5 * inch
ndg = 3 #nudge some pixels
leny = (Sqy - (s1y))/2
draw.centDim(c, U_x + locx, U_y - sp, U_x + locx + s1x, 
                        U_y - sp, draw.fracking2d(s1x/inch,'"')) #horz dim, S1
draw.centDim(c, U_x + locx + sp, U_y + leny + ndg, U_x + locx + sp, 
                U_y + leny + s1y- ndg , draw.fracking2d(s1y/inch,'"')) # vertical, segment 1
c.line(U_x + locx, U_y - sp-.125*inch,U_x + locx, U_y + leny - .125 * inch) 

locx = locx + s1x
leny = (Sqy - (s2y))/2
draw.centDim(c, U_x + locx, U_y - sp, U_x + locx + s2x , 
                    U_y - sp, draw.fracking2d(s2x/inch,'"')) #horizontal, segment 2
c.line(U_x + locx, U_y - sp-.25*inch,U_x + locx, U_y + leny - .125 * inch)
draw.centDim(c, U_x + locx + sp, U_y + leny, U_x + locx + sp, 
                U_y + leny + s2y - ndg, draw.fracking2d(s2y/inch,'"'))  # vertical, segment 2

locx = locx + s2x
draw.centDim(c, U_x + locx, U_y - sp, U_x + locx + s3x , 
                    U_y - sp, draw.fracking2d(s3x/inch,'"')) #horizontal, segment 3
c.line(U_x + locx, U_y - sp-.25*inch,U_x + locx, U_y + leny - .125 * inch)
leny = (Sqy - (s3y))/2
draw.centDim(c, U_x + locx + sp, U_y + leny + ndg, U_x + locx + sp, 
                U_y + leny + s3y - ndg, draw.fracking2d(s3y/inch,'"'))  # vertical, segment 3

locx = locx + s3x
draw.centDim(c, U_x + locx, U_y - sp, U_x + locx + s4x , 
                    U_y - sp, draw.fracking2d(s4x/inch,'"')) #horizontal, segment 4
c.line(U_x + locx, U_y - sp-.25*inch,U_x + locx, U_y + leny - .125 * inch)
leny = (Sqy - (s4y))/2
draw.centDim(c, U_x + locx + sp, U_y + leny + ndg, U_x + locx + sp, 
                U_y + leny + s4y - ndg, draw.fracking2d(s4y/inch,'"'))  # vertical, segment 4

locx = locx + s4x

c.line(U_x + locx, U_y - sp-.25*inch,U_x + locx, U_y + leny - .125 * inch)

##----------------------------------------------------------------------

#define dimensions and locxation of the detail 1. 
U_x    = U_x + 9.25 * inch  # Origin _ x dimension - pulls from previous detail.
U_y    = U_y # Origin _ y dimension  

x_cen = U_x + maxy/2
y_cen = U_y + maxy/2

# #c.circle(x_cen, y_cen, s1y*rat / 2 , fill=0) will never need 
# c.circle(x_cen, y_cen, s2y / 2 , fill=0)
# c.circle(x_cen, y_cen, s3y / 2 , fill=0)
# c.circle(x_cen, y_cen, s4y / 2 , fill=0)





c.showPage()
c.save()


