"""Simple workflow component that queries a BIDS dataset and handles files individually"""
from bids.layout import BIDSLayout
from nipype.interfaces.io import BIDSDataGrabber
from nipype import Workflow, Node, Function, MapNode
from niworkflows.interfaces.bids import DerivativesDataSink
import os

# Set project variables and set up workflow
project_dir = os.path.abspath('../..')
data_dir = 'data/ds000171/'
wf = Workflow(name='wf', base_dir = os.getcwd())

# Leverage BIDS to get subject list
layout = BIDSLayout(os.path.join(project_dir, data_dir))
subject_list = layout.get_subjects()[:2]
runs = layout.get_runs()[:2]

"""
==============================
Anatomical Image Input
==============================
"""
grab_anat = Node(BIDSDataGrabber(), name = 'grab_anat')
grab_anat.inputs.base_dir = os.path.join(project_dir, data_dir)

# Iterate through subjects; [:2] for only 2 subjects to keep memory usage low
grab_anat.iterables = ('subject', subject_list)

# Define filetypes to grab, and how ouput will be accesses by other nodes 
grab_anat.inputs.output_query = {'T1w': dict(extension=['nii.gz'], suffix='T1w')}

#res = grab_anat.run()

# The Select utility interface
from nipype.interfaces.utility import Select
sel1 = Node(Select(), name='select1')
sel1.inputs.index = 0

wf.connect(grab_anat, 'T1w', sel1, 'inlist')

wf.run()

"""
============================================
Input of Functional Images
============================================
"""
grab_func = Node(BIDSDataGrabber(), name='grab_func')

grab_func.inputs.base_dir = os.path.join(project_dir, data_dir)
grab_func.inputs.output_query = {'bold': dict(extension=['nii.gz'], suffix='bold')}
grab_func.iterables = [('subject', subject_list), ('run', runs)]

sel2 = Node(Select(), name='select2')
sel2.inputs.index = 0

wf.connect(grab_func, 'bold', sel2, 'inlist')

"""
============================================
Output of Anatomical and Functional Images
============================================
"""
dsink = MapNode(DerivativesDataSink(), name='dsink', iterfield=["in_file", "source_file"])
dsink.inputs.base_directory = os.getcwd()
dsink.inputs.desc = 'preprocessed'

wf.connect(sel1, 'out', dsink, 'in_file')
wf.connect(sel1, 'out', dsink, 'source_file')

dsink2 = MapNode(DerivativesDataSink(), name='dsink2', iterfield=["in_file", "source_file"])
dsink2.inputs.base_directory = os.getcwd()
dsink2.inputs.desc = 'preprocessed'

wf.connect(sel2, 'out', dsink2, 'in_file')
wf.connect(sel2, 'out', dsink2, 'source_file')

wf.run()
