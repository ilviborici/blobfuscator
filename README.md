# Blobfuscator
Python code obfuscation


# Settings ⚙

 - recursion: How many times to encrypt, keep this below 100 at most, because it will start taking a long amount of time to run
 
 - base: what Base system to use during encryption, must be a whole number, can go all the way up to infinity, unless you disable `bytes_allowed`. 
    ⚠ The higher the base the longer it'll take to run, generally keep it below 1024

 - indent: hides code by using indents to space out the code so its harder to see inside an IDE.
 
 - bytes_allowed: Wether or not the program is allowed to use byte characters
