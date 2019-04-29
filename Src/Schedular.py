class Cpuschedule:

    def __init__(self):
        self.data = []  # The queue of process burst time
        self.n = 0  # No of processes

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
        B = list(self.data)
        Wt = [0]
        for i in range(1, int(self.n)):
            temp = int(B[i - 1]) + int(Wt[i - 1])
            Wt.append(temp)
        for i in range(0, int(self.n)):
            Twt = Twt + Wt[i]
        for i in range(0, int(self.n)):
            Bst = Bst + Wt[i]
        print("Total Waiting Time:"+str(Twt))
        print("Average Waiting Time:"+str(Twt/int(self.n)))

        # Shortest job First Algorithm
    def Sjf(self):
        pass

    # Priority Algorithm
    def Priority(self):
        pass

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
    s.getData()
    s.Fcfs()
