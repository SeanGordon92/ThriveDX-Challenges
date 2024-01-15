![image](https://github.com/SeanGordon92/ThriveDX-Challenges/assets/60423498/5fa92f48-5ae8-437d-b36f-df504e7f0272)# I Am Listening
## Challenge Description:
A couple of days ago, a guy claiming to be a network tech came to our colleague and said he had to review his network configuration. Since then, your colleague complained about abnormal behavior in this system.<br>
At first, he thought it was merely his lack of experience with Ubuntu. However, soon enough, he began suspecting the issue had something to do with the supposed network technician. <br>
He turned to you for advice on how to check the system more thoroughly. 

#### Your goals are:
☛ Find the reason for the abnormal activity in the system.<br>
☛ Find all possible information about the  attacker.<br>
☛ Find any malicious traces the attacker left in the system.<br>

## Process:
To solve this issue, we first ran the command 'netstat -ano' , which will give us  a foreign IP in the response that we must check.<br>
We need to run 'curl [foreign IP]' in order to try to gain more information about it. Curling all other IP's will give us nothing of value.<br>

And we will find the first part of the flag.<br>
<details> 
        <summary>First half of the flag</summary> 
          4d4d0febee7020cc
    </details>

Next step is to run 'ps -x'  in order to see and find all current processes in the machine.<br>
We will notice that there is a process from /bin/bash /tmp/c8WeUfS34K.sh which is suspicious<br>

Reading the file with cat will reveal the 2nd part of the flag<br>
<details> 
        <summary>Second half of the flag</summary> 
          0b1f8acdbd610d80
    </details>
