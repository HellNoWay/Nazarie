##@auther Hossein Hosseinpour 96521155;
## Mirhossein SeyedNasiri 96521281;



def process_input(File):
    ListOfInput = []
    for line in File:
        line = line.split("\n")
        ListOfInput.append(line)

    for i in range(len(ListOfInput)):
        if ListOfInput[i][-1] == '':
            del ListOfInput[i][-1]
    return ListOfInput

def find_first_last(List):
    last_first = []
    first = List[4][0]
    first = first.split(',')
    for i in range(len(first)):
        if first[i][0] == "-":
            last_first.append(first[i][2:])
            break
    last = List[-1][0]
    last = last.split(',')
    for i in range(len(last)):
        if last[i][0] == "*":
            last_first.append(last[i][1:])
            break

    return last_first

def peek_stack(stack):
    if stack:
        return stack[-1]

def main():
    input_file = input("Please Enter The File Dir \n")
    input_file = open(input_file , 'r')
    procedure = process_input(input_file)
    found = find_first_last(procedure)
    Begin = found[0]

    last = found[1]

    Grammar = []
    for i in range(4,len(procedure)):
        Grammar.append(procedure[i])

    final_grammar = []
    for i in range(len(Grammar)):
        final_grammar.append(Grammar[i][0])

    Grammar = [s.replace('->', '') for s in final_grammar]
    Grammar = [s.replace('*', '') for s in Grammar]
    Grammar = [s.replace('_', '') for s in Grammar]
    indep_v = Grammar[-1]
    indep_v = indep_v.split(",")
    indep_v = "(" + indep_v[0] + indep_v[2] + indep_v[4] + ")"


    Stack = ["$"]
    StringOfInput = input("Please Enter A STR \n")

    reporter_stack = []
    length  = len(Grammar)
    for i in range(len(StringOfInput)):
        for j in range(len(Grammar)):
            current_grammar = Grammar[j].split(",")
            peek = peek_stack(Stack)


            if(StringOfInput[i] == current_grammar[1] and peek == current_grammar[2] and Begin == current_grammar[0]):
                Begin = current_grammar[4]
                Stack.pop()
                for k in range(len(current_grammar[3])-1,-1,-1):

                    Stack.append(current_grammar[3][k])
                    reporter_stack.append(current_grammar[3][k])

                break


    final_dir = Grammar.pop()
    final_dir = final_dir.split(",")
    aux_str = ""



    for i in range(len(Stack)):
        aux_str = aux_str.join(Stack[i])

    if(aux_str == final_dir[2]):
        print("Output")
        print("True")
        final_list_of_TLA = show_dir(Begin , reporter_stack, indep_v, StringOfInput)

        for j in range(len(final_list_of_TLA)-1):
            print(final_list_of_TLA[j] , end = " => ")
        print(final_list_of_TLA[len(final_list_of_TLA)-1])

    else:
        print("Output")
        print("False")


def show_dir(Begin , reporter_stack , indep_v , StringOfInput):
    Stack =[indep_v]
    for i in range(1,len(StringOfInput)):
        Stack.append(str(StringOfInput[0:i] + "(" + Begin + reporter_stack[i] + Begin +  ")" + indep_v))
    Stack.append(StringOfInput + indep_v)
    Stack.append(StringOfInput)
    return Stack

if __name__ == "__main__":
main()