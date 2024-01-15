# All Ears
## Challenge Description:
During a thread hunting project within the local network of 'PlugHD' a headphone manufacturer, you identified an encrypted data stream between two computers. <br>
When trying to locate the physical computers themselves, nobody, including you, managed to find any trace of the suspected stations. <br>
After a prolonged search, you decided to try a different approach and intercept the data rather than finding the computers themselves.<br>

Your goals:<br>
☛ Identify the two target computers on the network.<br>
☛ Find a way to obtain secrets shared between the two computers.<br>


## Process:
Checking 'sudo -l' shows that we have the following option:<br>
(root) NOPASSWD: /usr/bin/ettercap, /usr/sbin/netdiscover.<br>

Let's start with 'ifconfig' to see what our IP is. Now with that IP, we will place it in 'nmap -sn [IP]'.<br>
This will find us "Nmap scan report for game-45057_receiver_1.game-45057_default".

Executing 'sudo netdiscover' will find the true target which will hold the secrets that were passed between the two machines.<br>
Since we can see it is also an ARP connection, we will use ettercap.<br>
'sudo ettercap -T -M arp ///[IP]'
