from playerFP import *
from settingsFP import *

class Program():
    def __init__(self):
        pygame.mixer.init() #to add music
        pygame.mixer.music.load("monody.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        self.screen = pygame.display.set_mode((screen_width, screen_height)) #Resolution
        self.clock = pygame.time.Clock()
        self.running = True
        self.play = True
        self.all_sprites = pygame.sprite.Group()
        self.blocks = pygame.sprite.Group()
        self.i = 0 #index
        self.stopped = False
        self.current_block = []
        self.previous_block = []
        self.stacked = 4
        self.penalty = 0
        #self.introbg = pygame.display.load("intro.png")

    def text_objects(self, text, ang):
        font = pygame.font.Font('leadcoat.ttf',ang)
        textsurface = font.render(text, True, (0,0,0))
        return textsurface, textsurface.get_rext()

    def intro(self):
        intro = True
        while intro:
            for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.screen.fill((0,0,0))
            textsurf ,textrect = self.text_objects("Play",55)
            textrect.center = ((screen_width/2),(screen_height/2))
            self.screen.blit(textrect,textsurf)
            pygame.display.update()
            clock.tick(15)

    def run(self):
        self.new()
        while self.play:
            self.clock.tick(FPS)
            self.event()
            self.update()
            self.draw()

    def new(self):
        for block in blocklist[0]:
            b = Player(*block)
            self.current_block.append(b)
            self.all_sprites.add(b)
            self.blocks.add(b)

    def update(self):
        self.all_sprites.update()
        for block in self.blocks:
            if block.rect.x == 0 and not block.stop:
                for block in self.blocks:
                    block.edge = False
            if block.rect.x == 231 and not block.stop:
                for block in self.blocks:
                    block.edge = True

        if self.stopped: # kalo kita pencet space semua blok yg ada di screen stop dan semua yg dibawah ini terjadi

            # cek blok yg baru dibawahnya ada blok yg sebelumnya kaga, kalo ga ya jatoh
            if len(self.previous_block) != 0:
                for block_now in self.current_block:
                    for block in self.previous_block:
                        if block.rect.x == block_now.rect.x:  # cara cek nya itu dia bandingin posisi x blok2 yg ada dibawah (self.previous_block) itu sama atau tidak dgn blok2 yg ada di atas (self.current_block).
                            self.all_sprites.add(block_now)
                            self.blocks.add(block_now)
                            self.stacked += 1  # kalo posisi x nya ada yg sama (ga jatoh), kita tambah 1 self.stacked nya
                            break
                        else: # kalo posisi x nya ga sama (jatoh), di delete blok nya
                            self.all_sprites.remove(block_now)
                            self.blocks.remove(block_now)
            # kurangin blok nya kalo ada yg jatoh, caranya jumlah blok yg baru dikurang dengan jumlah blok yg ga jatoh (self.stacked)
            if len(blocklist[self.i]) >= self.stacked:
                self.penalty = len(blocklist[self.i]) - self.stacked

            # kalo udh di cek kita kosongin self.previous_block (utk penegecekan blok bawah) untuk yg berikutnya
            self.previous_block.clear()

            # terus kita isi self.previous_block nya dgn self.current_block
            for block in self.current_block:
                if block in self.blocks:
                    self.previous_block.append(block)

            # kalo udh di isi self.previous_block nya dgn self.current_block, kita kosongin self.current_block nya (utk pengecekan blok atas) untuk yg berikutnya
            self.current_block.clear()

            # setelah cek itu baru dibuat diatasnya blok yg baru
            for index in range(len(blocklist[self.i]) - self.penalty):
                b = Player(*blocklist[self.i][index])
                b.currentspeed = blockspeed[self.i] # naikin kecepatannya untuk blok yg baru
                self.current_block.append(b) # nah blok yg baru ini kita masukin ke self.current_block untuk dibandingin/dicek bawahnya(self.previous_block) itu ada blok lagi atau tidak
                self.all_sprites.add(b)
                self.blocks.add(b)
            self.stopped = False
            self.stacked = 0
            self.penalty = 0

    def event(self):
        for event in pygame.event.get(): #harus ada
            if event.type == pygame.QUIT:
                if self.play:
                    self.play = False
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.i += 1
                    self.stopped = True
                    for i in self.blocks:
                        i.stop = True

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.all_sprites.draw(self.screen)
        pygame.display.flip()
