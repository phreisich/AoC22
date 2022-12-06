input = open("input.txt", "r").read()

def get_marker_pos(num_unique):
    tmp = ""
    marker_found = False
    for i in input:
        if (marker_found == False):
            tmp += i
            marker_found = len(set(tmp[-num_unique:])) == num_unique
    return(len(tmp))

print(get_marker_pos(4))
print(get_marker_pos(14))
