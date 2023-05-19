from huffman import HuffmanCoding
import mpi4py.MPI as MPI
import sys, os, time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

path = sys.argv[1]

def divide_file(filename, n):
    filename, file_extension = os.path.splitext(filename)
    chunk_size = 0
    file_size = 0
    file_chunks = []

    # Determine file size
    with open(filename + file_extension, 'rb') as file:
        file.seek(0, 2)
        file_size = file.tell()

    # Calculate chunk size
    chunk_size = file_size // n

    # Create new files for writing
    file_names = []
    for i in range(n):
        f = filename + "_part" + str(i+1)
        file_names.append(f)
        file_chunks.append(open(f, 'wb'))

    # Divide the file into chunks
    with open(filename + file_extension, 'rb') as file:
        for i in range(n):
            chunk_data = file.read(chunk_size)
            file_chunks[i].write(chunk_data)

    # Close all files
    for file_chunk in file_chunks:
        file_chunk.close()

    #print('names: ',file_names)
    return file_names
    #print(f"The file '{filename}' has been divided into {n} parts.")


if rank == 0:
    st = time.time()
    files_chunks = divide_file(path,  size)
    trash_files = files_chunks.copy()
    part_tag = 1
    for i in range(1, size):
        comm.send([files_chunks[0], part_tag, True], dest=i)
        #print('sending', files_chunks[0], 'to', i, 'with tag', part_tag)
        part_tag += 1
        files_chunks.pop(0)
    
    part_tag -= 1
    to_order_dic = {}
    while len(files_chunks) > 0 or len(to_order_dic) < size:
        data = comm.recv(source=MPI.ANY_SOURCE)
        #print('reciving data from', data[1], 'with tag', data[2])
        freq = data[0]
        worker = data[1]
        tag = data[2]
        part_tag += 1

        to_order_dic[tag] = freq

        if len(to_order_dic) < size - 1 and part_tag <= size:
            comm.send([files_chunks[0], part_tag, True], dest=worker)
            #print('sending', files_chunks[0], 'to', worker, 'with tag', part_tag)
            files_chunks.pop(0)
        else:
            comm.send([0,0,False], dest=worker)
            #print('sending end signal to', worker)

    comm.barrier()
    sorted_dics = dict(sorted(to_order_dic.items(),key=lambda x:x[0],reverse = False))
    #print(sorted_dics)

    for f in trash_files:
        if os.path.exists(f):
            os.remove(f)

    global_dic = sorted_dics[1]
    sorted_dics.pop(1)
    for dic in sorted_dics:
        for val in sorted_dics[dic]:
            if not val in global_dic:
                global_dic[val] = 0
            global_dic[val] += sorted_dics[dic][val]
    #print(global_dic)

    h = HuffmanCoding(path)
    output_path = h.compress_p(global_dic)
    ft = time.time()
    print(ft-st)


else:
    while(True):
        income_data = comm.recv(source=0)
        file = open(income_data[0], 'rb')
        #print('reciving', income_data[0], 'from', 0, 'with tag', income_data[1])

        if income_data[2]:
            text = file.read()
            frequency = {}
            for character in text:
                if not character in frequency:
                    frequency[character] = 0
                frequency[character] += 1

            file.close()
            comm.send([frequency, rank, income_data[1]], dest=0)
        else:
            comm.barrier()
            #print('Ending processing in worker', rank)
            break