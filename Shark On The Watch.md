# Shark On The Watch
## Challenge Description:
During a coffee break, your colleague, Boris, teased you and said that he managed to hack your computer earlier that day and planted a hidden file in it. <br>
Since you always lock you computer when you leave, you suspect he did it using a network-related vulnerability. Luckily, company policy includes network traffic monitoring. <br>
The NOC team agreed to provide you with access to the recorded traffic of your computer on the same morning.<br>

#### Your goals are:
☛ Identify what Boris did to hack your computer.<br>
☛ Find the content of the file that Boris planted on your computer.<br>

## Process:
When we start the challenge we will be presented with an open 'Wireshark' GUI with several hundreds if not more logs, one of which will contain the flag. <br>
<kbd align="center">
  <img src="Images/SharkOnTheWatch_01.png"/>
</kbd> 
<br><br>
If you want to look up everything by youself, you can go ahead.<br>
<details> 
        <summary>Rest of the process</summary> 
In the search bar, type in 'tcp.stream eq 1077'.<br>
<br>
<kbd align="center">
  <img src="Images/SharkOnTheWatch_02.png"/>
</kbd> 
<br><br>
You can now see several different logs. One of them has the flag. <br>
<br>
<kbd align="center">
  <img src="Images/SharkOnTheWatch_03.png"/>
</kbd> 
<br><br>

This is the one we need <br>
<br>
<kbd align="center">
  <img src="Images/SharkOnTheWatch_04.png"/>
</kbd> 
<br><br>

<details> 
        <summary>The hidden flag</summary> 
          <kbd align="center">
  <img src="Images/SharkOnTheWatch_05.png"/>
</kbd> 
<br><br>
          0baea2f0ae20150db78f58cddac442a9
    </details>
</details>
