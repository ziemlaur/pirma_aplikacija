# Write an assert statement that triggers an AssertionError if the variable spam is an integer less than 10.
# assert type(spam) == int and spam >= 10, "spam must be an integer 10 or greater."

# 2. Write an assert statement that triggers an AssertionError if the variables eggs and bacon contain strings 
# that are the same as each other, even if their cases are different
# (that is, 'hello' and 'hello' are considered the same, and 'goodbye' and 'GOODbye' are also considered the same).
# assert eggs.lower() != bacon.lower(), "eggs and bacon cannot be the same ."

# 3. Write an assert statement that always triggers an AssertionError.
# assert False, "This assertion always fails."

# 4. What are the two lines that your program must have in order to be able to call logging.debug()?
# import logging
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)
# s -  %(message)s')

# 5. What are the two lines that your program must have in order to have logging.debug() send a logging 
# message to a file named programLog.txt?
# import logging
# logging.basicConfig(filename='programLog.txt', level=logging.DEBUG, format='
# %(asctime)s -  %(levelname)s -  %(message)s')

# 6. What are the five logging levels?

# DEBUG
# INFO
# WARNING
# ERROR
# CRITICAL


# 7. What line of code can you add to disable all logging messages in your program?
# logging.disable


# 8. Why is using logging messages better than using print() to display the same message?
# Logging can include timestamps and other details automatically, You can easily change where the messages go, 
# clean and efficient, You can turn logging on or off


# 9. What are the differences between the Step Over, Step In, and Step Out buttons in the debugger?
# Step Over: Executes the current line of code and moves to the next line in the same function, 
#      skipping over any function calls.
# Step In: Moves into the function called on the current line, allowing you to debug inside that function.
# Step Out: Executes the remaining lines in the current function and returns to the caller function, stopping there.

# 10. After you click Continue, when will the debugger stop?
# The debugger will stop when it hits the next breakpoint, 
# encounters an unhandled exception, or when the program finishes execution.

# 11. What is a breakpoint?
# A breakpoint is a designated point in the code where the debugger will pause execution,
# allowing you to inspect variables, evaluate expressions, and control the flow of execution.

# 12. How do you set a breakpoint on a line of code in Mu?
#click on the line number in the editor where you want the 
#breakpoint to be, which will place a small dot or marker on that line.