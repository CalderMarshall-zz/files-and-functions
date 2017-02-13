hello_file=  open(raw_input("Enter a file name:"))
print "hello_file: %s" % hello_file
hello_content = hello_file.read()
# hello_file.write(raw_input("Type what you want to add."))
hello_file.close()

#letter histogram

def lettergraph():
    word = "%s" %hello_content
    counts = {}
    final = {}
    for char in word:
        counts[char] = counts.get(char, 0) + 1
        for char, count in counts.items():
            final.update({char: count})
    print final


#word histogram

def wordgraph():
    para = "%s" %hello_content
    word_counts = {}

    split_para = para.split()
    for i in split_para:
        word_counts[i] = word_counts.get(i, 0) + 1
    print word_counts
lettergraph()
wordgraph()
