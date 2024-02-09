# Route Me
## Challenge Description:
Recent reports regarding delays in food container production of the "Plastic & Elastic" company led to several changes in the company's network topology.<br>
The topology modification included new networking devices and permissions modifications.<br>
As the company's security specialist, you were requested to verify that the new topology and hierarchy were established securely.<br>
When considering the various cases, your main concern was a compromise of the main router in the network.<br>

#### Your goals<br>
☛ To perform the security evaluation without interrupting the production process, you were provided with an exact replica of the network, and access to 'R2', using the user and password 'Smith:DawaYk'.<br>
☛ Find a way to compromise the router and access the Global Configuration Mode.<br>
☛ Modify the router's configurations to enable access to the web server in the management network from the "tapdb-backup' Server.<br>
☛ Verify the web interface of 'websrv-internal' can be accessed from 'tapdb-backup'.<br>

## Process:
Go to 'R2'. In the CLI press enter. Enter the user and password as seen above.<br>
To gain password for 'enable' options, type 'show running-config'.<br>
Take "080A4D42003B041B1B" and run it through 'https://packetlife.net/toolbox/type7/' to get the reversed password which is "KaliBali".<br>

Execute 'show ip interface brief'.<br>
Enter the config mode by executing 'config t' and then the following commands:<br>
'interface gigabitEthernet 0/1'<br>
'no shutdown'<br>

Return to the main Cicso layout window, and enter the Server-PT.<br>
Go into 'Desktop' tab and click 'web browser'.<br>
In the URL enter the IP 192.168.1.5.<br>

You will be presented with a coupon with the flag inside of it.


