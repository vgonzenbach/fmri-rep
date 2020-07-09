"""Test ANTs' N4BiasFieldCorrection Interface"""
from nipype.interfaces.ants import N4BiasFieldCorrection

n4 = N4BiasFieldCorrection()

n4.inputs.input_image = 'test-data/haxby2001/subj2/anat.nii.gz'
n4.inputs.save_bias = True
n4.inputs.dimension = 3
n4.inputs.output_image = 'output/ants-n4/anat_corrected.nii.gz'
n4.inputs.bias_image = 'output/ants-n4/anat_bias.nii.gz'
n4.cmdline

# Run and time it
import time
tic = time.perf_counter()
n4.run()
toc = time.perf_counter()

print(f"Completed the process in {toc - tic:0.4f} seconds")

