from operator import itemgetter
from multiprocessing import Process, Queue
from .puzzle import num_queens_attacked, queen_attacks, perturb, random_board, \
    hill_climb, print_board


def local_beam_search(n=8):
    nb_procs = 4
    procs = []
    task_q = Queue()
    done_q = Queue()

    for t in range(nb_procs):
        p = Process(target=hill_climb, args=(task_q, done_q))
        procs.append(p)

    for t in range(nb_procs):
        task_q.put(random_board(n))

    for p in procs:
        p.start()

    results = []
    solution = None
    while True:
        result = done_q.get()
        if result[0] == True:
            solution = result[1]  
            for t in range(nb_procs):
                task_q.put('STOP')
            break
        else:
            results.append(result)
            if len(results) == nb_procs:
                counts = [(s, num_queens_attacked(s, queen_attacks(s))) for _,s in results]
                counts_sorted = sorted(counts, key=itemgetter(1))
                best = [c[0] for c in counts_sorted[:2]]
                mid = nb_procs // 2
                next_ss = perturb(best[1], mid) + perturb(best[0], nb_procs-mid)
                results.clear()
                for s in next_ss:
                    task_q.put(s)

    print(solution)
    print_board(solution)
