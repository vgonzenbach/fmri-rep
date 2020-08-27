from bids.layout import BIDSLayout
from nipype.interfaces.io import BIDSDataGrabber
from nipype import Workflow, Node, Function
import os

# Set project variables
project_dir = os.path.abspath('../..')
data_dir = 'data/ds000171/'

# Leverage BIDS to get subject list
layout = BIDSLayout(os.path.join(project_dir, data_dir))
subject_list = layout.get_subjects()

grab_anat = Node(BIDSDataGrabber(), name = 'grab_anat')
grab_anat.inputs.base_dir = os.path.join(project_dir, data_dir)

# Iterate through subjects; [:2] for only 2 subjects to keep memory usage low
grab_anat.iterables = ('subject', subject_list[:2])

# Define filetypes to grab, and how ouput will be accesses by other nodes 
grab_anat.inputs.output_query = {'T1w': dict(extension=['nii.gz'], suffix='T1w')}

def printFile(paths):
    print("\n\nPrinting " + str(paths) + "\n\n")
    
printfile = Node(Function(function=printFile, input_names=["paths"],
                            output_names=[]), name="printfile")

wf = Workflow(name='wf')
wf.connect(grab_anat, 'T1w', printfile, 'paths')
res = wf.run()
