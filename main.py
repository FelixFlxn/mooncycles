#!/usr/bin/python
#coding=UTF-8
import time 
from math import pi, cos

def moonphase(now_time):
    # constants
    syn_moon_month = 29.530589 						# synodal length of moon cycle 

    # constants
    hist_fullmoon = 2018,9,25,6,1,36,0,0,1 			# base full-moon as struct time 
    moon_time = time.mktime(hist_fullmoon) 			# base full-moon - seconds since epoch 
    hist_fullmoon_days = moon_time/86400 			# base full-moon - days since epoch 
    now_days = now_time/86400 						# days since eval 
    days_since_hist_fullmoon = now_days - hist_fullmoon_days   # difference in days between base fullmoon and now 
    full_moons_since = days_since_hist_fullmoon/syn_moon_month # Number of full-moons that have passed since base full-moon 
    phase = round(full_moons_since,2) 				# rounded to 2 digits 
    phase = (phase-int(phase))						# trailing rest = % moon-phase 

    # calculate moon phase
    if phase == 0: phase=1
    if phase < 0.25:
        ptext="abnehmender Mond (drittes Viertel)" 
    elif phase == 0.25:
        ptext="abnehmender Halbmond (letztes Viertel)" 
    elif 0.25 < phase < 0.50:
        ptext="abnehmende Sichel" 
    elif phase == 0.50:
        ptext="Neumond" 
    elif 0.50 < phase < 0.75:
        ptext="zunehmende Sichel" 
    elif phase == 0.75:
        ptext="zunehmender Halbmond (erstes Viertel)" 
    elif 0.75 < phase < 1:
        ptext="zunehmender Mond (zweites Viertel)" 
    elif phase == 1:
        ptext = "Vollmond"
        
    return phase, ptext

def illumination(phase):
    #constants
    hmoonA = float(pi/2)                            # area of unit circle/2

    # calculate percentage of moon illuminated
    if phase < 0.5:
            s = cos(phase * pi * 2)
            ellipse = s * 1 * pi                    # Ellipsenfäche = Produkt der beiden Halbachsen * Pi 
            hEllA = ellipse / 2                     # Ellipse Area/2 (major half axis * minor half axis * pi)/2
            illA = hmoonA + hEllA                   # illuminated area of moon = Half moon area plus half Ellipse
    else:
            s = -cos(phase * pi *2)                 # minor half axis of ellipse
            ellipse = s * 1 * pi
            hEllA = ellipse / 2                     # Ellipse Area/2 (major half axis * minor half axis)/2
            illA = hmoonA - hEllA                   # illuminated area = Half moon area minus half Ellipse Area

    illumperc =  illA / pi * 100                    # illuminated area relative to full moon area (based on unit circle r=1)	
    illumperc = round(illumperc,1)
        
    return illumperc
    
if __name__ == '__main__':
    adesso = time.mktime(time.localtime())
    mtupel = moonphase(adesso)
    mphase = mtupel[0]
    mphase_text = mtupel[1]
    millum = illumination(mtupel[0])
    formatted_mphase = "{:1.2f}".format(mphase)
    formatted_millum = "{:1.1f}".format(millum)
    print("Phase numerisch: " + formatted_mphase + " , Mondphase: " + mphase_text + " , beleuchtete Oberfläche: " + formatted_millum)