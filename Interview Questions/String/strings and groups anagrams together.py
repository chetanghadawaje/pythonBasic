"""
write a function that takes in an array of strings and groups anagrams together.
Anagrams are strings made up of exactly same characters
Sample input: ["yo","act","flop","cat","oy","tac"]
sample output: [["yo","oy"],["cat","act","tac"]]
"""

def check_anagrams(input1):
    sort_input = ["".join(sorted(i)) for i in input1]
    out_put = []
    process_done = set()
    for i, word in enumerate(sort_input):
        if word not in process_done:
            temp = [input1[j] for j in range(i, len(sort_input)) if word == sort_input[j]]
            if len(temp) > 1:
                out_put.append(temp)
        process_done.add(word)
    print(out_put)

check_anagrams(["yo","act","flop","cat","oy","tac"])
