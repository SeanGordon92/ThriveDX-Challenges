# AuthRev
#### Java, python, reverse engineering
## Challenge Description:
In the Reverse Universe, even reverse engineering is reversed. The troll-faced meme died years ago. <br>
﻿His code legacy was hidden in the Reverse Universe. The code contains divine memes that have never been seen before.<br>

Your goals<br>
☛ Find the troll's login info to set the divine memes free!

## Process:
When we download the file we can see that it is a '.CLASS' file, meaning Java. <br>

We need  to decompile the file in order to read it, and I would suggest using https://www.decompiler.com/ <br>
<details> 
        <summary>The Code</summary> 
  (I would suggest viewing the code here in the 'code' tab) <br>
  public class Auth {
    public Auth() {
    }

    public static void main(String[] a) {
        String b = a[0];
        System.out.println(a(b) ? "Authorized" : "Unauthorized");
    }

    private static boolean a(String b) {
        try {
            char[] c = b.toCharArray();
            return c[0] == 'N' && c[5] < 'b' && c[6] == c[0] - 3 && c[10] == c[6] + c[11] / 11 * 3 && c[7] == c[4] + 1 && c[1] ==c[0] + 27 && c[2] > c[1] + 1 && c[3] == c[1] && c[4] == c[1] + (c[0] - 1) / 7 && c[5] > '`' && c[8] == c[7] - 3 && c[9] == c[4] && c[11] > c[0] + 31;
        } catch (RuntimeException var2) {
            return false;
        }
    }
}
    </details><br>

So what now? <br>
We have several options:
1. We can manually go through each variable and find the phrase.
2. Write a python script that will solve the riddle.
3. Ask GPT for aid.

I will present to you both the python script and the manual steps to solve this. <br>
##### Manual 
We will see that the phrase is constructed from a string of up to 11 characters, meaning it is a string of 12 characters. <br>
The phrase is set up with certain conditions, either that can be solved directly or by looping iterations back and forth. <br>
<details>
          <summary>Steps</summary>
1. First character 'N': (c[0] = 'N') (Direct, simple as that). <br>
2. Second character 'i': (c[1] = c[0] + 27) (Direct, 'N' + 27 = 'i'). <br>
3. Third character 'k': (c[2] > c[1] + 1) (Loop, 'k' > 'i' + 1). <br>
4. Fourth character 'i': (c[3] = c[1]) (Direct, 'i'). <br>
5. Fifth character 't': (c[4] = c[1] + (frac{(c[0] - 1)})/{7}) (Direct, 'i' + ('N' - 1)/7 = 't'). <br>
6. Sixth character 'a': (c[5] < 'b' && c[5] > '`') (Loop, 'a' < 'b' and 'a' > '`'). <br>
7. Seventh character 'K': (c[6] = c[0] - 3) (Direct, 'N' - 3 = 'K'). <br>
8. Eighth character 'u': (c[7] = c[4] + 1) (Direct, 't' + 1 = 'u'). <br>
9. Ninth character 'r': (c[8] = c[7] - 3) (Direct, 'u' - 3 = 'r'). <br>
10. Tenth character 't': (c[9] = c[4]) (Direct, 't'). <br>
11. Eleventh character 'i': (c[10] = c[6] + (frac{c[11]}/{11} times 3) (Loop, 'K' + ('n' / 11 * 3)). <br>
12. Twelfth character 'n': (c[11] > c[0] + 31) (Loop, 'n' > 'N' + 31). <br>
</details>  

##### Python script

<details>
  <summary>Script</summary>
    (Again, I would suggest viewing the code here in the 'code' tab): <br>
  def find_valid_string():
    #Initialize an empty character array of length 12
    c = [' '] * 12

    c[0] = 'N'  # Condition 1
    c[1] = chr(ord(c[0]) + 27)  # Condition 6
    c[3] = c[1]  # Condition 8
    c[4] = chr(ord(c[1]) + (ord(c[0]) - 1) // 7)  # Condition 9
    c[7] = chr(ord(c[4]) + 1)  # Condition 5
    c[6] = chr(ord(c[0]) - 3)  # Condition 3
    c[9] = c[4]  # Condition 12
    c[8] = chr(ord(c[7]) - 3)  # Condition 11

    #The remaining conditions have some level of dependency or ranges, so we loop to find valid values
    for c2 in range(ord(c[1]) + 2, 128):  # Condition 7, limiting to ASCII range up to 127
        c[2] = chr(c2)
        for c5 in range(ord('`') + 1, ord('b')):  # Conditions 4 and 10
            c[5] = chr(c5)
            for c11 in range(ord(c[0]) + 32, 128):  # Condition 13
                c[10] = chr((ord(c[6]) + c11 // 11 * 3) % 128)  # Condition 4 (mod 128 to stay in ASCII range)
                c[11] = chr(c11)

                # Check if the final condition is met
                if ord(c[10]) == ord(c[6]) + c11 // 11 * 3:
                    return ''.join(c)


#Run the function to find the valid string
valid_string = find_valid_string()
print("Valid string:", valid_string)
</details>
