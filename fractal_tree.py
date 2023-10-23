import matplotlib.pyplot as plt
import numpy as np






class node:
    def __init__(self, name, pos):

        self.name = name
        self.pos = pos # as np.array

class fractal_tree:
    def __init__(self, alpha, gamma, depth):

        self.alpha = round(2*np.pi*alpha/360,2)
        #self.alpha = alpha
        self.gamma = gamma
        self.depth = depth

    def grow(self, hist = "yx", move = "1"):
        # next step, hist is who you are in this iteration, call is your child
        call = hist + move

        # break recursion if depth is reached
        if len(call) > self.depth:

    
            return None

        # initialize
        if call == "yx1":

            self.nodes = {}
            self.Xs = []
            self.Ys = []

            self.nodes["y"] = node("y", np.array([0,0]))
            self.nodes["yx"] = node("yx", np.array([0,1]))

            plt.figure(dpi=1500)
            plt.plot([0,0], [0,1], 'b', linestyle="-", linewidth = 5/len(call))
            plt.axis('off')

        # get parents name
        par = hist[:-1]
        
        # get parent position
        A = self.nodes[par].pos

        # get own position
        B = self.nodes[hist].pos

        self.Xs.append(B[0])
        self.Ys.append(B[1])

        v1 = B-A
        n1 = np.linalg.norm(v1)

        n2 = n1 * (1+ self.gamma * np.math.cos(self.alpha)) 

        c = np.sqrt( n2**2 / n1**2 )

        v2 = c * v1

        v3 = v2 - v1

        if move == "1":
            alf = -self.alpha
        else: alf = self.alpha
        
        # create rotation matrix
        R = np.array( [[np.math.cos(alf),-np.math.sin(alf)],
                       [np.math.sin(alf), np.math.cos(alf)]] )
        
        v4 = R@v3 / np.math.cos(self.alpha)

        # calc poistion of child
        C = B + v4

        self.Xs.append(C[0])
        self.Ys.append(C[1])

        # plot line between hist and call
        
        plt.plot([B[0],C[0]], [B[1],C[1]], 'b', linestyle="-", linewidth = 5/len(call)**1.2)
        
        plt.plot([-B[0],-C[0]], [B[1],C[1]], 'b', linestyle="-", linewidth = 5/len(call)**1.2)

        xlim = abs(max(self.Xs))+0.1
        ylim = abs(max(self.Ys))+0.1
        plt.xlim(-xlim, xlim)
        plt.ylim(-0.1, ylim)
        plt.gca().set_aspect('equal', adjustable='box')
        


        # create child node
        self.nodes[call] = node(call, C)

        # recursion step
        #print(call)
        self.grow(hist = call, move = "0")
        #print(call)
        self.grow(hist = call, move = "1")



    
