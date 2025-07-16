# try:
#     cnt = 0
#     stream = open("C:/Users/luara/Desktop/code/file.txt", "rt")
#     # Processing goes here.
#     content = stream.read(1)
#     while content != "":
#         print(content, end="")
#         cnt += 1
#         content = stream.read(1)
#     stream.close()
#     print("\n\nChareacters in file:", cnt)
# except Exception as exc:
#     print("Cannot open file:", exc)

    

try: # Attempt to open a file for reading
    stream = open("C:/Users/luara/Desktop/code/file.txt", "rt") # Open file in text mode 
    # Processing goes here.
    content = stream.read() # Read the entire file content
    print(content,) # Print the content of the file
        
    stream.close() # Close the file after reading
except Exception as exc: # Handle any exceptions that occur
    print("Cannot open file:", exc)
    