"""This function calls the GPF xml file by calling its
argument through a command prompt.

Arguments:
path= path to Sentinel 3 unzipped data containing xmls files
outputPath= output path where you want to export the final goetiff
xmlGraph= path to the xmlGraph containing SNAP functions (in this case it is fuGraph_nc.xml from:
https://github.com/CefasRepRes/Cefas_Plume_Mapping_Training/blob/main/fuGraph_nc.xml)
year= processing year 'YYYY'
month= processing month 'mm' format

This function assumes a specific folder structure, which might have to be changed.
""" 

def ForelUleSnapNC(path, outputPath, xmlGraph, year, month):

    import subprocess
    import glob

    #############assign variables##############

    dataList = glob.glob(path+"/"+year+"/"+month+"/*.SEN3")
    dataList.sort()
    ##########################################
    
    for i in range(len(dataList)):

        print(str(i))
        inputData = dataList[i]+"/xfdumanifest.xml"
        
        #extracts the data date but needs checking in case the path changes
        date = dataList[i].split('\\')[1][16:24] 
        print(date+" and index: "+str(i))
        
        #replace the slashes
        inputData = inputData.replace("\\", "/")
        
        #define the output data file
        outputData = outputPath+"/"+month+"/fu_"+date+"_"+str(i)+".nc"
        
        #create a string which will passed to command prompt
        command = "gpt "+xmlGraph+" -Pout="+outputData+" "+inputData
        print("Processing...")
        #print(inputData)
        print(command)
        #run the command
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
        stdout, stderr = process.communicate()
        print(stdout)
        #subprocess.call(command, shell=True)
        print("Successfully created FU.")
        
months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
year = "2020"

##loop through the months
for month in months:
    ForelUleSnapNC(path = "yourDataPath/s3_data",
                 outputPath= "yourOutputPath"+year+"/s3_fu_daily",
                 xmlGraph = "yourfuGraphOutputPath/fuGraph_nc.xml",
                 year= year,
                 month=month)
    
