from time import sleep
from numpy.random import default_rng
import QDB

def askQuestion():
    global q
    q = QDB.get_q(qnum[level]);

    print("Question " + str(level+1) + ": " + q[0]);
    sleep(1)
    print("A." + " " + q[1]);
    sleep(1)
    print("B." + " " + q[2]);
    sleep(1)
    print("C." + " " + q[3]);
    sleep(1)
    print("D." + " " + q[4]);
    sleep(1)

    return

def checkAnswer():
    global q, level
    answer = input("your answer: ");

    while (answer.lower() != "a" and answer.lower() != "b" and answer.lower() != "c" and answer.lower() != "d" ):
        answer = input("your answer: ");
    else:
        if(answer.lower() == q[5]):
            if(level == 4):
                print("\nWINNER");
            else:
                print("\nCORRECT\n");
                level = level+1;
                askQuestion();
                checkAnswer();
        else:
            print("Sorry you got it wrong, thanks for playing");



level = 0;
q = [];


print("welcome to who wants to be a millionaire \n")
sleep(1)

rng = default_rng();
qnum = rng.choice(22, size=5, replace=False);

askQuestion();
checkAnswer();
