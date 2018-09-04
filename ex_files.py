with open("resources/file1.txt", "r") as file1, open("resources/file2.txt", "r") as file2, \
        open("resources/file3.txt", "r") as file3, open("resources/out.txt", "w") as out:
    for line0 in file1.readlines():
        for line1 in file2.readlines():
            for line2 in file3.readlines():
                print("%s%s%s" % (line0.rstrip(), line1.rstrip(), line2.rstrip()))
                out.write(line0.rstrip())
                out.write(line1.rstrip())
                out.write(line2.rstrip())
                out.write("\n")
            file3.seek(0)
        file2.seek(0)
