from random import *
from pygame import *

score = 0
missing = 0
font.init()
font2 = font.Font(None,36)




class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (60,60))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y          
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):       
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y <= 500:
            self.rect.y += self.speed

        if keys_pressed[K_a] and self.rect.x >= 0:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x <= 640:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.centery, 5)
        bullets.add(bullet)

 


class Enemy(GameSprite):
    def update(self):
        global missing
        self.rect.y += self.speed
        if self.rect.y >= 500:
            missing += 1
            self.rect.y = 0
            self.rect.x = randint(1,500)
#создай окно игры
window = display.set_mode((700, 500))
display.set_caption('Шутер')
background = transform.scale(image.load('galaxy.jpg'), (700, 500))



class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.kill()


clock = time.Clock()
FPS = 100
rocket = Player('rocket.png', 50, 50, 6)
monsters = sprite.Group()
for i in range(5):
    monster = Enemy('ufo.png', randint(0, 500), randint(-200, -50), randint(1,2))
    monsters.add(monster)
bullets = sprite.Group()
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()

finish = False
game = True
while game: 

    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == MOUSEBUTTONDOWN:
            if e.button == 1:
        
                rocket.fire()
    if finish != True:
        window.blit(background,(0,0))
        rocket.reset()
        rocket.update()
        monsters.update()
        monsters.draw(window)
        bullets.update()
        bullets.draw(window)
        collides = sprite.groupcollide(monsters, bullets, True, True)
        for c in collides:
            score += 1
            monster = Enemy('ufo.png', randint(0, 500), randint(-200, -50), randint(1,2))
            monsters.add(monster)
        

        text1 = font2.render('Счёт:' + str(score), 1, (255,255,255))

        text2 = font2.render('Пропущено:' + str(missing), 1, (255,255,255))
        window.blit(text1, (10, 20))
        window.blit(text2, (10, 50))


        

    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)



# from pygame import *

# class GameSprite(sprite.Sprite):
#     def __init__(self, player_image, player_x, player_y, player_speed):
#         super().__init__()
#         self.image = transform.scale(image.load(player_image), (90,90))
#         self.speed = player_speed
#         self.rect = self.image.get_rect()
#         self.rect.x = player_x
#         self.rect.y = player_y          
#     def reset(self):
#         window.blit(self.image, (self.rect.x, self.rect.y))


# class Player(GameSprite):       
#     def update(self):
#         keys_pressed = key.get_pressed()
#         if keys_pressed[K_w] and self.rect.y >= 0:
#             self.rect.y -= self.speed
#         if keys_pressed[K_s] and self.rect.y <= 500:
#             self.rect.y += self.speed

#         if keys_pressed[K_a] and self.rect.x >= 0:
#             self.rect.x -= self.speed
#         if keys_pressed[K_d] and self.rect.x <= 640:
#             self.rect.x += self.speed

# class Wall(sprite.Sprite):
#     def __init__(self, r, g, b, x, y, w, h):
#         super().__init__()
#         self.red = r
#         self.green = g 
#         self.blue = b 
#         self.width = w
#         self.height = h
#         self.image = Surface((self.width, self.height))
#         self.image.fill((self.red, self.green, self.blue))
#         self.rect = self.image.get_rect()
#         self.rect = self.image.get_rect()
#         self.rect.x = x
#         self.rect.y = y
#     def draw_wall(self):
#         window.blit(self.image, (self.rect.x, self.rect.y))


        



    
        
# #создай окно игры
# window = display.set_mode((700, 500))
# display.set_caption('Догонялки')
# background = transform.scale(image.load('background.jpg'), (700, 500))

# clock = time.Clock()
# FPS = 60
# hero = Player('hero.png', 50, 50, 5)
# cyborg = Enemy('cyborg.png', 550, 300, 5)
# gold = GameSprite('treasure.png', 550, 380, 0)


# w1 = Wall(0, 0, 0, 100, 200, 5, 5)
# w2 = Wall(0, 0, 0, 170, 50, 205, 5)
# w3 = Wall(0, 0, 0, 170, 170, 0, 5)
# w4 = Wall(0, 0, 0, 300, 200, 30, 5)
# w5 = Wall(0, 0, 0, 240, 228, 69, 5)
# w6 = Wall(0, 0, 0, 130, 100, 105, 5 )
# w7 = Wall(0, 0, 0, 400, 400, 5, 230)



# mixer.init()
# mixer.music.load('jungles.ogg')
# mixer.music.play()
# font.init()
# font = font.Font(None, 70)
# lose = font.render('ХА-ХА-ХА ТЫ ПРОИГРАЛ', True, (255, 215, 0))
# win = font.render('Ты выиграл', True, (255, 215, 0))

# finish = False
# game = True
# while game: 
#     if finish != True:
#         window.blit(background,(0,0))
#         hero.reset()
#         cyborg.reset()
#         gold.reset()
#         hero.update()
#         cyborg.update()
#         w1.draw_wall()
#         w2.draw_wall()
#         w3.draw_wall()
#         w4.draw_wall()
#         w5.draw_wall()
#         w6.draw_wall()
#         w7.draw_wall()
#         if sprite.collide_rect(hero, cyborg):
#             finish = True
#             window.blit(lose, (100, 100))
#         if sprite.collide_rect(hero, gold):
#             finish = True
#             window.blit(win, (100, 100))






#     for e in event.get():
#         if e.type == QUIT:
#             game = False
