from time import sleep
import QDB

def askQuestion():
    global q
    q = QDB.get_q(level);

    print("Question " + str(level+1) + ": " + q[0]);
    print("A." + " " + q[1]);
    print("B." + " " + q[2]);
    print("C." + " " + q[3]);
    print("D." + " " + q[4]);

    return

def checkAnswer():
    global q, level
    answer = input("your answer: ");

    while (answer.lower() != "a" and answer.lower() != "b" and answer.lower() != "c" and answer.lower() != "d" ):
        answer = input("your answer: ");
    else:
        if(answer == q[5]):
            if(level == 4):
                print("WINNER");
            else:
                print("CORRECT\n");
                level = level+1;
                askQuestion();
                checkAnswer();
        else:
            print("Sorry you got it wrong, thanks for playing");



level = 0;
q = [];


print("welcome to who wants to be a millionaire \n")
sleep(1)

askQuestion();
checkAnswer();
