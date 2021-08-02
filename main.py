import networkx as nx
import matplotlib.pyplot as plt
from termcolor import colored
from pyfiglet import Figlet
import os
os.system('cls')

class Main :
    FileData = ''
    edgeList = dict()
    nodes = 0
    edges = 0
    def __init__(self) :
        with open('input.txt', 'r') as file :
            self.FileData = file.read().strip()
        i=0
        j=0
        for L in self.FileData.strip().split('\n') :
            for B in L.strip().split() :
                if int(B) == 1 :
                    self.edgeList[self.edges] = list()
                    self.edgeList[self.edges].append(j)
                    self.edgeList[self.edges].append(i)
                    self.edges += 1
                i += 1
            self.nodes += 1
            i = 0
            j += 1

    def ShowIT(self):
        G = nx.DiGraph()
        i=0
        j=0
        for L in self.FileData.strip().split('\n') :
            for B in L.strip().split() :
                if int(B) == 1 :
                    G.add_edge(j+1,i+1)
                i += 1
            i = 0
            j += 1
        nx.draw(G  , with_labels=True,  node_shape="s",  node_color="none", bbox=dict(facecolor="skyblue", edgecolor='black', boxstyle='round,pad=0.2'))
        plt.draw()
        plt.savefig("OutPut.png", format="PNG")
        plt.show()

    def GetMaxV(self) :
        MyDict = dict()
        V = 0
        for L in self.FileData.strip().split('\n') :
            for B in L.strip().split() :
                if int(B) == 1 :
                    if V in MyDict :
                        MyDict[V] += 1
                    else :
                        MyDict[V] = 1
            V += 1
        MaxIndex = 0
        MaxV = 0
        for i,j in MyDict.items():
            if j > MaxV :
                MaxV = j
                MaxIndex = i
        return 'vertex No. '+str(MaxIndex+1)+' with '+str(MaxV)+' edges.'

    def GetIncidence(self) :
        MyRes = ''
        for V in range(self.nodes) :
            for E in range(self.edges-1):
                if V in self.edgeList[E] :
                    MyRes += '1 '
                else :
                    MyRes += '0 '
            MyRes += '\n'
        return MyRes

    def GetAllv(self) :
        MyDict = dict()
        V = 0
        for L in self.FileData.strip().split('\n') :
            for B in L.strip().split() :
                if int(B) == 1 :
                    if V in MyDict :
                        MyDict[V] += 1
                    else :
                        MyDict[V] = 1
            V += 1
        MainResult = '-All vertex with their degree :\n\n'
        for i,j in MyDict.items():
            MainResult += 'vertex '+str(i+1)+' -> '+str(j)+'\n'
        return MainResult

    def Connectivity(self):
        MyList = [self.edgeList[0][0]]
        for L in self.edgeList.values():
            if L[0] == self.edgeList[0][0] and L[1] not in MyList:
                MyList.append(L[1])
            if L[1] == self.edgeList[0][0] and L[0] not in MyList:
                MyList.append(L[0])
        for i in MyList.copy() :
            for L in self.edgeList.values():
                if L[0] == i and L[1] not in MyList:
                    MyList.append(L[1])
                if L[1] == i and L[0] not in MyList:
                    MyList.append(L[0])
        if len(MyList) == self.nodes :
            return True
        else :
            return False

    def HaveCycle(self) :
        visited = [0]
        connected = dict()
        temp = dict()
        counter = 0
        while True :
            if counter >= self.nodes :
                return False
            for node in visited :
                connected[node] = []
                for L in self.edgeList.values() :
                    if node == L[0] :
                        connected[node].append(L[1])
                for newN in connected.values():
                    for i in newN :
                        temp[i] = []
                        for L in self.edgeList.values():
                            if i == L[0] :
                                temp[i].append(L[1])
                for newN in visited :
                    for L in temp.values():
                        for i in L :
                            if i == newN :
                                return True
                visited = []
                for i in connected.values():
                    for k in i :
                        visited.append(k)
                connected = dict()
                for i,j in temp.items():
                    connected[i] = list()
                    for k in j :
                        connected[i].append(k)
                temp = dict()
            counter += 1

    def CoLorinG(self) :
        MyNodes = dict()
        for i in range(self.nodes) :
            MyNodes[i] = list()
            for L in self.edgeList.values() :
                if L[0] == i and L[1] not in MyNodes[i] :
                    MyNodes[i].append(L[1])
                if L[1] == i and L[0] not in MyNodes[i] :
                    MyNodes[i].append(L[0])
        
        ColorsList = ['Blue','Red','Black','Pink','Orange','White','Brown','Gray','Purple','Yellow','Green']
        Result = {0:ColorsList[0]}
        UsedColorsIndex = 1
        for node in range(self.nodes) :
            if node in Result.keys() :
                continue
            for i in MyNodes[node] :
                if i == node-1 :
                    for colorINDEX in range(UsedColorsIndex) :
                        if Result[node-1] != ColorsList[colorINDEX] :
                            Result[node] = ColorsList[colorINDEX]
                            continue
                    Result[node] = ColorsList[UsedColorsIndex]
                    UsedColorsIndex+=1
                else :
                    Result[node] = ColorsList[UsedColorsIndex-1]
        return Result

    def Bipartite(self) :
        MyList = list()
        for color in self.CoLorinG().values() :
            if color not in MyList :
                MyList.append(color)
        if len(MyList) == 2 :
            return True
        else :
            return False



while True :
    os.system('cls')
    print(colored(Figlet().renderText('Graph Assistant'), 'green'))
    print('Hi , welcome to my program.')
    print('Please choose an option :\n')
    print('\t1-Show the input graph graphically')
    print('\t2-Show all vertex degree')
    print('\t3-Show the vertex of the graph with the highest degree')
    print('\t4-Show incidence matrix')
    print('\t5-Does the graph have connectivity')
    print('\t6-Does the input graph have a cycle?')
    print('\t7-Is the input graph a tree?')
    print('\t8-Coloring graph')

    user_input = int(input('\n\t> '))
    MyClass = Main()

    if user_input == 1 :
        os.system('cls')
        MyClass.ShowIT()
        input(colored('\nPress on enter button to continue', 'red'))
    if user_input == 2 :
        os.system('cls')
        print('\n' + MyClass.GetAllv() )
        input(colored('\nPress on enter button to continue', 'red'))
    if user_input == 3 :
        os.system('cls')
        print('\n' + MyClass.GetMaxV() )
        input(colored('\nPress on enter button to continue', 'red'))
    if user_input == 4 :
        os.system('cls')
        print('Your incidence matrix:\n')
        print(MyClass.GetIncidence())
        input(colored('\nPress on enter button to continue', 'red'))
    if user_input == 5 :
        os.system('cls')
        if MyClass.Connectivity() :
            print('Its have Connectivity.')
        else :
            print('Its havnt Connectivity.')
        input(colored('\nPress on enter button to continue', 'red'))
    if user_input == 6 :
        os.system('cls')
        if MyClass.HaveCycle() :
            print('It have a cycle.')
        else :
            print('It havnt cycle.')
        input(colored('\nPress on enter button to continue', 'red'))
    if user_input == 7 :
        os.system('cls')
        if MyClass.Connectivity() and MyClass.HaveCycle() == False :
            print('It is a Tree. \U00002705')
        else :
            print('It is not a Tree.')
        input(colored('\nPress on enter button to continue', 'red'))
    if user_input == 8 :
        os.system('cls')
        for node,color in MyClass.CoLorinG().items() :
            print(str(node+1) + ' -> ' + color)
        print('\n')
        if MyClass.Bipartite() :
            print ('\tIts a bipartite graph.')
        else :
            print('\tIts not a bipartite graph.')
        input(colored('\nPress on enter button to continue', 'red'))