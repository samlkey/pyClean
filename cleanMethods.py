from os import listdir

def Run(params):
    if params["dir"] != "":
        print("Running at Location " + params["dir"])
        contents = [f for f in listdir(params["dir"])]

