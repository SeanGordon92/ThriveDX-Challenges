# Oh My Data
## Challenge Description:
﻿"CyberNT" is a large journalism company that reports the latest cybersecurity news. <br>
Several months ago, the company discovered that its website was hacked and are sure that data was leaked. <br>
However, they are not certain which accounts were compromised and therefore took measures to secure as many accounts as possible. <br>
To be on the safe side, they hired you, a cybersecurity specialist, to verify that the incident was mitigated properly.<br>

#### Your goals<br>
☛ You were provided with the user and password 'student:CyberNT88#!' to reconnect if needed.<br>
☛ Use OSINT to locate the leaked credentials.<br>
☛ Determine if any account is still compromised.<br>

## Process:
When we start the machine we will be presented with this desktop, with this site already open
<br>
<kbd align="center">
  <img src="Images/OhMyData_01.png"/>
</kbd> 
<br><br>
Lets examine the 'Ports' section of the site to see if we can find anything of use there. In the video we saw the name 'stikked' mentioned in an HTML script, so we should keep a lookout for that name.<br>

If we go to the news section and to 'Data Leaks', we will see that very name mentioned as a link. <br>
<br><kbd align="center">
  <img src="Images/OhMyData_02.png"/>
</kbd> 
<br><br>
Clicking it will direct us to their site. There we can search for the name 'CyberNT' as that is the name of the hacked site.<br>
<br><kbd align="center">
  <img src="Images/OhMyData_03.png"/>
</kbd> 
<br><br>
This will reveal a list of leaked email accounts and their passwords.<br>
<br><kbd align="center">
  <img src="Images/OhMyData_04.png"/>
</kbd> 
<br><br>
Download th
<br><kbd align="center">
  <img src="Images/OhMyData_05.png"/>
</kbd> 
<br><br>
We will download this as a txt file. Edit the text file with 'nano' and replace all "--" with ":", so it will be more compatible with Hydra.<br>

Finally, we will use Hydra to brute-force all the users to find at least one that wasn't disabled and can still access the site<br>

hydra -C list.txt cybernt-labs.com -s 443 https-post-form "/api/login:email=^USER^&pass=^PASS^:your account has been disabled" -V<br>
