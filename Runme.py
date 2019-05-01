from src.Schedular import Cpuschedule
class Runme:
    def __init__(self):
        self.schedular= Cpuschedule()
    
    def run(self):
        while True:
            print("\n SIMULATION OF CPU SCHEDULING ALGORITHM")
            print(" Menu:")
            print(" 1. FCFS.")
            print(" 2. SJF Normal.")
            print(" 3. Priority Algorithm.")
            print(" 4. SJF with Preemption.")
            print(" 5. SJF with NonPreemption.")
            print(" 6. RoundRobin.")
            print(" 7. Quit.")
            ch = int(input(" Select : "))

            if ch == 1:
                self.schedular.getData()
                self.schedular.Fcfs()
            elif ch == 2:
                self.schedular.getData()
                self.schedular.Sjf()
            elif ch == 3:
                self.schedular.Priority()
            elif ch == 4:
                self.schedular.getData()
                # print("Not Implemented yet.")
            elif ch == 5:
                self.schedular.getData()
                # print("Not Implemented yet.")
            elif ch == 6:
                self.schedular.getData()
                self.schedular.RoundRobin()
            elif ch == 7:
                print(" See you soon.")
                break
            else:
                print("Invalid Keywords.") 

if __name__ == "__main__":
    Runme().run()