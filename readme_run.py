Description Document for run.py
Overview
run.py is a Python script written by Emily Rong Zhou, currently in its 1.0 release version. This script is designed to automate the processing of DICOM files and their subsequent handling, including directory management, file zipping, and preparation for transfer to an XNAT server.
Features
Flexible Input Handling: The script accepts various command-line arguments, including input file, output directory, and additional directory path. This allows for dynamic use based on user-specified paths and files.
Verbose and Debug Modes: Users can specify the level of verbosity for output messages or enable a debug mode for more detailed diagnostic information.
Automatic Directory Management: It can ensure the existence of specified directories, create them if they don't exist, and handle errors during creation.
DICOM File Handling: The script includes functionality to remove backup DICOM files (.dcm.bak) and to zip an entire directory of DICOM files for easier transfer and storage.
XNAT Integration: While detailed XNAT integration steps are not fully implemented in the script, it lays the groundwork for processing and preparing files for upload to an XNAT server.
Usage
Command-Line Arguments
-i, --input: Specify the input file (required).
-o, --outdir: Define the output directory path.
-d, --directory: Set an additional directory path.
-v, --verbose: Increase verbosity for more detailed output messages.
-D, --debug: Enable debug mode for additional diagnostic information.

Example Usage
./run.py -i CUPS.log -o /path/to/output -d /path/to/directory -v -D

Note:
CUPS.log is created with "du -k" to list files in CUPS direcotry like the following:
%cd ~/CUPS
%du -k &> CUPS.log

Functionality
Argument Parsing: The script uses argparse to manage command-line arguments, making it user-friendly and adaptable to various use cases.
Directory and File Operations: Functions like ensure_dir, rm_bak_files, and zip_directory manage directory creation, clean up backup files, and zip directories, respectively.
Custom Output Management: The Util class provides custom methods for running commands, timestamped printing (tprint), and debugging information (debug_print).
Extracting IDs: The get_id_in_file function extracts specific IDs from a given file, useful for processing specific subsets of data.
Running External Commands: The myRun class encapsulates the logic to execute external commands (related to XNAT file pipeline processing) for each ID in the provided list.
Notes
The script is designed with a focus on security and efficiency, avoiding hardcoding sensitive information and handling potential errors gracefully.
Users should ensure that the necessary Python environment and dependencies are set up before running the script.
The script is intended for users with a basic understanding of Python and command-line operations, especially in the context of medical imaging data management.
