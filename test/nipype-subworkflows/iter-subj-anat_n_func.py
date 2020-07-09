"""A simple iterative workflow that grabs functional and anatomical images. for each subject in a database and saves them. This workflow can serve as a template for a preprocessing pipeline for a whole database: just add preprocessing nodes between input and output nodes."""
from nipype import MapNode, Node, Workflow, IdentityInterface, DataGrabber, DataSink
import os

test_dir = os.getcwd()
wf = Workflow(name = 'iter_subj_splitgrabber', base_dir = test_dir)

# Two subjects minimum
subject_list = ['control01', 'control02']
runs = [1,2,3,4,5]

# A IdentityInterface node helps to iterate over list of subject names and run: grabs anatomical images
info_subj = Node(IdentityInterface(fields=['subject_id']), name="info_subj")
info_subj.iterables = [('subject_id', subject_list)]

# Same as above: grabs functional images
info_run = Node(IdentityInterface(fields=['run_id']), name="info_run")
info_run.iterables = [('run_id', runs)]

# DataGrabber 1 - grab_anat
data_dir = '/Users/vgonzenb/Python/nipy/fmri-rep/data/ds000171/'

grab_anat = Node(DataGrabber(infields=['subject_id'],outfields=['anat']), name = 'grab_anat', nested = True)
grab_anat.inputs.base_directory = data_dir
grab_anat.inputs.template = '*'
grab_anat.inputs.sort_filelist = True
grab_anat.inputs.template_args = {'anat': [['subject_id']]}
grab_anat.inputs.field_template = {'anat': 'sub-%s/anat/s*T1w.nii.gz'}

# DataGrabber 2 - func

grab_func = Node(DataGrabber(infields=['subject_id', 'runs'],outfields=['func']), name = 'grab_func', nested = True)
grab_func.inputs.base_directory = data_dir
grab_func.inputs.template = '*'
grab_func.inputs.sort_filelist = True
grab_func.inputs.template_args = {'func': [['subject_id', 'runs']]}
grab_func.inputs.field_template = {'func': 'sub-%s/func/sub-*run-%d_bold.nii.gz'}

# DataSink

datasink = Node(DataSink(base_directory = os.getcwd()), name='datasink')

wf.connect([(info_subj, grab_anat, [('subject_id', 'subject_id')]),(info_subj, grab_func, [('subject_id', 'subject_id')]),(info_run, grab_func, [('run_id', 'runs')]),(info_subj, datasink, [('subject_id', 'container')]),(grab_anat, datasink, [('anat', 'anat')]),(grab_func, datasink, [('func', 'func')])])

# Plot worflow
wf.write_graph(dotfilename='try.dot', graph2use='exec', simple_form = False)
from IPython.display import Image
Image(filename="iter_subj_splitgrabber/try_detailed.png")

# Run it 
# wf.run()