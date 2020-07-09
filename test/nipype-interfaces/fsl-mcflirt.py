"""Test FSL's MCFLIRT for motion correction"""
from nipype.interfaces.fsl import MCFLIRT

mcflt = MCFLIRT()
mcflt.inputs.in_file = 'test-data/haxby2001/subj2/bold.nii.gz'
mcflt.inputs.cost = 'mutualinfo'
mcflt.inputs.out_file = 'output/fsl-mcflirt/functional_mcorr.nii.gz'
mcflt.inputs.save_mats = True
mcflt.inputs.save_plots = True
mcflt.cmdline

# How long to run?
%timeit mcflt.run()
