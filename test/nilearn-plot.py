"""This script shows how to use modules and functions from nilearn
    MODULES: image, masking, plotting, datasets
    Functions: 
"""
from nilearn import datasets

#By default 2nd subject will be fetched
haxby_dataset = datasets.fetch_haxby()

# print basic information on the dataset
print('First anatomical nifti image (3D) located is at: %s' % haxby_dataset.anat[0])
print('First functional nifti image (4D) is located at: %s' % haxby_dataset.func[0])

# Computer the mean EPI: we do the mean along the axis 3, time
from nilearn.image.image import mean_img

func_filename = haxby_dataset.func[0]
mean_haxby = mean_img(func_filename)

from nilearn.plotting import plot_epi, show
plot_epi(mean_haxby, output_file = 'nilearn-fig/epi_image.pdf')
#show()
#plt.savefig('nilearn-fig/epi_image.pdf')

from nilearn.masking import compute_epi_mask
mask_img = compute_epi_mask(func_filename)

from nilearn.plotting import plot_roi
plot_roi(mask_img, mean_haxby, output_file = 'nilearn-fig/roi_img.pdf')
#show()
#plt.savefig('nilearn-fig/roi_img.pdf')

from nilearn.masking import apply_mask
masked_data = apply_mask(func_filename, mask_img)

import matplotlib.pyplot as plt
plt.figure(figsize=(7,5))
plt.plot(masked_data[:150, :2])
plt.xlabel('Time [TRs]', fontsize=16)
plt.ylabel('Intensity', fontsize=16)
plt.xlim(0,150)
#show()
plt.savefig('nilearn-fig/time-series.pdf')
