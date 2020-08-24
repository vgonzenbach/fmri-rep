"""Workflow that grabs files in a BIDS dataset and copies them into another location while preserving directory structure"""
from niworkflows.interfaces.bids import DerivativesDataSink
from nipype import Workflow, Node, IdentityInterface 
from nipype.interfaces.io import BIDSDataGrabber

# Initialize pipeline
pipeline = Workflow(name='pipeline')

# Create one Node from 
sink = Node(DerivativesDataSink(), name = 'sink')

# Create any other node
inputspec = Node(IdentityInterface(fields='file'), name = 'inputspec')
inputspec.inputs.file = '../../data/ds00171/sub-control01/anat/sub-control01_T1w.nii.gz'

# Test the connect method
pipeline.connect(inputspec, 'file', sink, 'in_file')

pipeline.run()
