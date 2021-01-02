def convert(number):
    drops = ''.join(
        sound 
        for factor, sound in 
            [(3, "Pling"), 
             (5, "Plang"), 
             (7, "Plong")]
        if not number % factor
    )
    return drops if drops \
                 else str(number)
