from mainFP import *

p = Program()
while p.running:
    p.intro()
    if p.play:
        p.run()
    p.win_or_lose()
pygame.quit ()
