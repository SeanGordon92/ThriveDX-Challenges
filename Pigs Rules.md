##### Note - I no longer have access to the TDX Arena site so I apologise if the images aren't very clear. This is one of the first guides I wrote so I apologise for it being less than stellar
##### Also that note that when I did this there was a bug that prevented the flag from showing
# Pigs Rules
#### Snort, TCPdump, alerting
## Challenge Description:
As a SOC analyst in the "Flying Piglet" post office, you gained intel about Hacktivists throughout the globe who plan to launch a hacking campaign against your country.<br>
To stay ahead, you are required to sniff the ongoing incoming traffic, identify the malicious traffic, and configure Snort IDS rules accordingly.<br>
The rules must not capture any legitimate traffic.<br>
Your goals:


#### Your goals<br>
☛ You are provided with the user and password 'snortoinko1nk" to reconnect if needed. Snorby Credentials:snorby@example.com:snorby<br>
☛ Sniff incoming traffic using TCPdump and identify malicious traffic.<br>
☛ Create a custom Snort rule to alert for malicious traffic.<br>
☛ Read the flag in the Snorby GUI, if Snort was configured correctly.<br>

## Process:
Login with the given credentials. <br>
We will need to add the relevant rules for this challenge. They can be found in '/etc/snort/rules/local.rules' 
<br>
<kbd align="center">
  <img src="Images/Pigs_Rules_01.png"/>
</kbd> 
<br><br>
Let's run 'netstat -a'.<br>
Now we will start running 'sudo tcpdump' and start filtering out all the legitimate looking ports, such as 8443, 22, 80, 3306.<br>
We'll use the command "sudo tcpdump port not '(8443 or 22 or 80 or 3306)' -n"<br>
<br>
<kbd align="center">
  <img src="Images/Pigs_Rules_02.png"/>
</kbd> 

Let's modify it to "sudo tcpdump port not '(8443 or 22 or 80 or 3306)' -n | grep 1024" to show all ports that contain the 1024 size
We will notice that port 36730 repeats itself over and over again.
<br>
<kbd align="center">
  <img src="Images/Pigs_Rules_03.png"/>
</kbd> 
<br>
Now let's edit the Snort rules in order to filter what we need. <br>
Use 'nano /etc/snort/rules/local.rules' to access the rules file for Snort. <br>
'alert tcp any any -> any any (msg:"TCP Windows size is 1024"; sid:1000001; window:1024;)'
<br>
<kbd align="center">
  <img src="Images/Pigs_Rules_04.png"/>
</kbd> 
<br>
And now we'll run the following command
<br>
<kbd align="center">
  <img src="Images/Pigs_Rules_05.png"/>
</kbd> 
<br>
The flag should appear in the 'Sensors' tab, but there is currently an issue that prevents this from happening
<br>
<kbd align="center">
  <img src="Images/Pigs_Rules_06.png"/>
</kbd> 
<br>

<details> 
        <summary>The Hidden Flag</summary> 
          <details> 
            <summary>Did you find the flag yourself?</summary> 
          <details> 
            <summary>I sure hope you did</summary> 
                1fdcf70d937c1d1796a53fb4fdb9e79c
    </details><br>
    </details><br>
    </details><br>
