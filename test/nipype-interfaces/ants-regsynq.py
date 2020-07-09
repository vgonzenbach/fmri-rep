"""Test a quicker registration of option from the ANTs interface.
"""
from nipype.interfaces.ants import RegistrationSynQuick

#Get template path per your system
from nipype.interfaces.fsl import Info
template_path = Info.standard_image('MNI152_T1_1mm_brain.nii.gz')

reg = RegistrationSynQuick()
reg.inputs.fixed_image = template_path
reg.inputs.moving_image = 'test-data/haxby2001/subj2/anat.nii.gz'
reg.inputs.num_threads = 2
reg.cmdline

%timeit reg.run()  
