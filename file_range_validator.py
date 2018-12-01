"""
File Downloader

- Suppose that you are writting a p2p file downloader that downloads a file from a number of peers. Each peer has a portion of the file available, but they are not complete, and may overlap. For each download request, your downloader will reach to a number of peers to retrieve the file. Your job is to write a function that give the offsets of all the downloaded file portions, and check the download is complete.


Input:
File Ranges:
        ------
   --------
          --------------
------------------
                    ----------------
                           ----------------

File Size
-------------------------------------------

Output:
True


Input:
File Ranges:
        ------
   --------
          --------------
------------------
                    -----
                           ----------------

File Size
-------------------------------------------

Output:
False
"""


# Solution
# input: arr = [(0,2), (1,3)], filesize=3


def check_file(ranges, filesize):
    ranges = sorted(ranges, key=lambda x: x[0])
    if len(ranges) is 0 or ranges[0][0] > 0: # missing ranges or missing range at beginning of file
        return False

    cur_buffer = ranges[0][1]

    for r in ranges:
        if r[0] > cur_buffer:
            return False # break in ranges
        if r[1] > cur_buffer:
            cur_buffer = r[1]

    if cur_buffer < filesize:
        return False #missing range at end of file

    return True

# Unit test
r1 = [(0,2), (1,3)]
f1 = 3
print(check_file(r1,f1))

# Missing at begninning
r2 =  [(1,2), (1,3)]
f2 = 3
print(check_file(r2,f2))

# Missing at end
r3 = [(0,2), (2,6)]
f3 = 7
print(check_file(r3,f3))

# Mising in middle
r4 = ([0,4], [3,5], [6,8])
f4 = 8
print(check_file(r4,f4))

