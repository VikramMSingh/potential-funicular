def remove_special_characters_right(file1, file2):
    file_read = open(file1,"r")
    file_write = open(file2,"w")
    lines=''
    for line in file_read:
        lines = line.replace('-','')
        file_write.write(lines)       
    file_read.close()
    file_write.close()

remove_special_characters_right("test_names.txt", "test_names_2.txt")

    
