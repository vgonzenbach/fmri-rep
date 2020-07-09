"""Test ANTs registration interface
    Parameters values are taken from: https://github.com/ANTsX/ANTs/wiki/Anatomy-of-an-antsRegistration-call
    Note: Runtime is quite long with current parameters
"""
from nipype.interfaces.ants import Registration

#Get template path in your system
from nipype.interfaces.fsl import Info
template_path = Info.standard_image('MNI152_T1_1mm_brain.nii.gz')

reg = Registration()
reg.inputs.fixed_image = template_path
reg.inputs.moving_image = 'test-data/haxby2001/subj2/anat.nii.gz'

# Choose Mutual Information as the metric and relevant metric inputs
reg.inputs.metric = ['MI', 'MI', 'CC']
reg.inputs.metric_weight = [1]*3
reg.inputs.radius_or_number_of_bins = [32]*3
reg.inputs.sampling_strategy = ['Regular', 'Regular', None]
reg.inputs.sampling_percentage = [0.25, 0.25, None]

# Choose the type of transforms and in what order to implement
reg.inputs.transforms = ['Rigid', 'Affine', 'SyN']

# Parameters are (GradientStep, updateFieldVarianceInVoxelSpace, totalFieldVarianceInVoxelSpace)
reg.inputs.transform_parameters = [(0.1,), (0.1,), (0.1, 3.0, 0.0)]

# Specify where to save results
reg.output_warped_image = 'out-ants-reg/anat_norm.nii.gz'

# Choose size of kernels for smoothing
reg.inputs.smoothing_sigmas = [[3,2,1,0],[3,2,1,0],[3,2,1,0]]

# Choose factors for
reg.inputs.shrink_factors = [[8, 4, 2, 1],[8, 4, 2, 1],[8, 4, 2, 1]]

# Choose maximum number of iterations
reg.inputs.number_of_iterations = [[1000,500,250,100],[1000,500,250,100],[1000,500,250,100]]

# Other parameters
reg.inputs.float = False
reg.inputs.dimension = 3

reg.cmdline
reg.run()
