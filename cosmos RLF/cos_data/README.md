## This is folder contains the data used in the this work.

## The describtion of the optical/NIR data is fully explained in the [paper](http://arxiv.org/abs/2012.09797). Below is a technical discription of how the data is prepared.

1. Run ```$python cosmos_sf.py``` This applies the galaxies selection and saves them into different files according to their redshifts. 
* The selection includes limiting the data to the central 2 deg square which leads to a minor cut in the data RA >149.4
* K_s<=24.5 #average 5sigma magnitude limit for UltraVista
* M*< M*_comp #stellar mass selection. 
* 0.1<z<0.4 > data_s1.txt
* 0.4<z<0.6 > data_s2.txt
* 0.6<z<0.8 > data_s3.txt
* ...
* 2.5<z<3.2 > data_s9.txt
* 3.2<z<4.0 > data_s10.txt

2. With optical data selected, the next step is to extract the radio flux densities.
```
$ python flux_extract.py 1 #where 1 refers to the 0.1<z<0.4 redshift bin
```
3. run 
```
$python binner.py 1 binner_settings_lf.py
``` 
