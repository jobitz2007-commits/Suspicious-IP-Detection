#Jonah Obitz
#Python Final Project
#Finding and catching suspicious IPs


def main():
    #Open the file
    inputFile = openFile("ipList.txt", "r")

    #Process the input file
    inputData = inputFile.readlines()  #Read all lines
    inputFile.close()  #Explicitly close the file after reading

    totalRecords = len(inputData)
    suspectIPs = []
    suspects = ["168.193", "224.174", "233.012"]

    for line in inputData:
        ipAddress = line[:11]  #The IP address is the first 11 characters so line[:11] slices and isolates the IP
        for prefix in suspects:
            if ipAddress[:len(prefix)] == prefix:  #Check prefix by isolating only prefixes
                suspectIPs.append(line[:-1])  #Add the full line (IP and timestamp)
                break

    #Gets the output file names and opens it
    outputFile = openFile("output.txt", "w")
    #Generates and writes the output report
    writeFile(totalRecords, suspectIPs, outputFile)

    #Gets the print file names and opens it
    printFile = openFile("output.txt", "r")
    #Uses print file to print the output file
    readFile(printFile)
    printFile.close()


#Function to handle file opening in read or write mode    
def openFile(fileName, mode):
    valid = 0
    while valid ==0:
        try:
            file = open(fileName, mode)
            valid = 1  #File opened successfully
        except:
            print(f"ERROR -- There is an issue with file {fileName}. Please reenter:")
            fileName = input("Enter the file name (ip_list.txt): ")
    return file



#Function to create the output report
def writeFile(totalRecords, suspectIPs, outputFile):
     # Manually sort the suspect IPs
    length= len(suspectIPs)
    for i in range (length):
        for j in range(i + 1, length):
            if suspectIPs[i] > suspectIPs[j]:
               temp= suspectIPs[i]
               suspectIPs[i]=suspectIPs[j]
               suspectIPs[j]= temp

    #Write the report header
    outputFile.write("Output Report\n")
    outputFile.write("----------------------\n")
    outputFile.write(f"The total number of records in the file is: {totalRecords}\n")
    outputFile.write(f"The number of suspect IP addresses is: {len(suspectIPs)}\n")
    outputFile.write(f"The percentage of suspect IP addresses is: {len(suspectIPs) / totalRecords:.3f}\n")
    outputFile.write("Suspect IP Addresses\n")
    outputFile.write("----------------------\n")

    #Write sorted suspect IPs
    for ip in suspectIPs:
        outputFile.write(ip + "\n")
    outputFile.close()  # Closes the file
    print("Program complete!")

def readFile(file):
    #Prints the output report
    line= file.readline()[:-1]
    while line:
        print(line) 
        line = file.readline()[:-1]
    
main()