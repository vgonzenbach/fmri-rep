"""Test FSL's Brain Extraction Interface"""

from nipype.interfaces.fsl import BET
bet = BET()

bet.inputs.in_file = 'test-data/haxby2001/subj2/anat.nii.gz'
bet.inputs.out_file = 'output-fsl-bet/anat_bet.nii.gz'
bet.cmdline
bet.run()
