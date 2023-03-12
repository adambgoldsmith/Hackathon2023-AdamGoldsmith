# Hackathon2023-AdamGoldsmith

## This is my unofficial entry for the "Hack the break 2023" hackathon. I unfortunately missed the sign up, but I wanted to participate nonetheless.

## Python Vs Java
Tech used: Pygame, Aseprite, jsfxr, Beepbox(Jummbox)

I made this small street fighter/mortal kombat style game in around 36 hours.

All assets including art, sounds, and music were made by me (Adam).

Excuse the (much) less than perfect .py file.

### What did I learn:
I am used to engines like unity, godot, and unreal, so trying out pygame for the first time was interesting.

Not being able to see and manipulate objects in a scene makes it much more challenging to get things to work properly.
Pygame uses simple x and y coordinate system to map rectangular objects to the screen, so it took a lot of trial and error
to get sprites into the exact positions that I needed them to be in.

I started off watching a tutorial that didn't use classes to create objects. Even though that one tutorial was all I needed to
understand pretty much everything about pygame, not using classes was a BIG BIG BIG mistake. I ended up making way too many unnecessary
functions that could have been turned into simple class methods.

An extended problem of not using classes came up when I wanted to change the sprites of the characters. Because python is pass-by-value,
I couldn't change the sprites through a function call and instead had to use mutable lists to globally change the sprites. This was
also the case with checking if the player was blocking or not.

### What would I change:

Classes: 90% of my issues would be solved if I had known classes were best practice.

Organization: My main module is a mess and could use a spring cleaning. I don't think it's too awful for 36 hours minus sleeping time though.

Nested ifs: Too many. gross. 

Sprites/art: I really like all of the python character's sprites; The java character's sprites, not so much. If I had
more time I would have refined the java sprites and made more interesting art for him.

---

![image](https://user-images.githubusercontent.com/52685070/224569633-48d5b85a-29e5-4516-b73f-6d2b42b01ca2.png)

![image](https://user-images.githubusercontent.com/52685070/224569780-29fd8ed8-7fc4-45cb-a36f-477bc0fc8086.png)

![image](https://user-images.githubusercontent.com/52685070/224569809-87eb7919-9c59-4bb6-a731-6c9ef652eda7.png)

