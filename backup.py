
import subprocess
import os

if __name__ == "__main__":

    with open("paths.txt", "r") as f:
        paths = f.readlines()
    
    
    for path in paths:
        
        path = path.strip()
        name = path.split("/")[-1] 
        
        if os.path.exists(name+".tar.gz.gpg"):
            print("Skipping folder '%s' as it was already processed (delete <...>.gpg to backup again)."%path)
            continue
            
        print("Compressing '%s'..."%path)
        
        subprocess.run(["tar", "-czf", name+".tar.gz", path])
        
        print("Encrypting...")
                
        subprocess.run(["gpg", "-e", "--recipient", "<enter recepient>", "--yes", "--trust-model", "always", name+".tar.gz"])
        
