import numpy as np
import random

def main():
    n = input("Enter the N value")
    n = int(n)
    print("Running for %d iterations", n)
    single_pair = 0
    double_pair = 0
    three_of_a_kind = 0
    four_of_a_kind = 0

    for itr in range(n):
        print("Iteration Number ---------------------{0}".format(itr))
        choice = random.sample(range(20), 5)
        print("choice: \n", choice)
        heatMap = [0, 0, 0, 0, 0]
        for i in range(5):
            a = choice[i] % 5
            heatMap[a] = heatMap[a] + 1

        print("heatMap: \n", heatMap)
        maximum = max(heatMap)
        if maximum > 2:
            if maximum == 4:
                four_of_a_kind = four_of_a_kind + 1
                print("Current Four of a kind: %d \n", four_of_a_kind)
            elif maximum == 3:
                if 2 in heatMap:
                    print("Full-House shouldnt be considered as three of a kind \n")
                else:
                    three_of_a_kind = three_of_a_kind + 1
                    print("Current Three of a kind: %d \n", three_of_a_kind)
        else:
            cnt = 0
            for j in range(len(heatMap)):
                if(heatMap[j] == 2):
                    cnt = cnt + 1;

            if cnt == 2:
                double_pair = double_pair + 1
                print("Current Double pairs: %d \n", double_pair)
            elif cnt == 1:
                single_pair = single_pair + 1
                print("Current Single pairs: %d \n", single_pair)

    print("Probability of Single pairs: %.5f \n", single_pair/n)
    print("Probability of Double pairs: %.5f \n", double_pair/n)
    print("Probability of Three of a kind: %.5f \n", three_of_a_kind/n)
    print("Probability of Four of a kind: %.5f \n", four_of_a_kind/n)


if __name__ == "__main__":
    main()
