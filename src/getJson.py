import os
  
#path to your own openpose ordner
#youtubePath_to your own video files ordner

path = "C:\\Users\\gayou\\Desktop\\openpose-1.6.0-binaries-win64-only_cpu-python-flir-3d\\openpose\\bin\\OpenPoseDemo.exe --video \""
path2 = "\" --model_pose MPI --write_json output/"
path3 = "\\"
path4 = " --render_pose 1\""
outputFolder = ()
currentDir = os.getcwd() + "\\output\\"
youTubePath = "C:\\Users\\gayou\\Desktop\\Youtube\\videos"

for root, dirs, files in os.walk(youTubePath, topdown=False):
  
    for name in files:

      outputFolder = root.split(os.path.sep, 6)
      outputFolderPath = outputFolder[6] + "//" + name
      
      if not os.path.exists(currentDir +  outputFolderPath):
          os.makedirs(currentDir + outputFolderPath)
          os.system( path + root + path3 + name + path2 +  outputFolderPath + path4 )