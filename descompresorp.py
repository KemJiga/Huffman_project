from huffman import HuffmanCoding
import mpi4py.MPI as MPI
import sys, os, time
import pickle

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

path = sys.argv[1]

if rank == 0:
    st = time.time()
    dic_file = open('diccionariop.bin', 'rb')
    dicc = pickle.load(file=dic_file)
    dic_file.close()

    lim = len(dicc)

    clean_dicc = {}
    keys = list(dicc.keys())

    for i in range(1, size):
        comm.send([dicc[keys[0]], keys[0], True], dest=i)
        #print("Enviando: " + str(dicc[keys[0]]) + " " + str(keys[0]) + " a worker " + str(i))
        keys.pop(0)

    values_added = 0
    while values_added < lim:
        data = comm.recv(source=MPI.ANY_SOURCE)
        #print("Recibiendo: " + str(data[0]) + " " + str(data[1]) + " de worker " + str(data[2]))
        clean_dicc[data[1]] = data[0]
        values_added += 1
        #print("Valores agregados: " + str(values_added) + " de " + str(lim))
        if len(keys) > 0:
            comm.send([dicc[keys[0]], keys[0], True], dest=data[2])
            #print("Enviando: " + str(dicc[keys[0]]) + " " + str(keys[0]) + " a worker " + str(data[2]))
            keys.pop(0)
        else:
            comm.send([0, 0, False], dest=data[2])
            #print('Terminando worker ' + str(data[2]))

    comm.barrier()
    #print(clean_dicc)

    h = HuffmanCoding(path)
    output_path = h.decompress_p(input_path=path, clean_dic=clean_dicc)
    ft = time.time()
    print("Decompression time: " + str(round(ft-st, 5)) + "s")

else:
    while(True):
        income_data = comm.recv(source=0)
        #print("Recibiendo: " + str(income_data[0]) + " " + str(income_data[1]) + " de master")
        if income_data[2]:
            income_data[0] = income_data[0].to_bytes(1, 'big')
            comm.send([income_data[0], income_data[1], rank], dest=0)
            #print("Enviando: " + str(income_data[0]) + " " + str(income_data[1]) + " a master")
        else:
            comm.barrier()
            break
