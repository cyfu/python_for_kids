filename = "pokemon_list.txt"
filename_w = "pokemon_list_cleaned.txt"
fw = open(filename_w, "w")

with open(filename, 'r') as f:
    while True:
        first_line = f.readline()
        if not first_line: break

        second_line = f.readline()

        line1_split = first_line.split('\t')
        line2_split = second_line.split('\t')

        Num = line1_split[0].strip()
        Name = line1_split[1].strip()
        if (len(line1_split) > 2):  #no alia
            Alia = ""
            Type = line1_split[2].strip()
        else:
            Alia = line2_split[0].strip()
            Type = line2_split[1].strip()
            second_line = f.readline()
            line2_split = second_line.split('\t')

        if (len(line2_split) == 8):
            #first element is type
            Type = Type + "," + line2_split[0].strip()
            del line2_split[0]

        Total = line2_split[0].strip()
        HP = line2_split[1].strip()
        Attack = line2_split[2].strip()
        Defense = line2_split[3].strip()
        Sp_Atk = line2_split[4].strip()
        Sp_Def = line2_split[5].strip()
        Speed = line2_split[6].strip()
        print(Num)
        print(Name)
        print(Alia)
        print(Type)
        print(Total)
        print(HP)
        print(Attack)
        print(Defense)
        print(Sp_Atk)
        print(Sp_Def)
        print(Speed)

        new_line =  Num + "\t" + \
                    Name + "\t" + \
                    Alia + "\t" + \
                    Type + "\t" + \
                    Total + "\t" + \
                    HP + "\t" + \
                    Attack + "\t" + \
                    Defense + "\t" + \
                    Sp_Atk + "\t" + \
                    Sp_Def + "\t" + \
                    Speed

        print(new_line)
        fw.write(new_line + "\n")

f.close()
fw.close()