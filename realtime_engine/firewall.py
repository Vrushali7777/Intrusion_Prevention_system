import subprocess

def block_ip(ip):

    cmd = ["sudo","iptables","-A","INPUT","-s",ip,"-j","DROP"]

    subprocess.run(cmd)

    print(f"Blocked attacker {ip}")