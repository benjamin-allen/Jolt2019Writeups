# Insane Clown Party
# There are 36^5 possible inputs to test, but luckily they can all be tested in parallel. This program just eats up
# however many cores you have to let the testing happen. Each thread tests passwords starting with a different character,
# so one tests "ca....bv" and the next tests "cb....bv" and the next tests "cc....bv" and so on.

import hashlib
import multiprocessing

chars = "0123456789abcdefghijklmnopqrstuvwxyz"

# This function is called by each thread with a different start_char.
def tfunc(start_char):
    print("Thread started for char " + start_char)
    c1 = start_char
    # loop through all the chars...
    for c2 in chars:
        for c3 in chars:
            for c4 in chars:
                # ...over and over again
                for c5 in chars:
                    s =  "".join(["c", c1, c2, c3, c4, c5, "bv"]) # build a string and hash it
                    output = hashlib.md5(s.encode("utf-8")).hexdigest()
                    if(output[0:4] == "fe0d"):      # then compare it to the known part of the hash
                        if(output[10:] == "3c4f9037aeb3ac211f6ad6"):
                            f = open("candidates_" + start_char + ".txt", "w")
                            print("Candidate Password: " + s)
                            f.write(s + "\n")

if __name__ == "__main__":
    with multiprocessing.Pool(multiprocessing.cpu_count()) as p:
       p.map(tfunc, [x for x in chars])  # Create a thread pool and call tfunc('0'), tfunc('1'), etc...