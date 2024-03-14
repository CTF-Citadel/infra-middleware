# AI-Banking

## Description
```
Josef has built this super awesome web application for a bank.
Apparently his wive fuddled with his application during development.

Can you find an issue?
```

## Writeup

Starting off we should take a look at the website. <br/>
![image](https://github.com/CTF-Citadel/challenges/assets/110562298/44ba1609-1ab5-442c-8e3f-c16e47c5c192)

Looking around we can see a lot of things but skipping ahead we are able to do a directory scan. <br/>
```sh
kali@kali ffuf -w ../wordlists/wordlists/wordlists/discovery/common.txt -u http://127.0.0.1/FUZZ > output.txt

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.0.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://127.0.0.1/FUZZ
 :: Wordlist         : FUZZ: /home/w1sh/wordlists/wordlists/wordlists/discovery/common.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405,500
________________________________________________

:: Progress: [4613/4613] :: Job [1/1] :: 0 req/sec :: Duration: [0:00:00] :: Errors: 0 ::
```

Looking at the directory scan we see that every directory returns a response. <br/>
To get actual directores we can write the output to a file and than grep for a different length than the average response with size `424`. <br/>
```sh
kali@kali grep -v "Size: 434" output.txt

[Status: 301, Size: 169, Words: 5, Lines: 8, Duration: 0ms]
    * FUZZ: api

[Status: 200, Size: 50, Words: 4, Lines: 4, Duration: 0ms]
    * FUZZ: robots.txt

[Status: 301, Size: 169, Words: 5, Lines: 8, Duration: 0ms]
    * FUZZ: static
```

Looking at the robots.txt we can see interesting information. <br/>
```
User-agent: *
Disallow: /

Email: admin@tophack.at
```

Finding this should hint towards the usage in login or maybe some broken access control vulnerability. <br/>
Trying to use a simple SQL-Injection we are able to login using the found email. <br/>
![image](https://github.com/CTF-Citadel/challenges/assets/110562298/13ce5415-c1f4-4ba0-926b-7859cb7e953c)

Getting redirected back to the homepage we can see a new tab called `Profile`. <br/>
![image](https://github.com/CTF-Citadel/challenges/assets/110562298/14d2f673-ef3a-4b51-ab77-4761094b19a1)

Looking at the profile page wee are be able to see the flag which concludes this writeup. <br/>
![image](https://github.com/CTF-Citadel/challenges/assets/110562298/0400199b-1543-4bca-a5f1-8f09b4394a27)

