#!/usr/bin/env python

"""
Execute this code as

mpirun -np 4 ./bayestack.py bayestack_settings.py

"""

import os
import pymultinest
from bayestack_settings import *
from bayestackClasses import countModel

#-------------------------------------------------------------------------------

def main():

    settingsf='bayestack_settings'
    expt=countModel(modelFamily,nlaws,settingsf,dataset,binStyle,floatNoise)

    try:
        os.mkdir(outdir)
    except OSError:
        pass

    # Run multinest
    pymultinest.run(expt.loglike,expt.logprior,expt.nparams,\
                    resume=RESUME,verbose=True,\
                    multimodal=multimodal,max_modes=max_modes,write_output=True,\
                    n_live_points=n_live_points,\
                    evidence_tolerance=evidence_tolerance,\
                    mode_tolerance=-1e90,seed=SEED_SAMP,max_iter=max_iter,\
                    importance_nested_sampling=do_INS,\
                    outputfiles_basename=os.path.join(outdir,outstem),\
                    init_MPI=False)


    return 0

#-------------------------------------------------------------------------------

if __name__ == '__main__':

    ret=main()
    sys.exit(ret)

