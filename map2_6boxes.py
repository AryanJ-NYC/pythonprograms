import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy import stats
import numpy as np
import random
import time
from boxes_4 import *

def filein(filename):
    """Reads in a file
    :param filename: File to be read
    """
    xin = open(filename).read().splitlines()
    numlines = len(xin)
    return xin, numlines

def fileout(filename, filedata):
    """Writes to file
    :param filename: File to write to
    :param filedata: Data to be written to file
    """
    f2 = open(filename,'w')
    f2.write(filedata)
    f2.close()

def getxy(filename):
    data, numlines = filein(filename)
    x = []  # '0' for i in range(numlines)]
    y = []  # '0' for i in range(numlines)]
    for i in range(numlines):
        xline = data[i]
        xline2 = xline.split('\t')
        xline2[-1] = xline2[-1].replace('\n', '')
        # print ('\nxline2',xline2)

        # ASK DR. LIEBOVITCH ABOUT 0 AND 1
        x.append(eval(xline2[0]))  # [i] = eval(xline2[0])
        y.append(eval(xline2[1]))  # [i] = eval(xline2[1])
    return x, y, numlines

def getx(filename):
    """TODO
    Insert Dr. Liebovitch's doctring here
    :param filename: Filename to getx
    """
    data, numlines = filein(filename)
    #  print ('\ndata\n',data,'\nlines',numlines)
    x = [] # x=['0' for i in range(numlines)]
    for i in range(numlines):
        data[i] = data[i].replace('\n', '')
        x.append(eval(data[i]))
    return x, numlines

def getxn(filename):
    data, numlines = filein(filename)
    dataline = []  # '0' for i in range(numlines)]
    for i in range(numlines):
        # appends every line of data into dataline
        # dataline is now a 2D array
        y = data[i].split('\t')
        y[-1] = y[-1].replace('\n', '')
        dataline.append(y)

    # print ('\n\nascii-input',dataline)
    xdata = dataline[:]

    for i in range(numlines):
        line_length = len(dataline[i])
        for j in range(line_length):
            if xdata[i][j] != '':
                xdata[i][j] = eval(xdata[i][j])
            else:
                xdata[i][j] = None
    # print ('dataline',dataline)
    # print ('xdata',xdata)
    return xdata, numlines

def lslin(invars,invar):
    # Called after asked to change parameters
    # TODO ASK DR. LIEBOVITCH FOR DESCRIPTIVE VARIABLE/METHOD NAMES
    print('\ncurrent value of {} is {}'.format(invars, invar))
    outvars = input('\nchange to (def=no change)')
    if outvars == '':
        return invar
    else:
        return eval(outvars)

def generate_filenames():
    """Generates file names from user's digit input
    :return: tuple of four file names
    """
    # give it just a number n, will find files cn.txt, bn.txt, mn.txt, icn.txt
    fast = input('\nONLY NUMBER n and I will find cn.txt, etc. (#/a, Def=a)')
    if fast.isdigit():
        file_name_c = 'c' + fast + '.txt'
        file_name_b = 'b' + fast + '.txt'
        file_name_m = 'm' + fast + '.txt'
        file_name_ic = 'ic' + fast + '.txt'
    else:
        # TODO Perhaps write "Don't include .txt" ???
        # Detect extension or add if needed
        filename = input('\nfilename for array c [I will add .txt]=  ')
        file_name_c = filename + '.txt'

        filename = input('\nfilename for array b [I will add .txt]=  ')
        file_name_b = filename + '.txt'

        filename = input('\nfilename for array m [I will add .txt]=  ')
        file_name_m = filename + '.txt'

        filename = input('\nfilename for array IC [I will add .txt]=  ')
        file_name_ic = filename + '.txt'
    return file_name_b, file_name_c, file_name_ic, file_name_m

def print_file_arrays(ca, ba, ma, ica):
    print('\nca = ', ca)
    print('\nba = ', ba)
    print('\nma = ', ma)
    print('\nic = ', ica)

def get_plots(ba, ca, delta_time, ica, ma, numdata):
    """Euler inegration"""
    # OK now start the integration
    # fix +/- RESERVOIRS NEVER < 0
    ica[1] = max(ica[1], 0.)
    ica[2] = max(ica[2], 0.)
    xolda = ica
    tt = 0
    t = [0. for i in range(numdata)]
    z = np.array([ica for i in range(numdata)])  # NOTE: changed ic to ica HEREß

    for i in range(1, numdata):
        mtanh = np.tanh(z[i - 1])
        cterm = np.dot(ca, mtanh)
        dx = delta_time * (ma * z[i - 1] + ba + cterm)
        #    print ('\nz[i-1]',z[i-1])
        #    print ('\nma*z[i-1],ba, ca * mtanh, dx','\n',ma*z[i-1],ba, ca * mtanh, dx,'\n\n')
        tt += delta_time
        t[i] = tt
        z[i] = z[i - 1] + dx
        z[i][1] = max(z[i][1], 0.0)  # the + reservoir is NEVER negative
        z[i][2] = max(z[i][2], 0.0)  # the - reservoir is NEVER negative
        z[i][3] = max(z[i][3], 0.0)  # the + future is NEVER negative
        z[i][4] = max(z[i][4], 0.0)  # the - future is NEVER negative

    return t, z

def animate(i): 
    i = i * step

    # get plots for current i value
    x_plot1, y_plot1 = (t[:i], z[:i, 0])
    x_plot2, y_plot2 = (t[:i], z[:i, 1])
    x_plot3, y_plot3 = (t[:i], z[:i, 2])
    x_plot4, y_plot4 = (t[:i], z[:i, 3:numc])

    # clear lines
    ax1.clear()

    # replot
    ax1.plot(x_plot1, y_plot1, color='navy', linewidth='6')
    ax1.plot(x_plot2, y_plot2, color='greenyellow', linewidth='4')
    ax1.plot(x_plot3, y_plot3, color='hotpink', linewidth='4')
    ax1.plot(x_plot4, y_plot4)

    # redraw, update axis scale
    plt.draw()

    return ax1,

tt = 0. 
step = 100
numdata = 30000
delta_time = .001
param_in = 'used data from files'

file_name_b, file_name_c, file_name_ic, file_name_m = generate_filenames()  # get the files

c, numc = getxn(file_name_c)
b, numb = getx(file_name_b)
m, numm = getx(file_name_m)
ic, numic = getx(file_name_ic)

# check for consistency
if numc**3 != numb * numm * numic:
    print("\nFATAL WARNING - input issue - numbers c, b, m, ic don't match")

# make arrays (NOT matrices) and print
ca, ba, ma, ica = np.array(c), np.array(b), np.array(m), np.array(ic)

print_file_arrays(ca, ba, ma, ica)

change = input('\nWant to CHANGE parameters (y / n, def = n)')

if change == 'y' or change == 'Y':
    c, b, m, ic = lslin('c', c), lslin('b', b), lslin('m', m), lslin('ic', ic)
    ca, ba, ma, ica = np.array(c), np.array(b), np.array(m), np.array(ic)
    print('/n/nNEW PARAMETER VALUES ARE: ')
    print_file_arrays(ca, ba, ma, ica)
    param_in = input('\nNOTE changes here! ')

t,z = get_plots(ba, ca, delta_time, ica, ma, numdata)
print("plot is ready")

figure = plt.figure()
ax1 = figure.add_subplot(111)

# init animation
frames = numdata / step
anim = animation.FuncAnimation(figure, animate, frames=int(frames), interval=0, blit=True, repeat=False)

# resize graph to fit title
box = ax1.get_position()
ax1.set_position([box.x0, box.y0 - box.height * 0.05, box.width, box.height * 0.9])

# generate title
x_start = ica
x_final = z[-1]
localtime = time.asctime(time.localtime(time.time()))
program_name = 'map2_6boxes.py   ' + localtime
param1 = '\n   input files =  {}    {}    {}    {}'.format(file_name_c, file_name_b, file_name_m, file_name_ic)
param2 = '\nx_start = {}    delta_time = {}    var colors=ngp-bgrcmyk\nx_final={}'\
    .format(str(ica), str(delta_time), str(x_final))
param4 = '\n' + param_in
title = program_name + param1 + param4 + param2

# set title and show
plt.suptitle(title, fontsize=10)
plt.show()