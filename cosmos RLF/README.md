## What is this?
* This a baysian-stacking code that fits radio luminosity functions (RLF) to optical/NIR selected radio data (including undetected radio data)
* The code uses and extends [bayestack]{https://github.com/jtlz2/bayestack} 

Assuming all the installation is done, the first step is to extract the optical/NIR data.

2. Run the cosmos_sf.py file which selects galaxies and saves them into different files according to their redshifts
3. Run flux_extract.py to extract the flux-densities from the different redshifts
4. run binner_settings_lf.py to bin the flux-densities
5. edit the bayestack_setting file to point to the correct files
6. run bayestack.py bayestack_settings (preffeabley the one in the server_code.. folder)