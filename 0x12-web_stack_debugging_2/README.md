Project: 0x12. Web stack debugging #2
This project aims to tackle web stack debugging challenges on an Ubuntu 20.04 LTS environment. Below are the tasks completed along with their descriptions:

Task 0: Run software as another user
A Bash script is created to accept one argument.
The script runs the whoami command under the user passed as an argument.
Example Usage:

bash
Copy code
$ ./0-iamsomeoneelse www-data
Task 1: Run Nginx as Nginx
The task involves fixing a container so that Nginx runs as the less privileged nginx user.
Nginx is configured to listen on all active IPs on port 8080.
After debugging:

bash
Copy code
$ ps auxff | grep ngin[x]
nginx      884  0.0  0.0  77360  2744 ?        Ss   19:16   0:00 nginx: master process /usr/sbin/nginx
nginx      885  0.0  0.0  77712  2772 ?        S    19:16   0:00  \_ nginx: worker process
nginx      886  0.0  0.0  77712  3180 ?        S    19:16   0:00  \_ nginx: worker process
nginx      887  0.0  0.0  77712  3180 ?        S    19:16   0:00  \_ nginx: worker process
nginx      888  0.0  0.0  77712  3208 ?        S    19:16   0:00  \_ nginx: worker process
bash
Copy code
$ nc -z 0 8080 ; echo $?
0
Project Structure:

Copy code
.
├── 0-iamsomeoneelse
└── 1-run_nginx_as_nginx

