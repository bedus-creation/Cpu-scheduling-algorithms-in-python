class Cpuschedule:

    def __init__(self):
        # Default Data set
        # self.data = [10, 2, 3, 4, 4, 6, 7, 8, 9, 5]
        # self.n = 10  # No of processes
        # The queue of process burst time
        self.data = []
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
        aTat = 0.0
        Wt = [0]
        Tat=[0]
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
        w=0.0
        B = []
        P = []
        self.n=4
        self.n = int(input("Enter the no of processes:\n"))
        pMax=6
        # B = [5,4,2,4]
        # P = [4,2,6,3]
        Wt = [0]*self.n
        for i in range(int(self.n)):
            b, p = input("Enter The BurstTime and Priority for Process p" + str(i)+"\n").split()
            B.append(int(b))
            P.append(int(p))
            if pMax<int(p):
                pMax=int(p)

        print(B)
        print(P)

        for j in range(pMax):
            for i in range(0,self.n):
                if P[i]==j:
                    Wt[i]=w
                    w=w+B[i]
        # Sort the process according to their priority
        # for i in range(int(self.n)):
        #     for j in range(1,int(self.n)):
        #         if P[j - 1] < P[j]:
        #             temp = B[j - 1]
        #             B[j - 1] = B[j]
        #             B[j] = temp
        # Wt = [0]
        # for i in range(1, int(self.n)):
        #     temp = int(B[i - 1]) + int(Wt[i - 1])
        #     Wt.append(temp)
        # print(Wt)
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

    # Shortest job First Algorithm with Preemption
    def SjfP(self):
        pass

    # Shortest job First Algorithm with NonPreemption
    def SjfNp(self):
        pass

    # Round Robin Algorithm
    def RoundRobin(self):
        Twt = 0
        Bst = 0.0
        w=0.0
        Tat = [0]
        aTat=0.0
        Wt = [0]
        quantum=4
        B = list(self.data)
        rem_bt = list(self.data)
        t = 0 # Current time  
        while(1): 
            done = True
            for i in range(int(self.n) ): 
                if (int(rem_bt[i]) > 0) : 
                    done = False # There is a pending process 
                    if (int(rem_bt[i]) > quantum) : 
                        t += quantum  
                        rem_bt[i] =int(rem_bt[i])- quantum  
                    else: 
                        t = t + int(rem_bt[i])  
                        Wt.append(t - int(B[i]))  
                        rem_bt[i] = 0                
            if (done == True): 
                break
        for i in range(int(self.n)+1):
            Twt = int(Twt) + int(Wt[i])
        for i in range(int(self.n)): 
            temp=int(B[i]) + int(Wt[i])
            Tat.append(temp)
            aTat = aTat + Tat[i]  

        print("Total Waiting Time:"+str(Twt))
        print("Average Waiting Time:"+str(Twt/int(self.n)))
        print("Total Turnaround Time:"+str(aTat))
        print("Average Turnaround Time:"+str(aTat/int(self.n)))
    

    def Wrr(self):
        Twt=0
        aTat=0
        Tat = []
        B = []
        W=[]
        rem_bt = []
        time = 0
        self.n=5 # Can Comment Out
        quantum=1 # Can Comment Out
        # B=[1,2,3,4,5] # Can Comment Out
        # W=[1,2,3,4,5] # Can Comment Out
        self.n = int(input("Enter the no of processes:\n"))
        quantum = int(input("Enter the value For Quantum:\n"))
        for i in range(int(self.n)):
            b, p = input("Enter The BurstTime and Weight for Process p" + str(i)+"\n").split()
            B.append(int(b))
            W.append(int(p))
        Wt = [0]*self.n
        rem_bt = list(B)

        while (1):
            done = True
            for t in range(0, int(self.n)):
                if rem_bt[t] > 0:
                    done = False
                    if W[t] > 0:
                        quantum *= W[t] 
                    if rem_bt[t] > quantum:
                        time += quantum
                        rem_bt[t] -= quantum
                    else:
                        time += rem_bt[t]
                        Wt[t] = time - B[t]
                        rem_bt[t] = 0
            if done == True:
                break
        for i in range(self.n):
            Twt = int(Twt) + int(Wt[i])
        for i in range(int(self.n)): 
            temp=int(B[i]) + int(Wt[i])
            Tat.append(temp)
            aTat = aTat + Tat[i]  
        print("Total Waiting Time:"+str(Twt))
        print("Average Waiting Time:"+str(Twt/int(self.n)))
        print("Total Turnaround Time:"+str(aTat))
        print("Average Turnaround Time:"+str(aTat/int(self.n)))
        

