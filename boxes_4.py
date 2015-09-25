# boxes_3
# Making MAP2 like it is
# FOR 13 VARIABLES of map2_4.py

import math
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import random
import time


def perp2(vxin, vyin):
    if vxin == 0:
        vxp = -np.sign(vyin) * abs(vyin) * 2
        vyp = 0.
    else:
        vyp = np.sign(vxin) * 1.0 / np.sqrt(1 + vyin ** 2 / vxin ** 2)
        vxp = -np.sign(vyin) * abs(vyin * vyp / vxin)
    return vxp, vyp


# -------------------------------------------------------------------------

# NEED TO CHANGE THIS LATER
# numc=13
# ccin = [[0, 1.5, -5, 1.5, -5, 5, 5, 0, 0, 0, 0, 0, 0],[0.3, 0, 0, 0, 0, 0, 0, 1.5, 1.5, 0, 0, 0, 0], [-1.5, 0, 0, 0, 0, 0, 0, -0.3, -5, -1.5, 0, 0, 0], [0.3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1.5, 5], [-1.5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1.5], [0.3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0], [0.3, 0, 0, 0, 0, 0, 0, 0, 0, 0.3, 0, 0, 0], [0, 0.3, -1.5, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0], [0, 0.3, -5, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0], [0, 0, -0.3, 0, 0, 0, 0.3, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0.3, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0.3, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1.5, -5, 0, 0, 0, 0, 0, 0, 0, 0]]
# zzin=[ 10.69146502,   3.66661546,   0.        ,   6.04199951,
#          0.        ,   2.06698068,   0.37274724,   5.88836819,
#          5.88836819,   0.11879745,   0.32282218,   0.33332957,   #1.66664784]

def boxplot(cin, zin, programnamein):
    # set up only for THESE names
    vname = ['1-NODAL (+/-)', '2 +memory', '3 -memory', '4 +expect', '5 - expect', '6-Coop/Compete', '7-Conlf Manag',
             '8-Fairness', '9-Access', '10-Security', '11-Higher Authority', '12-Peace Vision', '13-Shared Ident']
    numc = len(cin)
    if numc > 13:
        print('\nSORRY, I cannot make a clockplot for more than 13 variables')
        return
    else:
        pass
    #

    # plot the variables
    radius = 1.
    pi = np.pi
    xp = ['0' for i in range(numc)]
    yp = ['0' for i in range(numc)]
    #     for i in range(numc):
    #         angle=i*pi/(6.5)
    #         xp[i]=radius*np.sin(angle)
    #         yp[i]=radius*np.cos(angle)
    #     print (xp)
    xp[0] = 1.
    xp[0] = 0.
    xp[1] = -.5
    xp[2] = -.5
    xp[3] = .5
    xp[4] = .5
    xp[5] = -.1
    xp[6] = 0.1
    xp[7] = -1.
    xp[8] = -1.
    xp[9] = -0.5
    xp[10] = 0.
    xp[11] = 0.6
    xp[12] = 1.

    yp[0] = 0.
    yp[1] = 0.25
    yp[2] = -0.25
    yp[3] = 0.25
    yp[4] = -0.25
    yp[5] = 0.5
    yp[6] = -0.5
    yp[7] = 0.35
    yp[8] = -0.35
    yp[9] = -0.6
    yp[10] = 1.
    yp[11] = 0.5
    yp[12] = 0.
    xpa = np.array(xp)
    ypa = np.array(yp)
    fig = plt.figure()
    # plt.axes([.1,.1,.7,.7])
    ax = fig.add_subplot(111)
    ax.set_aspect('equal')
    fig.patch.set_facecolor('white')
    ax.set_axis_bgcolor('white')
    # ax.arrow(0, 0, 0.5, 0.5, head_width=0.05, head_length=0.1, fc='k', ec='k')

    for i in range(numc):
        # Create circles (squares)
        maxz = max(np.abs(zin))
        msz = abs(zin[i]) * 40 / maxz
        if msz < 2:
            msz = 2.
        symbol = 'o'
        if i == 0:
            symbol = 's'
        varc = 'k'
        if zin[i] < 0:
            varc = 'r'
        if zin[i] > 0: varc = 'g'
        #         else:
        #             varc='g'
        plt.plot(xpa[i], ypa[i], symbol, ms=msz, c=varc, markeredgewidth=2.0,
                 markerfacecolor='none', markeredgecolor=varc)
        if xpa[i] < 0:
            halign = 'right'
        else:
            halign = 'left'
        if i != 0:
            #             plt.text(xpa[i]+.1,ypa[i]-0.07,vname[i])
            plt.text(xpa[i] + .1, ypa[i] + 0.07, vname[i], horizontalalignment=halign)
        else:
            plt.text(xpa[i] + .2, ypa[i] + 0.07, vname[i])

    plt.axis([-1.25, 1.25, -1.25, 1.25])
    plt.axis('off')

    # plot the connections
    cina = np.array(cin)
    xcon = ['0', '0']
    ycon = ['0', '0']
    for i in range(numc):
        for j in range(numc):
            if np.abs(cina[j][i]) > .1:
                width = abs(cina[j][i]) / 2.
                # print ('\nwidth= ',width)
                dxp = (xpa[j] - xpa[i]) * 0.9
                dyp = (ypa[j] - ypa[i]) * 0.9
                dxshift, dyshift = perp2(dxp, dyp)
                if cina[j][i] < 0:
                    test = 'r'
                else:
                    test = 'g'
                roff = 0.03
                xoff = dxshift * roff
                yoff = dyshift * roff
                xpastart = xpa[i] + xoff
                ypastart = ypa[i] + yoff
                # print ('\nijxy= ',i,j,xpastart, ypastart)

                ax.arrow(xpastart, ypastart, dxp, dyp, head_width=0.05,
                         head_length=0.1, fc=test, ec=test, linewidth=width)
                #     localtime = time.asctime( time.localtime(time.time()) )
                #     programname='peace_20.py   '+localtime
    pname = programnamein
    plt.title(pname, fontsize=12)
    plt.show()
    return

# THIS IS THE TEST RUN
# pprogamename='boxTEST'
# boxplot(ccin,zzin,pprogamename)
