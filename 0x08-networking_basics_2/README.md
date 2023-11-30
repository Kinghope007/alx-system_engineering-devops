Tasks
0. Change Your Home IP
Objective: Configure an Ubuntu server with the specified requirements.
bash
Copy code
sylvain@ubuntu$ ping localhost
# Before: PING localhost (127.0.0.1)
# After: PING localhost (127.0.0.2)
bash
Copy code
sylvain@ubuntu$ ping facebook.com
# Before: PING facebook.com (157.240.11.35)
# After: PING facebook.com (8.8.8.8)
Script Location:
GitHub Repository: alx-system_engineering-devops
Directory: 0x08-networking_basics_2
File: 0-change_your_home_IP
1. Show Attached IPs
Objective: Display all active IPv4 IPs on the machine.
bash
Copy code
sylvain@ubuntu$ ./1-show_attached_IPs | cat -e
# Example Output:
# 10.0.2.15$
# 127.0.0.1$
Script Location:
GitHub Repository: alx-system_engineering-devops
Directory: 0x08-networking_basics_2
File: 1-show_attached_IPs
2. Port Listening on Localhost (Advanced)
Objective: Write a Bash script that listens on port 98 on localhost.

Usage:

Terminal 0: sudo ./100-port_listening_on_localhost
Terminal 1: telnet localhost 98
Script Location:

GitHub Repository: alx-system_engineering-devops
Directory: 0x08-networking_basics_2
File: 100-port_listening_on_localhost
