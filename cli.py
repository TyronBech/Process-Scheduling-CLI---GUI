import os
from class_module import cli_input
import algorithms as al
from tabulate import tabulate

class cli_object(object):
    def __init__(self):
        while True:
            os.system("cls")
            print("Process Scheduling Solver")
            print("----------------------------------")
            print("Algorithms:")
            print("A - First Come First Serve")
            print("B - Shortest Job First")
            print("C - Non-Preemtive Priority")
            print("D - Shortest Remaining Time First")
            print("E - Preemtive Priority")
            print("F - Round Robin")
            print("G - Exit")
            choice = input("Enter your choice: ").upper()
            print(f"Your choice: {choice}")
            if choice == "C" or choice == "E":
                inputting = cli_input(is_priority=True)
                sorted_input = sorted(inputting.raw_input, key= lambda x: (x.at, x.p_id))
                result = None
                if choice == "C":
                    result = al.NPP(sorted_input)
                else:
                    result = al.PP(sorted_input)
                list_data = [[p.p_id, p.at, p.bt, p.pr, p.ct, p.tt, p.wt] for p in result.processes]
                header = ["Process ID", "Arrival Time", "Burst Time", "Priority", "Completion Time", "Turnaround Time", "Waiting Time"]
            elif choice == "A" or choice == "B" or choice == "D" or choice == "F":
                if choice == "F":
                    inputting = cli_input(is_priority=False)
                    quantum = int(input("Enter quantum time: "))
                    sorted_input = sorted(inputting.raw_input, key= lambda x: (x.at, x.p_id))
                    result = al.RR(sorted_input, quantum)
                else:
                    inputting = cli_input(is_priority=False)
                    sorted_input = sorted(inputting.raw_input, key= lambda x: (x.at, x.p_id))
                    if choice == "A":
                        result = al.FCFS(sorted_input)
                    elif choice == "B":
                        result = al.SJF(sorted_input)
                    elif choice == "D":
                        result = al.SRTF(sorted_input)
                list_data = [[p.p_id, p.at, p.bt, p.ct, p.tt, p.wt] for p in result.processes]
                header = ["Process ID", "Arrival Time", "Burst Time", "Completion Time", "Turnaround Time", "Waiting Time"]
            elif choice == "G":
                break
            else:
                print("Invalid input, please try again")
            print(tabulate(list_data, headers=header, tablefmt="grid", numalign="center", stralign="center"))
            os.system("pause")