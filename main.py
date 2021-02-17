import pygame
import sys
import random

v = 121
adj = [[] for i in range(v)]


def Translator(param):
    translatorCounter = 0
    for alpha in range(11):
        for beta in range(11):
            list2 = [beta, alpha]
            if param == list2:
                return translatorCounter
            translatorCounter += 1


def CatTranslator(param):
    translatorCounter = 0
    for alpha in range(11):
        for beta in range(11):
            list2 = [beta, alpha]
            if param == translatorCounter:
                return list2
            translatorCounter += 1


def add_edge(adj, src, dest):
    adj[src].append(dest);
    adj[dest].append(src);


def delete_edge(src):
    adj[src].clear()
    for i in range(len(adj)):
        if src in adj[i]:
            adj[i].remove(src)


def BFS(adj, src, dest, v, pred, dist):
    queue = []
    visited = [False for i in range(v)];

    for i in range(v):
        dist[i] = 1000000
        pred[i] = -1;

    visited[src] = True;
    dist[src] = 0;
    queue.append(src);

    while (len(queue) != 0):
        u = queue[0];
        queue.pop(0);
        for i in range(len(adj[u])):

            if not visited[adj[u][i]]:
                visited[adj[u][i]] = True;
                dist[adj[u][i]] = dist[u] + 1;
                pred[adj[u][i]] = u;
                queue.append(adj[u][i]);

                if (adj[u][i] == dest):
                    return True;

    return False;


def printShortestDistance(adj, s, dest, v):
    pred = [0 for _ in range(v)]
    dist = [0 for i in range(v)];

    if not BFS(adj, s, dest, v, pred, dist):
        print("Given source and destination are not connected")

    path = []
    crawl = dest;
    path.append(crawl);

    while pred[crawl] != -1:
        path.append(pred[crawl]);
        crawl = pred[crawl];

    print("Shortest path length is : " + str(dist[dest]), end='')

    print("\nPath is : : ")
    for i in range(len(path) - 1, -1, -1):
        print(path[i], end=' ')


def ShortestDistance(adj, s, dest, v):
    pred = [0 for i in range(v)]
    dist = [0 for i in range(v)];

    if not BFS(adj, s, dest, v, pred, dist):
        print(s, dest, dist[dest])

    path = []
    crawl = dest;
    path.append(crawl);

    while (pred[crawl] != -1):
        path.append(pred[crawl]);
        crawl = pred[crawl];

    point = [dist[dest], path[len(path) - 2]]
    return point


def add_all_edges():
    for x in range(120):
        if x % 10 != 0 or x == 0:
            add_edge(adj, x, x + 1)
        if x < 110:
            add_edge(adj, x, x + 11)
    # counter = 0
    # for x in range(120):
    #     if counter != 10 and x < 110:
    #         add_edge(adj, x, x + 12)
    #         counter += 1
    #     else:
    #         counter = 0
    counter = 0
    for x in range(11):
        for y in range(11):
            if (x % 2 != 0):
                if counter < 109:
                    add_edge(adj, counter, counter + 12)
                    counter += 1
            else:
                if counter < 110:
                    add_edge(adj, counter, counter + 10)
                    counter += 1


def NextHop(source):
    best = 1000001
    destination = 0
    for x in range(11):
        score = ShortestDistance(adj, source, x, v)
        if best > score[0]:
            best = score[0]
            destination = score[1]
        score = ShortestDistance(adj, source, x + 110, v)
        if best > score[0]:
            best = score[0]
            destination = score[1]
        score = ShortestDistance(adj, source, x + (1 + x) * 10, v)
        if best > score[0]:
            best = score[0]
            destination = score[1]
        score = ShortestDistance(adj, source, x + x * 10, v)
        if best > score[0]:
            best = score[0]
            destination = score[1]
    if(best == 1000000):
        return -1
    else:
        return destination

def drawCat(CatPosition):
    if CatPosition[1] % 2 == 0:
        gameDisplay.blit(cat, (35 + 50 * CatPosition[0], 35 + 50 * CatPosition[1]))
    else:
        gameDisplay.blit(cat, (60 + 50 * CatPosition[0], 35 + 50 * CatPosition[1]))

def PaintDeletes():
    for x in range(len(deleteEdges)):
        usun = deleteEdges[x]
        pos = CatTranslator(usun)
        if pos[1] % 2 == 0:
            pygame.draw.circle(gameDisplay, red, (75 + 50 * pos[0], 75 + 50 * pos[1]), 25)
        else:
            pygame.draw.circle(gameDisplay, red, (100 + 50 * pos[0], 75 + 50 * pos[1]), 25)

def PaintBoard():
    gameDisplay.fill(black)
    for x in range(11):
        for y in range(11):
            if y % 2 == 0:
                pygame.draw.circle(gameDisplay, GREEN, (75 + 50 * x, 75 + 50 * y), 25)

            else:
                pygame.draw.circle(gameDisplay, GREEN, (100 + 50 * x, 75 + 50 * y), 25)
    PaintDeletes()


#
#
#
#
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
char = pygame.image.load('standing.png')
clock = pygame.time.Clock()


if __name__ == '__main__':
    add_all_edges()

    source = 60

    pygame.init()

    white = (255, 255, 255)
    black = (252, 240, 109)

    red = (189, 255, 209)
    GREEN = (66, 245, 158)
    blue = (0, 0, 255)

    gameDisplay = pygame.display.set_mode((720, 720))
    cat = pygame.image.load('R1.png')
    gameDisplay.fill(black)

    randomList = []
    for x in range(120):
        if(x!=60):
            randomList.append(x)
    deleteEdges = random.sample(randomList, 25)

    for x in range(len(deleteEdges)):
        usun = deleteEdges[x]
        delete_edge(usun)


    PaintBoard()
    print("kot na pozycji", source)
    CatPosition = CatTranslator(source)
    gameDisplay.blit(cat, (65 + 50 * CatPosition[0], 50 * CatPosition[1] + 35))
    while True:
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()
                    if ((pos[1] -50) // 50) % 2 == 0:
                        param = [(pos[0] - 50) // 50, (pos[1] - 50) // 50]
                    else:
                        change = pos[0] - 25
                        param = [(change- 50) // 50, (pos[1]- 50) // 50]
                    usun = Translator(param)
                    deleteEdges.append(usun)
                    if (source != usun):
                        delete_edge(usun)
                    PaintBoard()
                    if(source != NextHop(source)):
                        source = NextHop(source)
                    else:
                        pygame.quit()
                        quit()
                    if(source == (-1)):
                        pygame.quit()
                        quit()
                    else:
                        CatPosition = CatTranslator(source)
                        drawCat(CatPosition)

                    pygame.display.flip()

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()


        pygame.display.update()
    # while True:
    #     print("kot na pozycji", source)
    #     usun = input("jaki wierzcholek usunac?")
    #     delete_edge(int(usun))
    #     source=NextHop(source)
