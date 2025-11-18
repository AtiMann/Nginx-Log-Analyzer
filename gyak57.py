from pathlib import Path
from collections import Counter
from datetime import datetime

def read_log(file_path):
    return Path(file_path).read_text(encoding="utf8").splitlines()

def analyze_log(lines):
    ip_counter = Counter()
    path_counter = Counter()
    status_counter = Counter()
    user_counter = Counter()
    day_counter = Counter()

    for line in lines:
        parts = line.split()
        user_s = line.split('"')
        try:
            ip = parts[0]
            path = parts[6]
            user = user_s[-2]
            parts = line.split()
            status = next((p for p in parts if p.isdigit() and len(p)==3),"-")
            
            


        except IndexError:
            continue
        path_counter [path] += 1
        ip_counter[ip] += 1
        status_counter[status] += 1
        user_counter[user] += 1
    return ip_counter,path_counter,status_counter,user_counter


def print_top(title,counter):
    print (f"\n{title}")
    print("-----------------------------------------")
    for item, count in counter.most_common(5):
        print(f"{item}: {count}")

def save_file(title,counter,formated,file_path = "stat.csv"): #output fájl alapértelmezett érték
    with open(file_path,"a",encoding="utf8")as f:
        f.write(f"\n=={formated}==")
        f.write(f"\n{title}\n")
        f.write(("-----------------------------------------\n"))
        for item,count in counter.most_common(5):
            f.write(f"{item}: {count}\n")

def main():
    
    now = datetime.now()
    formated = now.strftime("%Y-%m-%d %H:%M:%S")
    lines = read_log("ngingx.log") #log fájl beolvasása

    ip_counter,path_counter,status_counter,user_counter = analyze_log(lines)

    print_top("Top 5 IP addresses with the most requests:",ip_counter)
    print_top("Top 5 most requested paths:",path_counter)
    print_top("Top 5 response status codes:",status_counter)
    print_top("Top 5 user agents:" ,user_counter)

    save_file("Top 5 IP addresses with the most requests:",ip_counter,formated)
    save_file("Top 5 most requested paths:",path_counter,formated)
    save_file("Top 5 response status codes:",status_counter,formated)
    save_file("Top 5 user agents:" ,user_counter,formated)

main()