"""Grab data included in nipype directory for testing purposes"""
from nipype.testing import example_data

# Print different filepaths
example_data(infile = 'functional.nii')
example_data(infile = 'structural.nii')
example_data(infile = 'mni.nii')