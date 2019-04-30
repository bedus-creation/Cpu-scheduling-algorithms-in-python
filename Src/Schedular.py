class Cpuschedule:

    def __init__(self):
        # The queue of process burst time
        self.data = [10, 2, 3, 4, 4, 6, 7, 8, 9, 5]
        self.n = 10  # No of processes

    # Getting the No of processes & burst time
    def getData(self):
        self.n = input("Enter the no of processes:\n")
        for i in range(int(self.n)):
            temp = input("Enter The BurstTime for Process p" + str(i)+"\n")
            self.data.append(temp)

    # First come First served Algorithm
    def Fcfs(self):
        Twt = 0.0
        Bst = 0.0
        Tat = 0.0
        Wt = [0]
        B = list(self.data)
        for i in range(1, int(self.n)):
            temp = int(B[i - 1]) + int(Wt[i - 1])
            Wt.append(temp)
        for i in range(0, int(self.n)):
            Twt = Twt + Wt[i]
        for i in range(0, int(self.n)):
            Bst = Bst + Wt[i]
        for i in range(0, int(self.n)):
            Tat = Wt[i]+int(B[i])

        print("Total Waiting Time:"+str(Twt))
        print("Average Waiting Time:"+str(Twt/int(self.n)))
        print("Total Turnaround Time:"+str(Tat))
        print("Average Turnaround Time:"+str(Tat/int(self.n)))

    # Shortest job First Algorithm
    def Sjf(self):
        # Sort the brust time
        Twt = 0.0
        Bst = 0.0
        Tat = 0.0
        Wt = [0]
        B = list(self.data)
        for i in range(int(self.n), 0, -1):
            for j in range(1, int(self.n)):
                if B[j - 1] > B[j]:
                    temp = B[j - 1]
                    B[j - 1] = B[j]
                    B[j] = temp
        Wt = [0]
        for i in range(1, int(self.n)):
            temp = int(B[i - 1]) + int(Wt[i - 1])
            Wt.append(temp)
        for i in range(0, int(self.n)):
            Twt = Twt + Wt[i]
        for i in range(0, int(self.n)):
            Bst = Bst + Wt[i]
        for i in range(0, int(self.n)):
            Tat = Wt[i]+int(B[i])

        print("Total Waiting Time:"+str(Twt))
        print("Average Waiting Time:"+str(Twt/int(self.n)))
        print("Total Turnaround Time:"+str(Tat))
        print("Average Turnaround Time:"+str(Tat/int(self.n)))

    # Priority Algorithm
    def Priority(self):
        Twt = 0.0
        Bst = 0.0
        Tat = 0.0
        Wt = [0]
        B = []
        P = []
        self.n = input("Enter the no of processes:\n")
        for i in range(int(self.n)):
            temp = input("Enter The BurstTime for Process p" + str(i)+"\n")
            B.append(temp)
            temp = input("Enter The Priority for Process p" + str(i)+"\n")
            P.append(temp)

    # Shortest job First Algorithm with Preemption
    def SjfP(self):
        pass

    # Shortest job First Algorithm with NonPreemption
    def SjfNp(self):
        pass

    # Round Robin Algorithm
    def RoundRobin(self):
        pass


if __name__ == "__main__":
    s = Cpuschedule()
    # s.getData()
    # s.Fcfs()
    # s.Sjf()
    s.Priority()
