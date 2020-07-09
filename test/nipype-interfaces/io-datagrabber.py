"Test the DataGrabber interface"
from nipype.interfaces.io import DataGrabber

dg = DataGrabber()

dg.inputs.base_directory = '../../data/ds000171/'
dg.inputs.template = 'sub-*/anat/sub-*_T1w.nii.gz'
dg.inputs.sort_filelist = True

results = dg.run()
results.outputs

# Try it out for func images too
dg2 = DataGrabber()

dg2.inputs.base_directory = '../../data/ds000171/'
dg2.inputs.template = 'sub-*/func/s*.nii.gz'
dg2.inputs.sort_filelist = True

results2 = dg2.run()
results2.outputs
