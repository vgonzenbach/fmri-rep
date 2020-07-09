"""Test low-iteration 2-stage (Affine, SyN) registration to save computations
    Parameters are chosen from John Muschelli's extrantsr::reg_write default parameters
    
    May upgrade with access to computational resources
"""
from nipype.interfaces.ants import Registration

reg = Registration()

from nipype.interfaces.fsl import Info
template_path = Info.standard_image('MNI152_T1_1mm_brain.nii.gz')

reg = Registration()
reg.inputs.fixed_image = template_path
reg.inputs.moving_image = 'test-data/haxby2001/subj2/anat.nii.gz'

# Choose the type of transforms and in what order to implement
reg.inputs.transforms = ['Affine', 'SyN']
reg.inputs.metric = ['Mattes', 'Mattes']
reg.inputs.metric_weight = [1]*2
reg.inputs.radius_or_number_of_bins = [32]*2
reg.inputs.sampling_strategy = ['Regular', None]
reg.inputs.sampling_percentage = [0.2, 1]

# Parameters are (GradientStep, updateFieldVarianceInVoxelSpace, totalFieldVarianceInVoxelSpace)
reg.inputs.transform_parameters = [(0.25,), (0.2, 3.0, 0.0)]

# Specify where to save results
reg.output_warped_image = 'output/ants-reg/anat_reg_econ.nii.gz'

# Choose shinking factors and kernel size per iteration
reg.inputs.number_of_iterations = [[2100,1200,1200,0],[40,20,0]]
reg.inputs.smoothing_sigmas = [[3,2,1,0],[2,1,0]]
reg.inputs.shrink_factors = [[4, 2, 2, 1],[4, 2, 1]]

# Other parameters
reg.inputs.float = False # Use double for more precision + speed
reg.inputs.dimension = 3

reg.cmdline

# Run the registration and time it
import time

tic = time.perf_counter()
reg.run()
toc = time.perf_counter()

print(f"Completed the process in {toc - tic:0.4f} seconds")
# Completed the process in 271.2817 seconds
