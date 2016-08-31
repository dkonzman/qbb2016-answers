
"""
Parse a single FASTA records from stdin and print it
"""


class FASTAReader(object):
    def __init__ (self, file):
        self.file = file
        self.last_id = None
        
    def __iter__(self):
        return self
        
    def next(self):
        if self.last_id is None:
            line = self.file.readline()
            if line == "":
                raise StopIteration
            #verify is header line
            assert line.startswith(">")
            #extract id - take line as a string w/o ">", then split, then take 1st in that split list
            identifier = line[1:].split()[0]
        else:
            identifier = self.last_id

        sequences = []

        #infinite while loop to run through whole file.  make sure break is in there
        while 1:
            line = self.file.readline().rstrip("\r\n")
            if line.startswith(">"):
                self.last_id = line[1:].split()[0]
                break
            elif line == "":
                if sequences:
                    return identifier, "".join(sequences)
                #return None, None
                raise StopIteration
            else:
                sequences.append(line)
                
        return identifier, "".join(sequences)



#reader = FASTAReader(sys.stdin)

#while 1:
#    identifier, sequence = reader.next()
#    if identifier is None:
#        break
#    print identifier, sequence

#for identifier, sequence in reader:
#    print identifier, sequence

