import textwrap

text = """Lorem ipsum dolor sit amet consectetur adipiscing elit suscipit, 
        augue consequat nulla lacus ultrices posuere quisque, rutrum sollicitudin 
        habitant nibh ac tortor platea. Facilisi sodales habitasse suspendisse id 
        libero ridiculus imperdiet elementum accumsan vitae dictumst, pulvinar 
        hendrerit taciti leo quam natoque tortor justo nisl euismod aenean cursus, 
        semper urna odio nunc condimentum cras posuere sapien feugiat massa. 
        Tellus malesuada nisi ridiculus hac phasellus erat aptent, risus scelerisque 
        volutpat faucibus pulvinar montes egestas diam, imperdiet nascetur posuere 
        luctus eleifend consequat."""

wrapper = textwrap.TextWrapper(width=100)
wordList = wrapper.wrap(text=text)

for i in wordList:
    print(i)