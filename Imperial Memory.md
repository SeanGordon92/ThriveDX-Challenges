# I Am Listening
## Challenge Description:
Jules, a cyber researcher, left his office on his way to a new job. At his farewell party, he was speechless but managed to express his love for everyone he worked with.<br>
After his farewell party, you approach him and ask "What is the secret of your success?" Jules laughed and promised that the next day the answer would be on your desktop.<br>
The next day you discover a file on your desktop with a note that says "Always keep this in your memory".<br>

#### Your goals are:<br>
☛ You are provided with the user and password 'derrek:r3s3arch3r' to reconnect if needed.<br>
☛ Inspect the dump file to find clues for unlocking the archive file.<br>
☛ Analyze & Investigate the DOCX file.<br>

## Process:
When we start the machine we will be presented with an Ubuntu desktop, and we can see 2 files that stand out: 'Emperor.vmem' and 'gift.7z'. <br>
<img align="center" src="Images/Imperial _Memory_01.png"><br>

Inside the 'gift.7z' file, we can find a DOCX file named 'suspicious.docx', which we cannot extract without the password. <br>
<img align="center" src="Images/Imperial _Memory_02.png"><br>

In order to find the password, we will have to analyze the 'Emperor.vmem' file. <br>
As it turns out, a vmem file is the virtual machine's paging file, which backs up the guest main memory on the host file system. We can start analyzing it using 'volatility', but I found that it is not necessary for this challenge. <br> 

To transcribe the vmem file, we will use 'strings' with a few given chose words in order to search for anything that might be useful to us.<br>
<img align="center" src="Images/Imperial _Memory_03.png"><br>

Upon opening the output of the strings command, we will be presented with an extremely long and mostly unintelligible text. <br>
<img align="center" src="Images/Imperial _Memory_04.png"><br>

Lets start searching for things that might be related to the 'gift.7z' file. <br>
#### Please take note that using CTRL+W in the site to try searching for individual instances of the word will close your tab. I imported the output file using file.io/ from the station to my own Linux machine.

After finding multiple instances of the mentioned file, we will finally a reference to the file with it's password completely visible <br>
<details> 
        <summary>gift.7z password</summary> 
          <img align="center" src="Images/Imperial _Memory_05.png">
    </details>
<br>

Now we can extract the file and have a look at it. <br>
<img align="center" src="Images/Imperial _Memory_06.png"><br>
But alas, the file is empty, aside from the text at the top proclaiming "I am empty!".<br>
Analyzing the file will also give us nothing.

One thing that we can do, however, is reformat the file. Since docx files are essentially ZIP archives containing XML and other various files, we can replace the '.docx' with '.7z' and unzip the contents of the file.<br>
<img align="center" src="Images/Imperial _Memory_07.png"><br>
When we look at the new files, amongst the various XML files, we are presented with a txt file named "secrects".
<img align="center" src="Images/Imperial _Memory_08.png"><br>

These are Jules' secrets that he promised to share with us. While the file itself doesn't contain our flag, the file itself IS the flag. 
Let's run the command 'md5sum secrets.txt' to get the MD5 hash of the file. This is our flag
<details> 
        <summary>The hidden flag</summary> 
          <img align="center" src="Images/Imperial _Memory_09.png"><br>
          0f235385d25ade312a2d151a2cc43865
    </details>

