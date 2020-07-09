"""Perform slice timing and motion correction on brain extracted images"""
from nipype.interfaces.fsl import SliceTimer, MCFLIRT, PlotMotionParams

func = "../../data/ds000171/sub-control01/func/sub-control01_task-music_run-1_bold.nii.gz"
func_bet = '../testdata/func_bet2.nii.gz'

# Perform slice timing correction
st = SliceTimer()
st.inputs.in_file = func
st.inputs.interleaved = True
st.inputs.time_repetition = 3
st.inputs.out_file = '../testdata/func_st.nii.gz'

st.run()


# Perform motion correction
mc = MCFLIRT()
mc.inputs.in_file = '../testdata/func_st.nii.gz'
mc.inputs.cost = 'mutualinfo'
mc.inputs.interpolation = 'sinc'
mc.inputs.save_mats = True
mc.inputs.save_plots = True
mc.inputs.mean_vol = True
mc.inputs.out_file = '../testdata/func_mc_st.gz'
mc.run()

#Plot Motion Parameters - saved as .png in same directory

# Rotation
plotter_rot = PlotMotionParams()
plotter_rot.inputs.in_file = '../testdata/func_mc_st.gz.par'
plotter_rot.inputs.in_source = 'fsl'
plotter_rot.inputs.plot_type = 'rotations'
plotter_rot.run() 

#Translation
plotter_trans = PlotMotionParams()
plotter_trans.inputs.in_file = '../testdata/func_mc_st.gz.par'
plotter_trans.inputs.in_source = 'fsl'
plotter_trans.inputs.plot_type = 'translations'
plotter_trans.run()

#Displacement
plotter_disp = PlotMotionParams()
plotter_disp.inputs.in_file = '../testdata/func_mc_st.gz.par'
plotter_disp.inputs.in_source = 'fsl'
plotter_disp.inputs.plot_type = 'displacement'
plotter_disp.run()