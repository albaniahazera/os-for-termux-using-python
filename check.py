import time, termcolor, platform, os
from termcolor import colored

# check python version
def check_python():
    os.system("clear")
    print("checking python version on device !\n")
    time.sleep(1)
    print(f"Python version: {platform.python_version()}\n")

# check device 
def time_checking():
    time.sleep(1)
    print("Loading device info...\n")
    

def checking_device():    
<<<<<<< HEAD
    print(colored("━━" * 28, "green"))
    print(colored("\t\t\tDevice Info\n", "light_magenta", attrs=["bold"]))
    time.sleep(0.5)
    name_os_color = colored(platform.system(), "light_cyan")
    name_os_relase_color = colored(platform.release(), "light_cyan")
    print(f"OS                    : {name_os_color} {name_os_relase_color}")
=======
    print(colored("-" * 57, "green"))
    print("\t\t\tDevice Info\n")
    time.sleep(0.8)
    print(f"OS                    : {platform.system()} {platform.release()}")
>>>>>>> fc65cd97b029ec212737f6ca9d6d6fa577405f37
    def get_model_name():
        with open("/proc/cpuinfo", "r") as cpuinfo:
            for line in cpuinfo:
                if "Model name" in line:
                    model_name = line.split(":")[1].strip()
                    return model_name
                elif "model name" in line:
                    model_name = line.split(":")[1].strip()
                    return model_name
    model_name = get_model_name()
<<<<<<< HEAD
    time.sleep(0.6)
    model_name_color = colored(model_name, "light_cyan")
    print(f"Chipset architecture  : {model_name_color}")
=======
    time.sleep(0.9)
    print(f"Chipset architecture  : {model_name}")
>>>>>>> fc65cd97b029ec212737f6ca9d6d6fa577405f37
    def get_total_ram():
        with open("/proc/meminfo", "r") as meminfo:
            for line in meminfo:
                if "MemTotal" in line:
                    mem_total = int(line.split()[1])
                    return mem_total
<<<<<<< HEAD
    memory = get_total_ram()
    time.sleep(0.7)
    mem_total = (memory / 1024)
    if mem_total <= 2:
        mem_total_colored = colored(f"{mem_total} MB", "light_red")
    elif mem_total >= 4:
        mem_total_colored = colored(f"{mem_total} MB", "light_red")                
    else:
        mem_total_colored = colored(f"{mem_total} MB", "light_red")

    print(f"Total RAM             : {mem_total_colored}")
    print(colored("━━" * 28, "green"))

if __name__ == "__name__":
    check_python()
    time_checking()
    checking_device()
=======
    mem_total = get_total_ram()
    time.sleep(1)
    print(f"Total RAM             : {mem_total / 1024} MB")
    print(colored("-" * 57, "green"))
>>>>>>> fc65cd97b029ec212737f6ca9d6d6fa577405f37
