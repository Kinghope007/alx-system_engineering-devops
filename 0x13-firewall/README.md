0. Block all incoming traffic but
To configure the ufw firewall on web-01 to block all incoming traffic except for ports 22 (SSH), 443 (HTTPS SSL), and 80 (HTTP), follow these steps:

SSH into your web-01 server.

Install ufw if it's not already installed:

sql
Copy code
sudo apt update
sudo apt install ufw
Enable ufw:

bash
Copy code
sudo ufw enable
Set up the firewall rules:

bash
Copy code
sudo ufw allow 22/tcp
sudo ufw allow 443/tcp
sudo ufw allow 80/tcp
sudo ufw deny in from any to any
These commands allow traffic on ports 22, 443, and 80, and deny all other incoming traffic.

Verify the rules:

lua
Copy code
sudo ufw status verbose
This command will display the current ufw rules.

1. Port forwarding (Advanced)
To configure web-01 to forward port 8080/TCP to port 80/TCP, you need to modify the ufw configuration file. Here's how to do it:

SSH into your web-01 server.

Open the ufw configuration file using a text editor (e.g., nano):

bash
Copy code
sudo nano /etc/ufw/before.rules
Add the following lines to the file:

less
Copy code
*nat
:PREROUTING ACCEPT [0:0]
-A PREROUTING -p tcp --dport 8080 -j REDIRECT --to-port 80
COMMIT
These lines set up NAT (Network Address Translation) rules to redirect traffic from port 8080 to port 80.

Save and close the file (in nano, you can do this by pressing Ctrl + X, then Y to confirm, and Enter to save).

Restart ufw to apply the changes:

bash
Copy code
sudo ufw disable
sudo ufw enable
Verify that the port forwarding is working:

Use netstat or curl to confirm that port 8080 traffic is being forwarded to port 80.

Copy code
netstat -lpn
