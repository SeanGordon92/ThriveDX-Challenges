# Breaking Hollywood
## Challenge Description:
A few days back, you had an argument with your friend Hernandez about password complexity.<br>
He claimed you would never guess his strong passwords! As a challenge, he had set up an SSH server and secured it with one of his default passwords.

Your goals<br>
☛ You were provided with the user and password 'corey:TcPZ2rrS!' to reconnect if needed.<br>
☛ Create a custom wordlist to use against the accessible SSH service.<br>
☛ Execute a brute-force attack against the SSH service.<br>
☛ Retrieve Hernandez's password, and attempt to log in into the server<br>

## Process:
In the terminal, run 'cupp -i'. '-I' is used to start interactive mode.
We can see in the left screen the info that we will need to fill in the gaps.
In the 'First Name' enter Hernandez.<br>
Keep pressing enter and in 'Pet's name' enter Cachorro<br>
Skip all the rest<br>
No key words<br>
No special chars<br>
No random numbers  in the end<br>
Yes to leet <br>

Now execute the command 'hydra -l hernandez -P hernandez.txt ssh://172.17.0.131:22 -f -v'<br>
'-l hernandez' - specifies the login name.<br>
'-P hernandez.txt' - specifies the file containing the passwords that we created with the cupp command.<br>
'ssh://172.17.0.131:22' - The target webserver and the specific port.<br>
'-f' - Hydra will stop the attack after the first successful login is found.<br>
'-v' - enables verbose mode which causes Hydra to display more detailed information about the attack as it progresses.<br>
<details> 
<summary>You will receive the following output:</summary> 
"[22][ssh] host: 172.17.0.18   login: hernandez   password: c4ch0rr0"
</details>
Run the password through an md5 hash and that is the answer 
    
