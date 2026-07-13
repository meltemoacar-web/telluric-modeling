import numpy as np
from scipy.special import wofz
import matplotlib.pyplot as plt

#------------------------------------------------------------------------------------
def V(x, alpha, gamma):
    """
    Return the Voigt line shape at x with Lorentzian component HWHM gamma
    and Gaussian component HWHM alpha.

    """
    sigma = alpha / np.sqrt(2 * np.log(2))

    return (
        np.real(wofz((x + 1j * gamma) / sigma / np.sqrt(2)))
        / sigma
        / np.sqrt(2 * np.pi)
    )


figure, axes = plt.subplots(2,2)
alpha, gamma = 0.1, 0.1 

x = np.linspace(-0.8, 0.8, 1000)
y = V(x,alpha,gamma)

#This snippet of code was taken from https://scipython.com/books/book2/chapter-8-scipy/examples/the-voigt-profile/

#I used this code to graph the voigt profile. This is the model that represents a single spectral line (a general one) that has NOT been really contaminated or affected by anything.
#So it represents the "perfect" solar data that I don't have. In this program you'll see how added 'noise' (In correct context: telluric lines/contamination) will skew it's graph. 
#-------------------------------------------------------------------------------------

#For FWHM. (Full width half maxmimum stuff)
#Just comment out all of these if you don't want to get the points when you run this program
#Another comment at the bottom, where the code that plots these lines actually. Comment that out if you just want the lines gone to see the graphs itself. 
y_max = y.max()
y_max_half = y_max/2
print(y_max_half)

half_indices = []

for index, i in enumerate(y):

    if abs(i - y_max_half) <= 0.005:
        half_indices.append(index)

x_max_half=[]
for i in  half_indices:
    x_max_half.append(x[i])
print(x_max_half)


#Change these in order to change what the 'noise', basically this is how I created the contamination to skew the voigt profile. Showing how telluric lines will disrupt solar data...
peak_location = -0.8 + 1.6/1000 * 300         #center of the spike 
peak_height1 = 0.5                            #max height of spike
peak_height2=1                               
peak_width = 0.05                             #change width

y_noise1 = peak_height1 * np.exp(-0.5 * ((x - peak_location) / peak_width) ** 2)
peak_location = -0.8+1.6/1000 * 600
y_noise2 = peak_height2 * np.exp(-0.5 * ((x - peak_location) / peak_width) ** 2)


#plotting stuff, these are kind of useless now. 
#This was before I created subplots of the graph so this code can be disregarded. (Basically, this would show all 4 different graphs on 1 graph at once)

#plt.plot(x, y_noise1, label="Noise 1")
#plt.plot(x, y_noise2, label="Noise 2")
#plt.plot(x, y, label="Voigt")                     
#plt.plot(x, y + y_noise1 + y_noise2, label="Added") #added verison

#These are what creates the subplots. 
axes[0,0].plot(x,y, color="green")
axes[0,0].set_title("Voigt")

axes[0,1].plot(y_noise1, color="pink")
axes[0,1].set_title("Noise 1")

axes[1,0].plot(y_noise2, color="purple")
axes[1,0].set_title("Noise 2")

axes[1,1].plot(x,y + y_noise1 + y_noise2, color="blue")
axes[1,1].set_title("Added")

#Messing around with full-width, half-maximum stuff just on the simple voigt profile. 
#Can be commented out if you only want to see the graphs without any extra lines. 
for i in x_max_half:
    axes[0,0].axvline(i)

axes[0,0].axhline(y_max)
axes[0,0].axhline(y_max_half)

#plt.title("Voigt with contamination/test", color="purple")
plt.xlim(-0.8, 0.8)
#plt.legend()
plt.show()
