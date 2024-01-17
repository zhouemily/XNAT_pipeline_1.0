set -x
#/usr/local/bin/python run.py -i CUPS.log -d path -v
#/usr/local/bin/python run.py -i /Users/zhou/xnat/testdir/CUPS.log -d /Volumes/CUPS/PipelineOutputs/bids/derivatives/ -v
#/System/Volumes/Data/Volumes/CUPS is the mounting directory
#du -k &> CUPS.log (this log is useful to extract the CUPS id which is used extensively for the processing script
#root_path can use /Volumes/CUPS/PipelineOutputs/bids/derivatives/
#or /System/Volumes/Data/Volumes/CUPS/PipelineOutputs/bids/derivatives/
./run.py -i ./CUPS.log -d /Volumes/CUPS/PipelineOutputs/bids/derivatives/ -v

#The above code create CUPS.DCM.zip in the current directory for upload
#The following script will upload CUPS.DCM.zip file to xnat server
#using the following python script:
#xnat_send.py
#requirments: a .netrc file has to be created at home directory with only permission to your self
#chmod 600 ~/.netrc
#see the xnat_send.py script for more details about ~/.netrc file format and content example
#################################
#./xnat_send.py    run this script with caution, make sure all the files are tested and 
#checked before upload to the xnat server
#########################################
