import os
import re
import threading


class FileParser(threading.Thread):

    def __init__(self, _root, _file, _outputs):
        super().__init__()
        self.stats = {}
        self.file_path = "%s/%s" % (_root, _file)
        self.outputs = _outputs
        self.file_name = _file

    def run(self):
        for line in open(self.file_path, "r").readlines():
            for _word in re.sub("[^\w]", " ", line).split():
                l_word = _word.lower()
                if l_word in self.stats:
                    self.stats[l_word] += 1
                else:
                    self.stats[l_word] = 1
        self.outputs.append((self.stats, self.file_name))


if __name__ == "__main__":

    threads = []
    outputs = []

    for root, dirs, files in os.walk("res"):
        for file in files:
            t = FileParser(root, file, outputs)
            t.start()
            threads.append(t)

    for t in threads:
        t.join()

    print(outputs)

    final_stats = {}
    for stats, file_name in outputs:
        for word in stats.keys():
            if word in final_stats:
                final_stats[word] += stats[word]
            else:
                final_stats[word] = stats[word]

    print(final_stats)

    _max = None

    for key in final_stats:
        if _max is None:
            _max = key
        elif final_stats[key] > final_stats[_max]:
            _max = key

    print("\nThe highest is %s with %i occurrences" % (_max, final_stats[_max]))
