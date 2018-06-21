# CPAC Pipeline Configuration YAML file
# Version 1.0.4
#
# http://fcp-indi.github.io for more info.
#
# Tip: This file can be edited manually with a text editor for quick modifications.


# Select False if you intend to run CPAC on a single machine.
# If set to True, CPAC will attempt to submit jobs through the job scheduler / resource manager selected below.
runOnGrid :  False


# Full path to the FSL version to be used by CPAC.
# If you have specified an FSL path in your .bashrc file, this path will be set automatically.
FSLDIR :  /path/to/FSL


# Sun Grid Engine (SGE), Portable Batch System (PBS), or Simple Linux Utility for Resource Management (SLURM).
# Only applies if you are running on a grid or compute cluster.
resourceManager :  SGE


# SGE Parallel Environment to use when running CPAC.
# Only applies when you are running on a grid or compute cluster using SGE.
parallelEnvironment :  cpac


# SGE Queue to use when running CPAC.
# Only applies when you are running on a grid or compute cluster using SGE.
queue :  all.q


# The maximum amount of memory each participant's workflow can allocate. Use this to place an upper bound of memory usage. Warning: 'Memory Per Participant' multiplied by 'Number of Participants to Run Simultaneously' must not be more than the total amount of RAM. Conversely, using too little RAM can impede the speed of a pipeline run. It is recommended that you set this to a value that when multiplied by 'Number of Participants to Run Simultaneously' is as much RAM you can safely allocate.
maximumMemoryPerParticipant :  2


# The maximum amount of cores (on a single machine) or slots on a node (on a cluster/grid) to allocate per participant. Setting this above 1 will parallelize each participant's workflow where possible. If you wish to dedicate multiple cores to ANTS-based anatomical registration (below), this value must be equal or higher than the amount of cores provided to ANTS. The maximum number of cores your run can possibly employ will be this setting multiplied by the number of participants set to run in parallel (the 'Number ofParticipants to Run Simultaneously' setting).
maxCoresPerParticipant :  1


# The number of participant workflows to run at the same time. The maximum number of cores your run can possibly employ will be this setting multiplied by the number of cores dedicated to each participant (the 'Maximum Number of Cores Per Participant' setting).
numParticipantsAtOnce :  1


# The number of cores to allocate to ANTS-based anatomical registration per participant. Multiple cores can greatly speed up this preprocessing step. This number cannot be greater than the number of cores per participant.
num_ants_threads :  1


# Name for this pipeline configuration - useful for identification.
pipelineName :  pipeline01


# Directory where CPAC should store temporary and intermediate files.
workingDirectory :  /home/runs/pipeline01/work


# Directory where CPAC should write crash logs.
crashLogDirectory :  /home/runs/pipeline01/crash


# Directory where CPAC should place run logs.
logDirectory :  /home/runs/pipeline01/log


# Directory where CPAC should place processed data.
outputDirectory :  /home/runs/pipeline01/output


# If setting the 'Output Directory' to an S3 bucket, insert the path to your AWS credentials file here. ?absicherung der daten?
awsOutputBucketCredentials :  


# Enable server-side 256-AES encryption on data to the S3 bucket
s3Encryption :  [1]


# Include extra versions and intermediate steps of functional preprocessing in the output directory.
write_func_outputs: [0]


# Include extra outputs in the output directory that may be of interest when more information is needed.
write_debugging_outputs: [0]


# Generate quality control pages containing preprocessing and derivative outputs.
generateQualityControlImages: [1]


# Deletes the contents of the Working Directory after running.
# This saves disk space, but any additional preprocessing or analysis will have to be completely re-run.
removeWorkingDir :  False


# Whether to write log details of the pipeline run to the logging files.
run_logging :  True


# Uses the contents of the Working Directory to regenerate all outputs and their symbolic links.
# Requires an intact Working Directory from a previous CPAC run.
reGenerateOutputs :  False


# Create a user-friendly, well organized version of the output directory.
# We recommend all users enable this option.
runSymbolicLinks :  [1]


# The resolution to which anatomical images should be transformed during registration.
# This is the resolution at which processed anatomical files will be output.
resolution_for_anat :  2mm


# Template to be used during registration.
# It is not necessary to change this path unless you intend to use a non-standard template.
template_brain_only_for_anat :  /path/to/FSL/data/standard/MNI152_T1_${resolution_for_anat}_brain.nii.gz


# Template to be used during registration.
# It is not necessary to change this path unless you intend to use a non-standard template.
template_skull_for_anat :  /path/to/FSL/data/standard/MNI152_T1_${resolution_for_anat}.nii.gz


# Use either ANTS or FSL (FLIRT and FNIRT) as your anatomical registration method.
# Options: ['ANTS'] or ['FSL']
regOption :  ['ANTS']


# Configuration file to be used by FSL to set FNIRT parameters.
# It is not necessary to change this path unless you intend to use custom FNIRT parameters or a non-standard template.
fnirtConfig :  T1_2_MNI152_2mm


# Configuration file to be used by FSL to set FNIRT parameters.
# It is not necessary to change this path unless you intend to use custom FNIRT parameters or a non-standard template.
ref_mask :  /path/to/FSL/data/standard/MNI152_T1_${resolution_for_anat}_brain_mask_dil.nii.gz


# Register skull-on anatomical image to a template.
regWithSkull :  [0]


# Disables skull-stripping on the anatomical inputs if they are already skull-stripped outside of C-PAC. Set this to On if your input images are already skull-stripped.
already_skullstripped :  [0]


# Automatically segment anatomical images into white matter, gray matter, and CSF based on prior probability maps.
runSegmentationPreprocessing :  [1]


# Full path to a directory containing binarized prior probability maps.
# These maps are included as part of the 'Image Resource Files' package available on the Install page of the User Guide.
# It is not necessary to change this path unless you intend to use non-standard priors.
priors_path :  /path/to/FSL/data/standard/tissuepriors/2mm


# Full path to a binarized White Matter prior probability map.
# It is not necessary to change this path unless you intend to use non-standard priors.
PRIORS_WHITE :  $priors_path/avg152T1_white_bin.nii.gz


# Full path to a binarized Gray Matter prior probability map.
# It is not necessary to change this path unless you intend to use non-standard priors.
PRIORS_GRAY :  $priors_path/avg152T1_gray_bin.nii.gz


# Full path to a binarized CSF prior probability map.
# It is not necessary to change this path unless you intend to use non-standard priors.
PRIORS_CSF :  $priors_path/avg152T1_csf_bin.nii.gz


# Perform fieldmap correction using FSL FUGUE, with a single phase difference image, a subtraction of the two phase images from each echo.
# Default scanner for this method is SIEMENS.
runEPI_DistCorr :  [0]


# Since the quality of the distortion heavily relies on the skull-stripping,
# step, we provide a choice of method (AFNI 3dSkullStrip or FSL BET).
# Options: ["BET", "3dSkullStrip"]
fmap_distcorr_skullstrip: ["BET"]


# Set the threshold value for the skull-stripping of the magnitude file.
# Depending on the data, a tighter extraction may be necessary in order to
# prevent noisy voxels from interfering with preparing the field map.
# The default value is 0.5.
fmap_distcorr_frac: [0.5]


# Set the Delta-TE value, used for preparing the field map, the time delay between the first and second echo images.
fmap_distcorr_deltaTE : 2.46


# Set the Dwell time for FSL FUGUE. This is the time between scans.
# The default value is commonly 0.00231s.
fmap_distcorr_dwell_time : [0.0005]


# Set the asymmetric ratio input value for FSL FUGUE.
fmap_distcorr_dwell_asym_ratio : [0.93902439]


# Set the phase-encoding direction. The options are: x, y, z, -x, -y, -z.
fmap_distcorr_pedir: -y


# Run Functional to Anatomical Registration
runRegisterFuncToAnat :  [1]


# Run Functional to Anatomical Registration with BB Register
runBBReg :  [1]


# Standard FSL 5.0 Scheduler used for Boundary Based Registration.
# It is not necessary to change this path unless you intend to use non-standard MNI registration.
boundaryBasedRegistrationSchedule :  /path/to/FSL/etc/flirtsch/bbr.sch


# Choose whether to use the mean of the functional/EPI as the input to functional-to-anatomical registration or one of the volumes from the functional 4D timeseries that you choose.
func_reg_input :  ['Mean Functional']


# Choose which tool to be used in functional masking - AFNI 3dAutoMask or FSL BET.
functionalMasking :  ['3dAutoMask']


# Register functional images to a standard MNI152 template.
# This option must be enabled if you wish to calculate any derivatives. If set to On [1], only the template-space files will be output. If set to On/Off [1,0], both template-space and native-space files will be output.
# Options: [1], [0], or [1,0]
runRegisterFuncToMNI :  [1]


# The resolution (in mm) to which the preprocessed, registered functional timeseries outputs are written into. Note that selecting a 1 mm or 2 mm resolution might substantially increase your RAM needs- these resolutions should be selected with caution. For most cases, 3 mm or 4 mm resolutions are suggested.
resolution_for_func_preproc :  3mm


# The resolution (in mm) to which the registered derivative outputs are written into.
resolution_for_func_derivative :  3mm


# Standard FSL Skull Stripped Template. Used as a reference image for functional registration
template_brain_only_for_func :  /path/to/FSL/data/standard/MNI152_T1_${resolution_for_func_preproc}_brain.nii.gz


# Standard FSL Anatomical Brain Image with Skull
template_skull_for_func :  /path/to/FSL/data/standard/MNI152_T1_${resolution_for_func_preproc}.nii.gz


# Matrix containing all 1's. Used as an identity matrix during registration.
# It is not necessary to change this path unless you intend to use non-standard MNI registration.
identityMatrix :  /path/to/FSL/etc/flirtsch/ident.mat


# Run Nuisance Signal Regression
runNuisance :  [1]


# Standard Lateral Ventricles Binary Mask
lateral_ventricles_mask :  /path/to/FSL/data/atlases/HarvardOxford/HarvardOxford-lateral-ventricles-thr25-2mm.nii.gz


# Select which nuisance signal corrections to apply:
# compcor = CompCor
# wm = White Matter
# csf = CSF
# gm = Gray Matter
# global = Global Mean Signal
# pc1 = First Principle Component
# motion = Motion
# linear = Linear Trend
# quadratic = Quadratic Trend
Regressors :
  -  compcor :  1
     wm :  0
     csf :  1
     global :  0
     pc1 :  0
     motion :  1
     linear :  1
     quadratic :  1
     gm :  0


# Number of Principle Components to calculate when running CompCor. We recommend 5 or 6.
nComponents : [5]


# Use the Friston 24-Parameter Model during volume realignment.
# If this option is turned off, only 6 parameters will be used.
# These parameters will also be output as a spreadsheet.
runFristonModel :  [1]


# Remove or regress out volumes exhibiting excessive motion.
# Options: ['De-Spiking'] or ['Scrubbing']
runMotionSpike :  ['Off']


# (Motion Spike De-Noising only) Choose which Framewise Displacement (FD) calculation to apply the threshold to during de-spiking or scrubbing.
# Options: ['Jenkinson'] or ['Power']
fdCalc :  ['Jenkinson']


# (Motion Spike De-Noising only) Specify the maximum acceptable Framewise Displacement (FD) in millimeters.
# Any volume exhibiting FD greater than the value will be regressed out or scrubbed.
spikeThreshold : [0.5]


# (Motion Spike De-Noising only) Number of volumes to de-spike or scrub preceding a volume with excessive FD.
numRemovePrecedingFrames :  1


# (Motion Spike De-Noising only) Number of volumes to de-spike or scrub subsequent to a volume with excessive FD.
numRemoveSubsequentFrames :  2


# Correct for the global signal using Median Angle Correction.
runMedianAngleCorrection :  [0]


# Target angle used during Median Angle Correction.
targetAngleDeg : [90]


# Apply a temporal band-pass filter to functional data.
runFrequencyFiltering :  [1]


# Define one or more band-pass filters by clicking the + button.
nuisanceBandpassFreq : [[0.01, 0.1]]


# Extract the average time series of one or more ROIs/seeds. Must be enabled if you wish to run Seed-based Correlation Analysis.
runROITimeseries :  [0]


# Enter paths to region-of-interest (ROI) NIFTI files (.nii or .nii.gz) to be used for time-series extraction, and then select which types of analyses to run.
# Available analyses: ['Avg', 'Voxel', 'SpatialReg'].
# Denote which analyses to run for each ROI path by listing the names above. For example, if you wish to run Avg and SpatialReg, you would enter: '/path/to/ROI.nii.gz': Avg, SpatialReg
tsa_roi_paths: None
  - /path/to/resources/rois.nii.gz: Avg, Voxel, SpatialReg


# By default, extracted time series are written as both a text file and a 1D file. Additional output formats are as a .csv spreadsheet or a Numpy array.
roiTSOutputs :  [False, False]


# For each extracted ROI Average time series, CPAC will generate a whole-brain correlation map.
# It should be noted that for a given seed/ROI, SCA maps for ROI Average time series will be the same.
runSCA :  [1]


# Enter paths to region-of-interest (ROI) NIFTI files (.nii or .nii.gz) to be used for time-series extraction, and then select which types of analyses to run.
# Available analyses: ['Avg', 'DualReg', 'MultReg'].
# Denote which analyses to run for each ROI path by listing the names above. For example, if you wish to run Avg and MultReg, you would enter: '/path/to/ROI.nii.gz': Avg, MultReg
sca_roi_paths:
  - /path/to/resources/rois.nii.gz: Avg, DualReg, MultReg



# Normalize each time series before running Dual Regression SCA.
mrsNorm :  True


# Calculate Voxel-mirrored Homotopic Connectivity (VMHC) for all voxels.
runVMHC :  [1]


# Included as part of the 'Image Resource Files' package available on the Install page of the User Guide.
# It is not necessary to change this path unless you intend to use a non-standard symmetric template.
template_symmetric_brain_only :  $FSLDIR/data/standard/MNI152_T1_${resolution_for_anat}_brain_symmetric.nii.gz


# Included as part of the 'Image Resource Files' package available on the Install page of the User Guide.
# It is not necessary to change this path unless you intend to use a non-standard symmetric template.
template_symmetric_skull :  $FSLDIR/data/standard/MNI152_T1_${resolution_for_anat}_symmetric.nii.gz


# Included as part of the 'Image Resource Files' package available on the Install page of the User Guide.
# It is not necessary to change this path unless you intend to use a non-standard symmetric template.
dilated_symmetric_brain_mask :  $FSLDIR/data/standard/MNI152_T1_${resolution_for_anat}_brain_mask_symmetric_dil.nii.gz


# Included as part of the 'Image Resource Files' package available on the Install page of the User Guide.
# It is not necessary to change this path unless you intend to use a non-standard symmetric template.
configFileTwomm :  $FSLDIR/etc/flirtsch/T1_2_MNI152_2mm.cnf


# Calculate Amplitude of Low Frequency Fluctuations (ALFF) and and fractional ALFF (f/ALFF) for all voxels.
runALFF :  [1]


# Frequency cutoff (in Hz) for the high-pass filter used when calculating f/ALFF.
highPassFreqALFF : [0.01]


# Frequency cutoff (in Hz) for the low-pass filter used when calculating f/ALFF
lowPassFreqALFF : [0.1]


# Calculate Regional Homogeneity (ReHo) for all voxels.
runReHo :  [1]


# Number of neighboring voxels used when calculating ReHo
# 7 (Faces)
# 19 (Faces + Edges)
# 27 (Faces + Edges + Corners)
clusterSize :  27


# Calculate Degree, Eigenvector Centrality, or Functional Connectivity Density.
runNetworkCentrality :  [1]


# Full path to a NIFTI file describing the mask. Centrality will be calculated for all voxels within the mask.
templateSpecificationFile :  /path/to/resources/mask-thr50-3mm.nii.gz


# Enable/Disable degree centrality by selecting the connectivity weights
degWeightOptions :  [True, True]


# Select the type of threshold used when creating the degree centrality adjacency matrix.
# Options: ['Significance threshold'], ['Sparsity threshold'], or ['Correlation threshold']
degCorrelationThresholdOption :  ['Significance threshold']


# Based on the Threshold Type selected above, enter a Threshold Value.
# P-value for Significance Threshold
# Sparsity value for Sparsity Threshold
# Pearson's r value for Correlation Threshold
degCorrelationThreshold :  0.001


# Enable/Disable eigenvector centrality by selecting the connectivity weights
eigWeightOptions :  [True, True]


# Select the type of threshold used when creating the eigenvector centrality adjacency matrix.
# Options: ['Significance threshold'], ['Sparsity threshold'], or ['Correlation threshold']
eigCorrelationThresholdOption :  ['Significance threshold']


# Based on the Threshold Type selected above, enter a Threshold Value.
# P-value for Significance Threshold
# Sparsity value for Sparsity Threshold
# Pearson's r value for Correlation Threshold
eigCorrelationThreshold :  0.001


# Enable/Disable lFCD by selecting the connectivity weights
lfcdWeightOptions :  [True, True]


# Select the type of threshold used when creating the lFCD adjacency matrix.
# Options: ['Significance threshold'] or ['Correlation threshold']
lfcdCorrelationThresholdOption :  ['Significance threshold']


# Based on the Threshold Type selected above, enter a Threshold Value.
# P-value for Significance Threshold
# Sparsity value for Sparsity Threshold
# Pearson's r value for Correlation Threshold
lfcdCorrelationThreshold :  0.001


# Maximum amount of RAM (in GB) to be used when calculating Degree Centrality.
# Calculating Eigenvector Centrality will require additional memory based on the size of the mask or number of ROI nodes.
memoryAllocatedForDegreeCentrality :  3.0


# Smooth the derivative outputs or not, or produce both unsmoothed and smoothed versions, if preferred.
# Options: [1], [0], or [1,0]
run_smoothing: [1]


# Full Width at Half Maximum of the Gaussian kernel used during spatial smoothing.
# Can be a single value or multiple values separated by commas.
# Note that spatial smoothing is run as the last step in the individual-level analysis pipeline, such that all derivatives are output both smoothed and unsmoothed.
fwhm : [4]


# Decides format of outputs. Off will produce non-z-scored outputs, On will produce z-scores of outputs, and On/Off will produce both.
# Options: [1]
runZScoring : [1], [0], or [1,0]


# This number depends on computing resources.
numGPAModelsAtOnce :  1


# Use the + to add FSL model configuration to be run.
modelConfigs :  ['/path/to/configs/gpa_fsl_config_group1.yml']

