Node: dg (io)
=============


 Hierarchy : wf.dg
 Exec ID : dg


Original Inputs
---------------


* base_directory : ../../data/ds000171
* drop_blank_outputs : False
* field_template : {'anat': 'sub-%s/anat/s*T1w.nii.gz', 'func': 'sub-%s-/func/sub-*run-%d'}
* raise_on_empty : True
* run : [1, 2, 3, 4, 5]
* sort_filelist : True
* subject_id : ['control01']
* template : *
* template_args : {'anat': [['subject_id']], 'func': [['subject_id', 'run']]}

