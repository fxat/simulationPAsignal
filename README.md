# Simulation of a photo acoustical [PA] signal excitation

This simulation illustrates how a photoacoustic signal is produced.
Furthermore it shows us how a real, measureable signal shall look like if the conditions of thermal and stress confinement are fullfilled. 

## Spherical-source solution and point detector

The starting point is, the solution of the [photoacoustic equation](https://en.wikipedia.org/wiki/Photoacoustic_imaging#General_equation) for a absorbing spherical object with a given radius ![R_s](https://render.githubusercontent.com/render/math?math=R_s), that is homogeneously heated by a delta pulse. For details go to e.g. [Master thesis
Grueneisen relaxation photoacoustic microscopy with optical ultrasonic detection](https://github.com/fxat/Master_thesis__GR-PAM_and_OUSD/blob/master/thesis/main.pdf).
The propagating parts of this formula can be displayed as the following

![p(z,t) = \frac{z-c_s t}{2z} p_0(-z+c_s t) + \frac{z-c_s t}{2z} p_0(z-c_s t)](https://render.githubusercontent.com/render/math?math=p(z%2Ct)%20%3D%20%5Cfrac%7Bz-c_s%20t%7D%7B2z%7D%20p_0(-z%2Bc_s%20t)%20%2B%20%5Cfrac%7Bz-c_s%20t%7D%7B2z%7D%20p_0(z-c_s%20t))

![z](https://render.githubusercontent.com/render/math?math=z)...Distance source <-> detector [m]  
![c_s](https://render.githubusercontent.com/render/math?math=c_s)...Speed of sound in water [m/s]  
![p_0](https://render.githubusercontent.com/render/math?math=p_0)...Initial pressure rise [Pa]  

which results in a N-shaped pulse

![](https://github.com/fxat/Master_thesis__GR-PAM_and_OUSD/blob/master/thesis/02_principles_of_photoacoustics/images/nShape.png)

Excited with a gaussian shaped laserpulse and detected with a ultrasonic detector with finite bandwidth and a defined center frequency the measureable pulse looks like this

![](https://github.com/fxat/Master_thesis__GR-PAM_and_OUSD/blob/master/thesis/02_principles_of_photoacoustics/images/timeSphericalDet.png)

****
## Startup

runSim.py starts the simulation and states the simulation process.

## Extention possibilities

* Simulation of 
  * different sensor bandwidths and center frequencies
  * multible target sizes 
  * pulselengths of the laser
  
* Implementation of a more complex heating funciton

****

### License
This project is licensed under the GNU GPLv3 License - see the [LICENSE](https://github.com/fxat/simulationPAsignal/blob/master/LICENSE) file for details

### Contact

franz.taffner@yahoo.de
