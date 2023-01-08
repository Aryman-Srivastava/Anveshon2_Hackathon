def cleaner():
    with open("C:\\Users\\arjun\\OneDrive\\Desktop\\Anveshon2_Hackathon-1\\Software\\ML_Model\\rec.txt", 'r') as f_in:
        with open('output.txt', 'w') as f_out:
            prev_line = ''
            for line in f_in:
                if line.strip() or prev_line.strip() :
                    print(len(line))
                    f_out.write(line)
                    print(line)
                prev_line = line
