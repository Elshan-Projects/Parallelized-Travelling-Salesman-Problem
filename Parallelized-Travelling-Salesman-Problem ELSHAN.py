from itertools import permutations
import time
import multiprocessing

def calculate1(given_routes,graph,s,w1):
	kk = 0
	for i in given_routes:		
		current = 0
		k = s
		for j in i:
			current = current + graph[k][j]
			k = j
		current = current + graph[k][s]
		w1[kk] = current
		kk = kk+1

def calculate2(given_routes,graph,s,w2):
	qq = 0
	for i in given_routes:		
		current1 = 0
		k = s
		for j in i:
			current1 = current1 + graph[k][j]
			k = j
		current1 = current1 + graph[k][s]
		w2[qq] = current1
		qq = qq+1


if __name__ == "__main__":

    N = 4
    s = 0
    cities = []
    for i in range(N):
    	if i != s:
    		cities.append(i)
    
    all_routes=permutations(cities)
    routes_l = list(all_routes)
    
    graph1 = [[0, 20, 15, 22], [12, 0, 40, 25], [36, 30, 0, 50], [12, 35, 20, 0]]
    ll = len(routes_l)//2
    paths1 = routes_l[:ll]
    paths2 = routes_l[ll:]
    
    w1 = multiprocessing.Array('d', ll)
    w2 = multiprocessing.Array('d', ll)
    
    
    #################################################### 
    p1 = multiprocessing.Process(target=calculate1, args=(paths1, graph1,s,w1))
    p2 = multiprocessing.Process(target=calculate2, args=(paths2, graph1,s,w2))
    
    p1.start()
    p2.start()
    
    t1 = time.time()
    p1.join()
    p2.join()
    t2 = time.time()

    ww = list(w1)+list(w2)
    ##################################
    Minimum = min(ww)
    Name_ind = ww.index(Minimum)
    Name = routes_l[Name_ind]
    Weight = ww[Name_ind]
    print("The shortest route is: ", Name)
    print("w = ",Weight)
    
    print("Time Elapsed (Parallel): ", t2-t1)

