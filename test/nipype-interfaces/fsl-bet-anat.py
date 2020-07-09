"""Runs bet twice to improve skull-stripping with center of gravity"""
from nipype.interfaces.fsl import BET

anat = "../../data/ds000171/sub-control01/anat/sub-control01_T1w.nii.gz"

bet = BET()

bet.inputs.in_file = anat
bet.inputs.frac = 0.5

brain = '../output/better-bet-anat/anat_bet.nii.gz'
bet.inputs.out_file = brain
bet.inputs.mask = True
bet.run()



# Load mask as numpy array
import nibabel as nib
mask_path = '../output/better-bet-anat/anat_bet_mask.nii.gz'
mask = nib.load(mask_path)
mask_array = mask.get_fdata()

# Get center of mass with scipy
from scipy.ndimage.measurements import center_of_mass
cog = [int(x) for x in list(center_of_mass(mask_array))] # list comprehension yo!

bet2  = BET()
bet2.inputs.in_file = anat
bet2.inputs.frac = 0.3
bet2.inputs.center = cog
bet2.inputs.out_file = '../output/better-bet-anat/anat_bet2.nii.gz'
bet2.inputs.mask = True

bet2.run()

#Visualize results
from nilearn.image import index_img
from nilearn.plotting import plot_roi

plot_roi("../output/better-bet-anat/anat_bet2_mask.nii.gz", anat)
