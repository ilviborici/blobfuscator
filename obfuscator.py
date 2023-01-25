import random, math
from tqdm import tqdm
from tkinter import filedialog
import customtkinter
import configparser



config = configparser.ConfigParser()
config.read('config.env')
recursioninput = config.get('SETTINGS', 'RECURSION')
recursion=int(recursioninput)
baseinput = config.get('SETTINGS', 'BASE')
base = int(baseinput)
indentinput = config.get('SETTINGS', 'INDENT')
indent = int(indentinput)
bytes_allowed = config.get('SETTINGS', 'BYTES_ALLOWED')


app = customtkinter.CTk() 
app.geometry("400x340")
app.resizable(False, False)
app.title("Blobfuscator")



    
def rest():
        app.quit()
        
        
def filepick():
     global inputfile
     inputfile = filedialog.askopenfilename(filetypes=[('Python Files', '*.py')])
    
     
     return inputfile
 
 
frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=20, fill="both", expand=True)

button_1 = customtkinter.CTkButton(master=frame_1, text="Choose File",command=filepick)
button_1.pack(pady=20, padx=10)

button_2 = customtkinter.CTkButton(master=frame_1, text="Apply Obfuscation", command=rest)
button_2.pack(pady=70, padx=10)


app.mainloop()


     
if bytes_allowed:
    key = characters = list(map(chr, range(94, 94 + base)))
else:
    key = characters = list(map(chr, range(33, 34 + base)))

blacklist = ["'", "`", "\\"]

for item in blacklist:
    if item in key:
        key.remove(item)
        base -= 1

random.shuffle(key)
highest = 0
       
     

code = open(inputfile, "rb").read().decode() 

         
def encode(x, base):
                    global highest
                    if not x:
                        return key[0]
    
                    log = math.floor(math.log(x, base))
    
                    st = [0] * (log + 1)
                    st[-1] = 1
                    if log:
                        x -= base**log
    
                    while True:
                        if x >= base:
                            log = math.floor(math.log(x, base))
                            x -= base**log
                            st[log] += 1
                        else:
                            st[0] = x
                            return "".join([str(key[char]) for char in st[::-1]])
                        return key
    
    
def decode(x, base):
                    result = 0
                    for count, char in enumerate(str(x)[::-1]):
                        result += int(key.index(str(char))) * (base**count)
    
                    return result
                    
    
enc2 = " ".join([str(encode(ord(chr), base)) for chr in "exec"])
enc3 = " ".join([str(encode(ord(chr), base)) for chr in "compile"])

for n in tqdm(range(recursion)):
    enc = "`".join([str(encode(ord(chr), base)) for chr in code])

    if n + 1 == recursion:
        message = f"pass{'  '*indent};"
    else:
        message = ""
    src = f"""{message}k='{''.join(key)}';(eval(eval(''.join([chr(sum([k.index(str(ch))*({base}**c) for c, ch in enumerate(str(x)[::-1])]))for x in('{enc3}'.split(' '))]))(''.join([chr(sum([k.index(str(ch))*({base}**c) for c, ch in enumerate(str(x)[::-1])]))for x in('{enc2}'.split(' '))]), "", "eval")))(eval(''.join([chr(sum([k.index(str(ch))*({base}**c) for c, ch in enumerate(str(x)[::-1])]))for x in('{enc3}'.split(' '))]))(''.join([chr(sum([k.index(str(ch))*({base}**c) for c, ch in enumerate(str(x)[::-1])]))for x in('{enc}'.split('`'))]), "", "exec"))"""
    code = src.replace("-.", "-1")


with open("output.py", "wb") as file:
    file.write(src.encode())


