class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded = ""  # create an empty string to store the list of stirngs in continue data format

        for s in strs: # iterate each strings in strs 

            encoded += str(len(s)) + "#" + s # add len + sepatort + strs
        
        return encoded 

    def decode(self, s: str) -> List[str]:

        decoded = [] # intialize empty list to store decoded strings

        i = 0  # i pointer shows where are we right now current position
        while i < len(s): # whenevr i < len(s) mean jb tk i string ki len s chota hai tb tk 

            j = i # temp pointer j help to find separator it iterate and find the separators

            while s[j] != "#":
                j += 1

                # so now we know where is our lenth and our separator 
                #s = "5#Hello5#World"

                #index:
                #    5 # H e l l o

                # ok now we have idea ki hamari string ki lenght kya hai 
            length = int(s[i:j])
                # i = 0
                # j = 1

            i = j + 1
                      # move i after #
            word = s[i:i + length]
                        # find stirng using length

            decoded.append(word)

            i = i + length

        return decoded










