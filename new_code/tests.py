import util
from game import Package

def populatePackagesSmall1(queue):
    queue.push(Package((1,1),1),1)
    queue.push(Package((5,5),1),1)
    queue.push(Package((6,5),1),1)
    queue.push(Package((4,2),1),1)
    queue.push(Package((5,2),1),1)
    queue.push(Package((6,2),1),1)
    queue.push(Package((8,2),1),1)
    queue.push(Package((3,1),1),1)

def populatePackagesSmall2(queue):
    queue.push(Package((4,1),1),1)
    queue.push(Package((5,2),1),1)
    queue.push(Package((7,3),1),1)
    queue.push(Package((8,3),1),1)
    queue.push(Package((1,4),1),1)
    queue.push(Package((2,4),1),1)
    queue.push(Package((7,5),1),1)
    queue.push(Package((8,5),1),1)

def populatePackagesSmall3(queue):
    queue.push(Package((2,2),1),1)
    queue.push(Package((3,2),1),1)
    queue.push(Package((6,2),1),1)
    queue.push(Package((8,2),1),1)
    queue.push(Package((1,3),1),1)
    queue.push(Package((2,3),1),1)
    queue.push(Package((3,3),1),1)
    queue.push(Package((5,3),1),1)

def populatePackagesSmall4(queue):
    queue.push(Package((6,3),1),1)
    queue.push(Package((6,4),1),1)
    queue.push(Package((8,4),1),1)
    queue.push(Package((1,5),1),1)
    queue.push(Package((5,1),1),1)
    queue.push(Package((6,1),1),1)
    queue.push(Package((7,1),1),1)
    queue.push(Package((8,1),1),1)

def populatePackagesSmall5(queue):
    queue.push(Package((1,2),1),1)
    queue.push(Package((2,2),1),1)
    queue.push(Package((3,2),1),1)
    queue.push(Package((4,2),1),1)
    queue.push(Package((2,5),1),1)
    queue.push(Package((3,5),1),1)
    queue.push(Package((4,5),1),1)
    queue.push(Package((1,3),1),1)

def populatePackagesMedium1(queue):
    queue.push(Package((17,17),1),1)
    queue.push(Package((17,17),1),1)
    queue.push(Package((1,1),1),1)
    queue.push(Package((1,8),1),1)
    queue.push(Package((4,9),1),1)
    queue.push(Package((17,13),1),1)
    queue.push(Package((17,14),1),1)
    queue.push(Package((17,15),1),1)

def populatePackagesMedium2(queue):
    queue.push(Package((17,16),1),1)
    queue.push(Package((1,13),1),1)
    queue.push(Package((1,12),1),1)
    queue.push(Package((8,4),1),1)
    queue.push(Package((8,15),1),1)
    queue.push(Package((4,5),1),1)
    queue.push(Package((1,11),1),1)
    queue.push(Package((1,10),1),1)

def populatePackagesMedium3(queue):
    queue.push(Package((1,9),1),1)
    queue.push(Package((7,2),1),1)
    queue.push(Package((7,12),1),1)
    queue.push(Package((4,8),1),1)
    queue.push(Package((4,9),1),1)
    queue.push(Package((13,15),1),1)
    queue.push(Package((1,7),1),1)
    queue.push(Package((13,11),1),1)

def populatePackagesMedium4(queue):
    queue.push(Package((17,12),1),1)
    queue.push(Package((8,11),1),1)
    queue.push(Package((17,7),1),1)
    queue.push(Package((7,3),1),1)
    queue.push(Package((7,10),1),1)
    queue.push(Package((8,2),1),1)
    queue.push(Package((17,2),1),1)
    queue.push(Package((13,9),1),1)

def populatePackagesMedium5(queue):
    queue.push(Package((13,16),1),1)
    queue.push(Package((7,11),1),1)
    queue.push(Package((7,13),1),1)
    queue.push(Package((7,15),1),1)
    queue.push(Package((8,1),1),1)
    queue.push(Package((8,3),1),1)
    queue.push(Package((4,6),1),1)
    queue.push(Package((4,7),1),1)

def populatePackagesLarge1(queue):
    queue.push(Package((18,37), 1), 1)
    queue.push(Package((16,14), 1), 1)
    queue.push(Package((32,29), 1), 1)
    queue.push(Package((33,33), 1), 1)
    queue.push(Package((26,25), 1), 1)
    queue.push(Package((37,30), 1), 1)
    queue.push(Package((3,11), 1), 1)
    queue.push(Package((3,27), 1), 1)

def populatePackagesLarge2(queue):
    queue.push(Package((33,24), 1), 1)
    queue.push(Package((12,19), 1), 1)
    queue.push(Package((21,26), 1), 1)
    queue.push(Package((4,10), 1), 1)
    queue.push(Package((34,26), 1), 1)
    queue.push(Package((3,11), 1), 1)
    queue.push(Package((29,13), 1), 1)
    queue.push(Package((14,31), 1), 1)

def populatePackagesLarge3(queue):
    queue.push(Package((21,16), 1), 1)
    queue.push(Package((14,26), 1), 1)
    queue.push(Package((7,25), 1), 1)
    queue.push(Package((2,13), 1), 1)
    queue.push(Package((19,8), 1), 1)
    queue.push(Package((3,27), 1), 1)
    queue.push(Package((35,26), 1), 1)
    queue.push(Package((8,25), 1), 1)

def populatePackagesLarge4(queue):
    queue.push(Package((21,36), 1), 1)
    queue.push(Package((31,29), 1), 1)
    queue.push(Package((15,19), 1), 1)
    queue.push(Package((36,15), 1), 1)
    queue.push(Package((14,27), 1), 1)
    queue.push(Package((35,25), 1), 1)
    queue.push(Package((7,7), 1), 1)
    queue.push(Package((17,35), 1), 1)

def populatePackagesLarge5(queue):
    queue.push(Package((7,14), 1), 1)
    queue.push(Package((32,30), 1), 1)
    queue.push(Package((23,30), 1), 1)
    queue.push(Package((19,20), 1), 1)
    queue.push(Package((27,5), 1), 1)
    queue.push(Package((38,33), 1), 1)
    queue.push(Package((5,32), 1), 1)
    queue.push(Package((1,29), 1), 1)

def populateKA4(queue, even):
    if even:
        queue.push(Package((6,17), 1), 1)
        queue.push(Package((12,18), 1), 1)
        queue.push(Package((4,12), 1), 1)
        queue.push(Package((11,7), 1), 1)
    else:
        queue.push(Package((11,7), 1), 1)
        queue.push(Package((4,12), 1), 1)
        queue.push(Package((12,18), 1), 1)
        queue.push(Package((6,17), 1), 1)

def populateKAtop(queue):
    queue.push(Package((6,17), 1), 1)
    queue.push(Package((12,18), 1), 1)
    queue.push(Package((6,17), 1), 1)
    queue.push(Package((12,18), 1), 1)
    queue.push(Package((6,17), 1), 1)
    queue.push(Package((12,18), 1), 1)

def populateKAbottom(queue):
    queue.push(Package((4,8), 1), 1)
    queue.push(Package((11,7), 1), 1)
    queue.push(Package((4,8), 1), 1)
    queue.push(Package((11,7), 1), 1)
    queue.push(Package((4,8), 1), 1)
    queue.push(Package((11,7), 1), 1)

def populateKA3(queues):
	for q_index in xrange(len(queues)):
		for i in xrange(4):
			if q_index == 0:
				queues[q_index].push(Package((18, 2), 1), 1)
			elif q_index ==1:
				queues[q_index].push(Package((5, 10), 1), 1)
			else:
				queues[q_index].push(Package((6,17), 1), 1)

# Must not use loops or much logic due to initialization race condition with other parts of code
def populateKA4(queues):
	queues[0].push(Package((18, 2), 1), 1)
	queues[0].push(Package((18, 2), 1), 1)
	queues[0].push(Package((18, 2), 1), 1)
	queues[1].push(Package((10, 4), 1), 1)
	queues[1].push(Package((10, 4), 1), 1)
	queues[1].push(Package((10, 4), 1), 1)
	queues[2].push(Package((12,17), 1), 1) #top
	queues[2].push(Package((12,17), 1), 1) #top
	queues[2].push(Package((12,17), 1), 1) #top
	queues[3].push(Package((18,9), 1), 1) 
	queues[3].push(Package((18,9), 1), 1) 
	queues[3].push(Package((18,9), 1), 1) 


def populateKA5(queues):
	queues[0].push(Package((18, 2), 1), 1)
	queues[0].push(Package((18, 2), 1), 1)
	queues[0].push(Package((18, 2), 1), 1)
	queues[1].push(Package((10, 4), 1), 1)
	queues[1].push(Package((10, 4), 1), 1)
	queues[1].push(Package((10, 4), 1), 1)
	queues[2].push(Package((12,17), 1), 1)
	queues[2].push(Package((12,17), 1), 1)
	queues[3].push(Package((4,10), 1), 1)
	queues[3].push(Package((4,10), 1), 1)
	queues[4].push(Package((18,9), 1), 1)
	queues[4].push(Package((18,9), 1), 1)


def distributeKA(queue):
    all_packages = genKA10packagesMedium()
    print all_packages
    total = len(all_packages)
    for queue in queues:
        first = all_packages.pop(0)
        queue.push(first, total)
        total-=1
