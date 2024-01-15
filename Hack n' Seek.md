# Hack n' Seek
## Challenge Description:
In your goal of becoming a skilled penetration tester, you decided to try your hand at bug bounties.<br>
Browsing through the bug bounties that you received, you noticed one in particular that seemed like an excellent way to start the day.<br>
The target was a WordPress site that appears to have a slightly outdated version.<br>

#### Your goals
☛ Full exploitation of the vulnerability is not part of the challenge.<br>
☛ Search for a critical vulnerability in the WordPress site.<br>
☛ Read about the vulnerability to understand from where the issue originated.<br>
☛ Navigate to the page with the vulnerable code to reveal the flag.<br>

## Process: 
Notice the version of the site in the lower footer 'This website is powered by WordPress core 4.6'.<br>
Search online for 'wordpress 4.6 vulnerability' and one of the first sites you will find will be this one:<br>
https://exploitbox.io/vuln/WordPress-Exploit-4-6-RCE-CODE-EXEC-CVE-2016-10033.html

Scroll down to "IV. DESCRIPTION".
From the text, copy the following snippet 'wp-includes/pluggable.php' and paste it into the URL of the challenge site.

Press enter and you will receive the flag

<details> 
        <summary>Hidden Flag</summary> 
          08f60ae5cf4500ccc86a0601c34855ce
    </details>
