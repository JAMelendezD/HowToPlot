import numpy as np
import os
import argparse
from numpy import sin, cos


#cell size
xsize = 80.111
ysize = 80.111
zsize = 80.111

#arguments from terminal
parser = argparse.ArgumentParser()
parser.add_argument("plot", type=str, help="Your desire plot: sphere, curves, spiral, torus, klein8, kleinbot,shell,booster,dna")
parser.add_argument("llt", type=float, help="Lower limit theta")
parser.add_argument("ult", type=float, help="Upper limit theta")
parser.add_argument("llp", type=float, help="Lower limit phi")
parser.add_argument("ulp", type=float, help="Upper limit phi")
parser.add_argument("grid", type=int, help="Resolution for new equations maximum is 300")
parser.add_argument("scale", type=int, help="Factor that rescales the coordinates minimum 50")
parser.add_argument("r", type=str, help="Should be one or a function of T (theta) and P (Phi)")
parser.add_argument("x", type=str, help="Insert the equation for x as a function of T (theta) and P (Phi)")
parser.add_argument("y", type=str, help="Insert the equation for x as a function of T (theta) and P (Phi)")
parser.add_argument("z", type=str, help="Insert the equation for x as a function of T (theta) and P (Phi)")
args = parser.parse_args()

plot = args.plot

if args.ult > args.ulp:
	factor = args.scale/args.ult
else:
	factor = args.scale/args.ulp


if plot == 'sphere':
	grid = args.grid
	area = grid*grid
	p = np.linspace(args.llp,args.ulp,grid)
	t = np.linspace(args.llt,args.ult,grid)
	P,T = np.meshgrid(p, t)
	r = factor
	x = r*cos(P)*sin(T)
	y = r*sin(P)*sin(T)
	z = r*cos(T)

if plot == 'dna':
	grid = args.grid
	area = grid*grid
	p = np.linspace(args.llp,args.ulp,grid)
	t = np.linspace(args.llt,args.ult,grid)
	P,T = np.meshgrid(p, t)
	r = factor
	x = r*cos(P)*cos(T)
	y = r*sin(T)*cos(P)
	z = r*T

if plot == 'torus':
	grid = args.grid
	area = grid*grid
	p = np.linspace(args.llp,args.ulp,grid)
	t = np.linspace(args.llt,args.ult,grid)
	P,T = np.meshgrid(p, t)
	r = factor
	x = r*(2+cos(P))*cos(T)
	y = r*(2+cos(P))*sin(T)
	z = r*sin(P)

if plot == 'curves':
	grid = args.grid
	area = grid*grid
	p = np.linspace(args.llp,args.ulp,grid)
	t = np.linspace(args.llt,args.ult,grid)
	P,T = np.meshgrid(p, t)
	r = factor*(2+sin(7*P+5*T))
	x = r*cos(P)*sin(T)
	y = r*sin(P)*sin(T)
	z = r*cos(T)

if plot == 'spiral':
	grid = args.grid
	area = grid*grid
	p = np.linspace(args.llp,args.ulp,grid)
	t = np.linspace(args.llt,args.ult,grid)
	P,T = np.meshgrid(p, t)
	r = factor*(sin(4*P)**3+cos(2*P)**3+sin(6*T)**2+cos(6*T)**4)
	x = r*sin(P)*cos(T)
	y = r*cos(P)
	z = r*sin(T)*sin(P)

if plot == 'kleinbot':
	grid = args.grid
	area = grid*grid
	p = np.linspace(args.llp,args.ulp,grid)
	t = np.linspace(args.llt,args.ult,grid)
	P,T = np.meshgrid(p, t)
	r = factor
	x = r*(-2/15*cos(P)*(3*cos(T)-30*sin(P)+90*cos(P)**4*sin(P)-60*cos(P)**6*sin(P)+5*cos(P)*sin(P)*cos(T)))
	y = r*(-1/15*sin(P)*(3*cos(T)-3*cos(P)**2*cos(T)-48*cos(P)**4*cos(T)+48*cos(P)**6*cos(T)-60*sin(P)+5*cos(P)*sin(P)*cos(T)-5*cos(P)**3*sin(P)*cos(T)-80*cos(P)**5*sin(P)*cos(T)+80*cos(P)**7*sin(P)*cos(T)))
	z = r*(3/15*(3+5*cos(P)*sin(P))*sin(T))

if plot == 'klein8':
	grid = args.grid
	area = grid*grid
	p = np.linspace(args.llp,args.ulp,grid)
	t = np.linspace(args.llt,args.ult,grid)
	P,T = np.meshgrid(p, t)
	r = factor
	x = r*cos(T)*(2+cos(T/2)*sin(P)-sin(T/2)*sin(2*P))
	y = r*sin(T)*(2+cos(T/2)*sin(P)-sin(T/2)*sin(2*P))
	z = r*(sin(T/2)*sin(P)+cos(T/2)*sin(2*P))

if plot == 'shell':
	grid = args.grid
	area = grid*grid
	p = np.linspace(args.llp,args.ulp,grid)
	t = np.linspace(args.llt,args.ult,grid)
	P,T = np.meshgrid(p, t)
	r = factor
	x = r*(T*sin(T)*cos(P))
	y = r*(T*cos(T)*cos(P))
	z = r*(T*sin(P))

if plot == 'booster':
	grid = args.grid
	area = grid*grid
	p = np.linspace(args.llp,args.ulp,grid)
	t = np.linspace(args.llt,args.ult,grid)
	P,T = np.meshgrid(p, t)
	r = factor
	x = r*(cos(P)-cos(T))
	y = r*(sin(P)-sin(T))
	z = r*(T)

if plot == 'new':
	grid = args.grid
	area = grid*grid
	p = np.linspace(args.llp,args.ulp,grid)
	t = np.linspace(args.llt,args.ult,grid)
	P,T = np.meshgrid(p, t)
	r = factor*eval('%s' % args.r)
	x = factor*eval('%s' % args.x)
	y = factor*eval('%s' % args.y)
	z = factor*eval('%s' % args.z)

contador1 = 0

#function
with open('parametric.pdb', 'w') as f:
    f.write("TITLE     Function\n")
    f.write("CRYST1  {}  {}   {}  90.00  90.00  90.00\n".format(xsize,ysize,zsize))
    for j in range(len(y)):
        contador1+=1
        contador2 = 1
        for i in range(len(x)):
            f.write('ATOM {:6d} C    XXX A   1     {:07.3f} {:07.3f} {:07.3f}  1.00  {:03.2f}\n'.format(area - contador1*grid +contador2,x[i][j],y[i][j],z[i][j],abs(np.min(z)/factor)+(z[i][j]/factor)))
            contador2+=1
    f.write("END")

os.system('pymol showparam.pml')