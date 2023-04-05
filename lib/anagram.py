# your code goes here!

class Anagram:
    def __init__(self, name):
        self.name = name

    def match(self,list_of_words):
        #print(list_of_words)
        solutions = []
        for i in list_of_words:
            word_list = list(i)
            word_list.sort()
            name_list = list(self.name)
            name_list.sort()
            if (word_list == name_list):
                solutions.append(i)

        return solutions


    

listen = Anagram("listen")
print (listen.name)
print(listen.match(['enlists', 'google', 'inlets', 'banana']))