'''This programme takes as input a blurb from a movie and compares it with the blurb from a list of movies 
(I have included the input blurb for debugging). It then uses the en_core_web_md model to compare semantic
similarity between the blurbs and recommend the most appropriate next movie for the user to watch'''


#--------------------import and load modules and models------------------------------------
import spacy

spacy.load("en_core_web_md")

import en_core_web_md

#-----------------------define functions ----------------------------------

def watch_next(movie):
    '''This function takes as input the description of a movie in the form of a string and then reads from
The file, movies.txt and tells you which of these movies to watch next based on their semantic similarity'''
    
    #define nlp
    nlp = en_core_web_md.load()
    #apply to input movie
    doc1 = nlp(movie)

    #open movies.txt
    with open ("movies.txt", "r+")  as g:
        
        #initialise max_sim
        max_sim = 0
        #for each line, extract the blurb using split and apply nlp. Then calculate the similarity between this blurb
        #and the input blurb. If this is the highest yet, update max_sim
        for line in g:
            doc2 = nlp(line.split(":")[1])
            similarity = doc2.similarity(doc1)
            #print the similarities for interest
            print(f"{similarity} : {line}")
            if similarity > max_sim:
                max_sim = similarity
                max_movie = line.split(":")[0]
    #explain to user that they should watch the movie with the maximum semantic similarity next
    print (f"\nYou should watch {max_movie} next.\n")






def main():

    '''This programme initialises planet hulk with a given blurb and inputs it into watch_next'''

    planet_hulk = """Will he save their world or destroy it?
When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace.
Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."""

    watch_next(planet_hulk)


main()