input_file = input("Choose the input file name (case sensitive!)\n")
fi = open(input_file,'r')
#Read first line to skip column header
fi.readline()

output_file = input("Choose the output file name (case sensitive!\n")
fo = open(output_file,'w')
fo.write("abscice\  valeur\n")

#used variable       
is_peak = False
max_peak = None

for line in fi:
    #used to treat each line
    line = line.strip("\n")
    values = line.split(";")
    values[1] = values[1][:6]
    values[1] = float(values[1])
    
    if (is_peak):
        
        #Used to detect the speak end, 1 is an arbitrary value set viewing latis graph)
        if (values[1] < 1):
            fo.write(max_peak[0]+"  "+str(max_peak[1])+'\n')
            is_peak = False
            max_peak = None
            
        else:

            #Update maximum in the peak
            if (values[1] > max_peak[1]):
                max_peak = values
    else:

        #Used to detect the speak start, 1 is an arbitrary value set viewing latis graph)
        if (values[1] > 1):
            is_peak = True
            max_peak = values

#Close file
fo.close()
fi.close()
            
        
    





