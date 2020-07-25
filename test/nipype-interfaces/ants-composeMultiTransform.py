"""Droped from pipeline. Replaced by ApplyTransforms"""
from nipype.interfaces.ants import ComposeMultiTransform
from nipype.interfaces.fsl import Info

compose_transf = ComposeMultiTransform()
compose_transf.inputs.dimension = 3
compose_transf.inputs.reference_image = Info.standard_image('MNI152_T1_1mm.nii.gz')

compose_transf.inputs.transforms = ['transform1InverseWarp.nii.gz', 'transform1Warp.nii.gz']

compose_transf.output_image = 'singletransform.nii.gz'
`