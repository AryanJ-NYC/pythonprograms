# circles_28 - NEXT
# FOR 13 VARIABLES of map2_4.py

import math
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import random
import time


def perp(vxin, vyin):
    if vxin == 0:
        vxp = -np.sign(vyin) * vyin
        vyp = 0.
    else:
        vyp = np.sign(vxin) * 1.0 / np.sqrt(1 + vyin ** 2 / vxin ** 2)
        vxp = -np.sign(vyin) * abs(vyin * vyp / vxin)
    return vxp, vyp


# -------------------------------------------------------------------------

# NEED TO CHANGE THIS LATER
# numc = 8
cin = [[0, 3, -6, 3, 3, 3, 0, 0], [3, 0, 0, 0, 0, 0, 0, 3], [-3, 0, 0, 0, 0, 0, 0, -3], [3, 0, 0, 0, 0, 0, 0, 0], [3, 0, 0, 0, 0, 0, 0, 0], [3, 0, 0, 0, 0, 0, 3, 0], [0, 0, 0, 0, 0, 3, 0, 0], [0, 3, -6, 0, 0, 0, 0, 0]]
zin = [13.31636449,   6.65819304,   0.,   3.33333333, 3.33333333, 6.65819304, 3.33332235, 3.33332235]


def clockplot(cin, zin, programnamein):
    # set up only for THESE names
    vname = ['1-NODAL (+/-)',
             '2-POSITIVE memory',
             '3-NEGATIVE memory',
             '4-POSITIVE expect',
             '5-NEGATIVE expect',
             '6-Coop/Compete',
             '7-Conlf Manag',
             '8-Fairness',
             '9-Access',
             '10-Security',
             '11-Higher Authority',
             '12-Peace Vision',
             '13-Shared Ident'
             ]
    numc = len(cin)
    if numc > 13:
        print('\nSORRY, I cannot make a clockplot for more than 13 variables')
        return
    else:
        pass

    # plot the variables
    radius = 1.
    pi = np.pi
    xp = [0 for i in range(numc)]
    yp = [0 for i in range(numc)]
    for i in range(numc):
        angle = i * pi / 6.5
        xp[i] = radius * np.sin(angle)
        yp[i] = radius * np.cos(angle)
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
        if zin[i] > 0:
            varc = 'g'
        # else:
        #             varc='g'
        plt.plot(xpa[i], ypa[i], symbol, ms=msz, c=varc, markeredgewidth=2.0,
                 markerfacecolor='none', markeredgecolor=varc)
        if i != 0:
            plt.text(xpa[i] + .1, ypa[i] - 0.07, vname[i])
        else:
            plt.text(xpa[i] + .2, ypa[i] + 0.07, vname[i])
    plt.axis([-1.25, 1.25, -1.25, 1.25])
    plt.axis('off')

    # plot the connections
    cina = np.array(cin)
    xcon = [0, 0]
    ycon = [0, 0]
    for i in range(numc):
        for j in range(numc):
            if np.abs(cina[j][i]) > .1:
                width = abs(cina[j][i]) / 2.
                # print ('\nwidth= ',width)
                dxp = (xpa[j] - xpa[i]) * 0.9
                dyp = (ypa[j] - ypa[i]) * 0.9
                dxshift, dyshift = perp(dxp, dyp)
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