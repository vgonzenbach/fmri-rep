from bids.layout import BIDSLayout
#from nipype import Workflow, Node, Function, MapNode
from niworkflows.interfaces.bids import DerivativesDataSink
import os

# Set project variables and set up workflow
project_dir = os.path.abspath('../..')
data_dir = 'data/ds000171/'
#wf = Workflow(name='wf', base_dir = os.getcwd())

# Leverage BIDS to get subject list
layout = BIDSLayout(os.path.join(project_dir, data_dir))
subject_list = layout.get_subjects()

a_path = layout.get(subject='control01', suffix='T1w')[0].path

dsink = DerivativesDataSink()
dsink.inputs.base_directory = os.getcwd()
dsink.inputs.desc = 'preprocessed'
dsink.inputs.out_path_base = "fmri-rep"

dsink.inputs.source_file = a_path
dsink.inputs.in_file = a_path
res = dsink.run()

#wf.connect(grab_anat, 'T1w', dsink, 'source_file')
#wf.connect(grab_anat, 'T1w', dsink, 'in_file')