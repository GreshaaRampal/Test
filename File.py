
output_file = open("Output_file.txt", "w")
  

with open("Input_file.txt", "r") as scan:
    output_file.write(scan.read())
  

output_file.close()
