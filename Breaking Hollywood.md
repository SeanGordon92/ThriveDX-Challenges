# Breaking Hollywood
## Challenge Description:
A few days back, you had an argument with your friend Hernandez about password complexity.
He claimed you would never guess his strong passwords! As a
challenge, he had set up an SSH server and secured it with one of his default passwords.

Your goals
☛ You were provided with the user and password 'corey:TcPZ2rrS!' to reconnect if needed.
☛ Create a custom wordlist to use against the accessible SSH service.
☛ Execute a brute-force attack against the SSH service.
☛ Retrieve Hernandez's password, and attempt to log in into the server

## Process:
In the terminal, run 'cupp -i'. '-I' is used to start interactive mode.
We can see in the left screen the info that we will need to fill in the gaps.
In the 'First Name' enter Hernandez.
Keep pressing enter and in 'Pet's name' enter Cachorro
Skip all the rest
No key words
No special chars
No random numbers  in the end
Yes to leet 

Now execute the command 'hydra -l hernandez -P hernandez.txt ssh://172.17.0.131:22 -f -v'
'-l hernandez' - specifies the login name.
'-P hernandez.txt' - specifies the file containing the passwords that we created with the cupp command.
'ssh://172.17.0.131:22' - The target webserver and the specific port.
'-f' - Hydra will stop the attack after the first successful login is found.
'-v' - enables verbose mode which causes Hydra to display more detailed information about the attack as it progresses.

You will receive the following output:
"[22][ssh] host: 172.17.0.18   login: hernandez   password: c4ch0rr0"

Run the password through an md5 hash and that is the answer 
