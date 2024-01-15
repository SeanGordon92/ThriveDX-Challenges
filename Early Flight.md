# Early Flight
##Challenge Description: 
"Touch the Sky," a small flight company for cheap flights, has suffered several DoS attacks in the last few months. Despite numerous checks, they were not able to pinpoint the cause of the DOS.<br>
Furthermore, attempts to contact the programmer who originally built the site failed as he is not available<br>
As a last resort, the company decided to hire you in an attempt to identify the possible cause of the occasional DoS.<br>

#### Your goals
☛ Find a way to overload the application to get the flag.

## Process:
Pick locations and dates.<br>
Change in the URL the dates so that you are "going back in time"<br>

For this instance, let's pick Frankfurt ---> Vienna<br>

Pick a 'Depart' date for 3 days from now, and the 'Return by' date to be 4 days later.<br>
Press enter and let the page load.<br>
Go to the URL and there, change the date of the 'to=' section to be 1 or 2 days before the 'from=' section, but still later from the current date.<br>
Press enter and let the page load. <br>
After it loads you should get a 'An error occurred' message with the flag<br>

<details> 
        <summary>GeeksforGeeks</summary> 
          <img align="center" src="Images/Early_Flight_01">
    </details>
