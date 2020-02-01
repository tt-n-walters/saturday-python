#           Code Execution Timer
#           Created by Nico Walters
#           21/09/2019

from datetime import datetime
from sys import argv
from importlib import import_module

module_to_test = argv[2].strip(".py")
print("Module to test: \"" + module_to_test + "\".")

start_time = datetime.now()
print("Starting at: " + str(start_time))

imported = import_module(module_to_test) # Will import the file specified in the variable
if hasattr(imported, "main"):
    imported.main()
else:
    print("The specified file has no entry method named \"main\".")
    

end_time = datetime.now()
print("Finished at: " + str(end_time))

time_taken = end_time - start_time
print("The operation took " + str(time_taken) + " to complete.")
