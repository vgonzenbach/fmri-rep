import os
import numpy as np

from nibabel.testing import data_path
example_filename = os.path.join(data_path, 'example4d.nii.gz')

import nibabel as nib
img = nib.load(example_filename)

img.shape
img.get_data_dtype() == np.dtype(np.int16)
img.affine.shape

data = img.get_data()
data = img.get_fdata()
data.shape
type(data)

type(img)

hdr = img.header
hdr.get()
hdr.get_data_dtype()
hdr.get_xyzt_units()
raw = hdr.structarr
raw

## Creating a new image

import numpy as np
data = np.ones((32,32,15,100), dtype=np.int16)
img = nib.Nifti1Image(data, np.eye(4))
img.get_data_dtype()
img.get_data_dtype() == np.dtype(np.int16)
img.header.get_xyzt_units()
