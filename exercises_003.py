def exercise_300():

    # let's make a spell! eye of newt, wing of bat!

    # here is a list of body parts. 
    body_parts = ["eye", "wing"]

    # we can add to it like this
    body_parts.append("toe")

    # TASK 1. Use the "append" function to add some new body parts to the list.
    # (ADD YOUR CODE HERE)

    # TASK 2. Create a new variable called "animals", containing a list of animal names. Use the "print" function and
    # run your script to show your animals list
    # (ADD YOUR CODE HERE)

    # TASK 3. Uncomment the following line to print the first ingredient
    # of your spell - rerun your script to see it.
    
    # print("{} of {}".format(body_parts[0]+animals[0])

    # TASK 4. print out some of the other spell ingredients.

def exercise_301():

    # using dictionaries

    # in the real world, a dictionary maps word names to their defintions. In python, a dictionary maps "keys" to "values"
    # for example:

    spell_dictionary = {
        "bat" : "Ugly animal with wings, good for flying spells",
        "frog": "Another ugly animal, but might turn into a beautiful person if you kiss it", 
    }

    # we know that we can find the length of a list using the "len" function. we can use the same function to
    # find the lenght of a dictionary.

    # TASK 1. Uncomment the following line to print the length of the spell dictionary. Run the script to see this.
    # print(len(spell_dictionary))

    # we use numbers to get the values from a list, like my_value=my_list[5]. but when we want the values from
    # a dictionary, we use the keys instead, like in the next line.

    description  = spell_dictionary["bat"]

    # TASK 2. Add another line of code to print the description of the bat. Run the script to see this.
    # (ADD YOUR CODE HERE)

    # TASK 3. Go back and add some different animals to the spell_dictionary. use the print function and rerun
    # the script to display some of them.

def exercise_302():

    # TASK 1. Write some code of your own that uses a dictionary to match some "keys" to some "values"
    # and do something interesting with them.
    print()

exercise_300()
exercise_301()
    
