# 3..2..1...Blastoff (or not)

A classic "intro to looping" problem is a simple count to ten exercise. One
slight step up from this is the count down from 10. And of course the fun way to
do this is a rocket countdown to blastoff.

But rockets are, umm, like literally *rocket science*. And things can and do go
wrong. Often quite spetacularly. In your program, you will have essentially a
90% chance of a successful countdown and blastoff. But 10% of the time,
something's gonna go wrong.

 > The `time.sleep()` function is a way to force your program to pause for a
 > specified number of seconds. To use it just import sleep from time and call
 > it by passing in the number of seconds to pause. E.g., `sleep(1)`.
 >
 > You may comment the `sleep` line out to speed up testing, but make sure it is
 > back in place when you submit the assignment.

The program will work as follows:

 - create a `counter` set initially to 10
 - loop until the counter reaches 0
   + print the number
   + generate a random number called `chance` from 1 to 100
     - if `chance` is over 10, `sleep()` for 1 second, and subtract 1 from the counter and  keep on
       counting down
     - if `chance` is 8, 9, or 10, print "VALVE LEAK...COUNTDOWN ABORTED" and
       exit the program
     - if `chance` is 5, 6, or 7, print "RANGE VIOLATION...COUNTDOWN ABORTED"
       and exit the program
     - if `chance` is 2, 3, or 4, print "HOLD...HOLD...HOLD" and exit the
       program
     - if `chance` is 1, print "HOUSTON, WE HAVE A PROBLEM" and exit the
       program
  - Print "BLASTOFF!"

If all goes well, the output will be:
```
10
9
8
7
6
5
4
3
2
1
BLASTOFF!
```
Though tragedy can strike randomly at any moment:
```
10
9
8
HOUSTON, WE HAVE A PROBLEM
```
