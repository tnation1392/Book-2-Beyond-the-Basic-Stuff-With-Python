
def process(data, flag):
    if flag:
        print("Processing data...")

#program does not use boolean logic to lead to the print action
#--------------------------------------------------------------

def process(data, flag):
    if flag is True:
        print("Processing data...")


process(5, True)