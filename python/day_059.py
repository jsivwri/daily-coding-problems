# JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 59

# This problem was asked by Google.

# Implement a file syncing algorithm for two computers over a low-bandwidth network. What if we know the files in the two computers are mostly the same?

def open_data(file_name):
    f = open(file_name, "r")
    return f.read()

def num_to_char(num):
    if num > 93:
        raise ValueError
    else:
        return chr (33 + num)

def char_to_num(char):
    return ord(char) - 33

def create_hash(data):
    
    hash_output = ""
    hash_cache = [0]*15
    hash_cache_pointer = 0
    pointer = 0
    pointer_bit_depth = 32
    cache = 0
    
    for val in data:
        if pointer % pointer_bit_depth == 0 and pointer > 0:
            hash_cache[hash_cache_pointer % len(hash_cache)] += cache
            hash_cache_pointer += 1
            cache = 0
        cache += ord(val)
        pointer += 1

    for index in range(len(hash_cache)):
        hash_output += num_to_char(hash_cache[index] % 94)

    hash_output += num_to_char(len(data)%94)

    return hash_output

def data_split(data, frame_size=256):
    data_frames = []
    while(len(data) > 0):
        data_frames += [data[:frame_size]]
        data = data[frame_size:]

    return data_frames 

def create_hash_dictionary(data, frame_size=256):
    hash_dictionary = {}
    data_frames = data_split(data)

    frame_count = 0

    for data_frame in data_frames:
        hash_dictionary[frame_count] = create_hash(data_frame)

        frame_count += 1

    hash_dictionary['frame_size'] = frame_size
    hash_dictionary['frame_count'] = frame_count
    
    return hash_dictionary

def locate_hashes(data, hash_dictionary):
    frame_data = {}
    unlocated_frames = {}

    frame_size = hash_dictionary['frame_size']
    frame_count = hash_dictionary['frame_count']

    unlocated_frames_indexes = [frame for frame in range(frame_count)]

    index_set = range(len(data))[:]

    for count in range(frame_count):
        source_hash = hash_dictionary[count]

        for index in index_set:
            destination_hash = create_hash(data[index:frame_size+index])

            if destination_hash == source_hash:
                indexes_to_remove = range(index, frame_size+index)
                for index in indexes_to_remove:
                    try:
                        index_set.remove(index)
                    except:
                        pass
                frame_data[count] = data[index:frame_size+index]
                unlocated_frames_indexes.remove(count)
                break

    for frame in unlocated_frames_indexes:
        unlocated_frames[frame] = None

    return frame_data, unlocated_frames

def supply_missing_frames(data, missing_frames):
    data_frames = data_split(data)

    for key in missing_frames:
        missing_frames[key] = data_frames[key]

    return missing_frames

def rebuild_file(hash_dictionary, frame_data, supplied_missing_frames):
    output_file = ""


    for frame in range(hash_dictionary['frame_count']): 
        if frame in frame_data.keys():
            output_file += frame_data[frame]
        
        elif frame in supplied_missing_frames.keys():
            output_file += supplied_missing_frames[frame]

        else:
            print("Missing frame:")
            print(frame)

    return output_file

def save_file(data, filename):
    with open(filename, 'w') as f:
        f.write(data)


## CHANGE TO FILE_1 MADE To LINE 1 and LINE 1601 and LINE 2500

# Computer_1 opens file1 and creates hash_dictionary
file1 = open_data("./resources/day_059_file1.txt")
hash_dictionary = create_hash_dictionary(file1)


# After tx of hash_dictionary:
## Computer_2 opens file2 and locates file_1 hashes in that file
## then returns a dictionary of the data corresponding to each hash
## and a list of the missing indexes
file2 = open_data("./resources/day_059_file2.txt")
frame_data, missing_frames = locate_hashes(file2, hash_dictionary)

# After tx of requested missing_frames:
## Computer_1 supplies missings frames
supplied_missing_frames = supply_missing_frames(file1, missing_frames) 

# After tx of supply of missing_indexes
## Computer_2 rebuilds the file using it's data file, frame_data and supplied data
rebuilt_file2 = rebuild_file(hash_dictionary, frame_data, supplied_missing_frames)
save_file(rebuilt_file2, "./resources/day_059_rebuilt_file2.txt")