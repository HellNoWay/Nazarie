##@auther Hossein Hosseinpour 96521155;
## Mirhossein SeyedNasiri 96521281;

def input_process(File):
    ListOfInput = []
    for line in File:
        line = line.split("\n")
        ListOfInput.append(line)

    for i in range(len(ListOfInput)):
        if ListOfInput[i][-1] == '':
            del ListOfInput[i][-1]

    List = []
    for i in range(len(ListOfInput)):
        List.append(ListOfInput[i][0])

    List = [s.replace('->', '') for s in List]
    List = [s.replace('*', '') for s in List]
    List = [s.replace('_', '') for s in List]

    return List

def main_process(List):
    number = int(List[0])
    alphabet = List[1]
    alphabet = alphabet.split(",")
    trans = []
    non_trans = []
    for i in range(4,len(List)):
        local_Variable = List[i].split(",")
        if local_Variable[3] != "" :
            trans.append(List[i])
        else:
            non_trans.append(List[i])

    CFG_List = []
    for l in range(number):
        if l == 0:
            for i in range(len(trans)):
                local_Variable = trans[i].split(",")
                local_str = ""
                local_str = local_str + str(local_Variable[0])
                local_str = local_str + str(local_Variable[2])
                local_str = local_str + str(local_Variable[4])
                CFG_List.append(local_str)
                for j in range(number-1):
                    local_str = ""
                    local_str = local_str.join(local_Variable[1])
                    CFG_List.append(local_str)
                    for m in range(0,number):

                        local_str = ""
                        if len(local_Variable[3])>1:
                            local_str = local_str.join(str("("+local_Variable[0]+str(local_Variable[3][0])+"q"+str(m)+")"+"("+"q"+str(m)+str(local_Variable[3][1])+local_Variable[4]+")"))
                        else:
                            local_str = local_str.join(str("(" + local_Variable[0] + str(local_Variable[3][0]) + "q" + str(m) + ")"))
                        CFG_List.append(local_str)
        else:
            for i in range(len(trans)):
                local_Variable = trans[i].split(",")
                local_str = ""
                local_str = local_str + str(local_Variable[0])
                local_str = local_str + str(local_Variable[2])
                local_str = local_str + "qf"
                CFG_List.append(local_str)
                for j in range(number - 1):
                    local_str = ""
                    local_str = local_str.join(local_Variable[1])
                    CFG_List.append(local_str)
                    for m in range(0, number):
                        local_str = ""
                        if (len(local_Variable[3]) > 1):
                            local_str = local_str.join(str(
                                "(" + local_Variable[0] + str(local_Variable[3][0]) + "q" + str(m) + ")" + "(" + "q" + str(m) + str(
                                    local_Variable[3][1]) + "q" + ")"))
                        else:
                            local_str = local_str.join(str(
                                "(" + local_Variable[0] + str(local_Variable[3][0]) + "q" + str(m) + ")"))

                        CFG_List.append(local_str)


    others = Other_trans(non_trans)
    for i in range(len(others)):

        CFG_List.append(others[i])
    return CFG_List

def Other_trans(lst):
    CFG = []
    for i in range(len(lst)):
        string = ""
        Variable = lst[i].split(",")
        string = string + str(Variable[0])
        string = string + str(Variable[2])
        string = string + str(Variable[4])
        string = string + " -> "
        if Variable[1] != "":
            string = string + str(Variable[1])
        else:
            string = string + "_"

        CFG.append(string)
    return CFG





def main():
    input_file = input("Please Enter The File Dir \n")
    input_file = open(input_file , 'r')
    procedure = input_process(input_file)
    Main_list = main_process(procedure)

    for i in range(4*int(procedure[0])):
        print(Main_list[0] + " -> " + Main_list [1] + Main_list[2] + " | " + Main_list[1] + Main_list[3])
        for j in range(2*int(procedure[0])):
            del Main_list[0]

    for i in range(len(Main_list)):
        print(Main_list[i])





if __name__ == "__main__":
main()