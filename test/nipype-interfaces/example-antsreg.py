from nipype.interfaces.ants import Registration

#Get template
from nipype.interfaces.fsl import Info
Info.standard_image()
template_path = Info.standard_image('MNI152_T1_1mm_brain.nii.gz')

reg = Registration()
reg.inputs.moving_image='test-data/haxby2001/subj2/anat.nii.gz'
reg.inputs.output_warped_image='output-example/anat_registered.nii.gz'
reg.inputs.args='--float'
reg.inputs.collapse_output_transforms=True
reg.inputs.fixed_image=template_path
reg.inputs.initial_moving_transform_com=True
reg.inputs.num_threads=2
reg.output_inverse_warped_image=True
reg.inputs.sigma_units=['vox']*3
reg.inputs.transforms=['Rigid', 'Affine', 'SyN']
reg.inputs.winsorize_lower_quantile=0.005
reg.inputs.winsorize_upper_quantile=0.995
reg.inputs.convergence_threshold=[1e-06]
reg.inputs.convergence_window_size=[10]
reg.inputs.metric=['MI', 'MI', 'CC']
reg.inputs.metric_weight=[1.0]*3
reg.inputs.number_of_iterations=[[1000, 500, 250, 100],
                                 [1000, 500, 250, 100],
                                 [100, 70, 50, 20]]
reg.inputs.radius_or_number_of_bins=[32, 32, 4]
reg.inputs.sampling_percentage=[0.25, 0.25, 1]
reg.inputs.sampling_strategy=['Regular',
                              'Regular',
                              'None']
reg.inputs.shrink_factors=[[8, 4, 2, 1]]*3
reg.inputs.smoothing_sigmas=[[3, 2, 1, 0]]*3
reg.inputs.transform_parameters=[(0.1,),
                                 (0.1,),
                                 (0.1, 3.0, 0.0)]
reg.inputs.use_histogram_matching=True
reg.inputs.write_composite_transform=True

%timeit reg.run()