* [What is this?](README.md#what-is-this)
* [Software roll-call](README.md#installations-and-dependencies)
* [Quick start](README.md#quick-start)


## What is this?
* This a baysian-stacking code that fits radio luminosity functions (RLF) to optical/NIR selected radio data (including undetected radio data). 
* The code uses and extends [bayestack](https://github.com/jtlz2/bayestack).
* This is done by extracting radio fluxes at the position of optical/NIR source population. Then bining the fluxes into flux bins (the code is not very sensitive to any sensible bin size, we tried linear bins, log bins, etc) which includes negative bins (as some flux densities are dominated by noise). Luminosity functions models that are assumed/expected to describe the radio luminosity function are converted into flux bins and compared to the flux bins. The fitting takes into account the radio noise of the date which can be fitted or fixed. 

## installations and dependencies
* At the moment the code is written in python 2.7
* The code requries basic python models; matplotlib numpy, scipy, os, sys, time, glob, [cosmocalc](https://cxc.harvard.edu/contrib/cosmocalc)
* The fitting is done with pymultinest. There are various methods to install pymultimest, through [pip](https://johannesbuchner.github.io/PyMultiNest/install.html), through [anaconda](https://anaconda.org/conda-forge/multinest) and [directly](http://johannesbuchner.github.io/pymultinest-tutorial/install.html) on a linux/mac/windows machine.

## Quick start
Assuming all the installation is done, 
1. The first step is to prepare the optical/NIR data (which is breifly explained in data section and fully explained in the [paper](http://arxiv.org/abs/2012.09797).
2. edit the settings for the fit in bayestack_setting file. The most essential varibles to set are:
 *  ```outdir``` this is the directory where the output will be saved into
 *  ```modelFamily``` is the model being fitted to the data.
 * ```floatNoise``` if set to ```True``` then the noise will be fitted (with proirs ```{SURVEY_NOISE*0.2,SURVEY_NOISE*2}```). if False, then the noise will be set to ```SURVEY_NOISE``` 
* ```WhichRedshiftSlice``` is the redshift bin being used. 1 refers to z_med=0.32 (corresponding to cos_data/data_cos_s1.txt) and 10 refers to z_med=3.44 (corresponding to cos_data/data_cos_s10.txt)

4. Finally run the code using  ```bayestack.py bayestack_settings```


