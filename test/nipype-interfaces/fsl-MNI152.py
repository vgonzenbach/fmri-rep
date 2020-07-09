from nipype.interfaces.fsl import Info

Info.standard_image()
template_path = Info.standard_image('MNI152_T1_1mm_brain.nii.gz')
