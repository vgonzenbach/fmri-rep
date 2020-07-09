"""Runs bet twice to improve skull-stripping with center of gravity"""

from nipype.interfaces.fsl import BET
func = "../../data/ds000171/sub-control01/func/sub-control01_task-music_run-1_bold.nii.gz"

bet = BET()

bet.inputs.in_file = func
bet.inputs.frac = 0.5
bet.inputs.out_file = '../output/fsl-bet-func/func_bet.nii.gz'
bet.inputs.mask = True
bet.run()

mask_path = '../testdata/func_bet_mask.nii.gz'

# Load mask as numpy array
import nibabel as nib
mask = nib.load(mask_path)
mask_array = mask.get_fdata()

# Get center of mass with scipy
from scipy.ndimage.measurements import center_of_mass
cog = [int(x) for x in list(center_of_mass(mask_array))] # list comprehension yo!

# Run again
bet2  = BET()
bet2.inputs.in_file = func
bet2.inputs.frac = 0.3
bet2.inputs.center = cog
bet2.inputs.out_file = '../output/fsl-bet-func/func_bet2.nii.gz'
bet2.inputs.mask = True

bet2.run()

# Visualize the results
from nilearn.image import index_img
from nilearn.plotting import plot_roi

volume = 0
plot_roi('../output/fsl-bet-func/func_bet2_mask.nii.gz', index_img(func, volume))