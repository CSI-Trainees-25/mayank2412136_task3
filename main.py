import pygame
from sys import exit
from random import randint

pygame.init()
playing = True
enemy_speed=5
def draw_floor():
    screen.blit(land1, (land1_x, land_y))
    screen.blit(land2, (land2_x, land_y))

def screen_run():
    global land1_x, land2_x, smallmountains1_x, smallmountains2_x,enemy_speed
    global montaintrees1_x, montaintrees2_x, foreground_trees1_x, foreground_trees2_x ,enemy_rect
    
    enemy_rect.x -= enemy_speed
    
    
    land1_x -= land_speed
    land2_x -= land_speed
    

    smallmountains1_x -= smallmountains_speed
    smallmountains2_x -= smallmountains_speed
    montaintrees1_x -= montaintrees_speed
    montaintrees2_x -= montaintrees_speed
    foreground_trees1_x -= foreground_trees_speed
    foreground_trees2_x -= foreground_trees_speed
    

    if land1_x <= -screen_width:
        land1_x = land2_x + screen_width
    if land2_x <= -screen_width:
        land2_x = land1_x + screen_width
    

    if smallmountains1_x <= -screen_width:
        smallmountains1_x = smallmountains2_x + screen_width
    if smallmountains2_x <= -screen_width:
        smallmountains2_x = smallmountains1_x + screen_width
        
    if montaintrees1_x <= -screen_width:
        montaintrees1_x = montaintrees2_x + screen_width
    if montaintrees2_x <= -screen_width:
        montaintrees2_x = montaintrees1_x + screen_width
        
    if foreground_trees1_x <= -screen_width:
        foreground_trees1_x = foreground_trees2_x + screen_width
    if foreground_trees2_x <= -screen_width:
        foreground_trees2_x = foreground_trees1_x + screen_width
    


def player_run():
    global run_frame_index, frame_speed
    
    if frame_speed % 5 == 0 and pygame.key.get_pressed()[pygame.K_RIGHT]:
        run_frame_index += 1
        if run_frame_index >= len(player_run_frames):
            run_frame_index = 0
def jump():
    global player_rect, jump_status
    
    if player_rect.bottom >= land_y -300 and jump_status:
        player_rect.y -= 5
        if player_rect.bottom == land_y -300:
            jump_status = False
    else:
        player_rect.y += 5
        if player_rect.bottom == land_y + 50:
            jump_status = True
    if player_rect.bottom > land_y + 50:
        player_rect.bottom = land_y + 50



jump_status = True 
def getdown():
    global player_rect, jump_status
    if player_rect.bottom < land_y + 55:
        player_rect.y += 5
            

def trajectry_attack():
    global enemy_rect, enemy_surface
    enemy_rect.x -= 18
    enemy_rect.y +=trajectry_attack_count
trajectry_attack_count=15
screen = pygame.display.set_mode((1400, 800))
pygame.display.set_caption("My Game")
screen_width, screen_height = screen.get_size()
clock = pygame.time.Clock()
background_screen_sky = pygame.image.load('BACKGROUND\sky.png').convert()
background_screen_smallmountains = pygame.image.load('BACKGROUND\parallax-mountain-mountains.png').convert_alpha()
background_screen_montaintrees = pygame.image.load('BACKGROUND\parallax-mountain-trees.png').convert_alpha()
background_screen_foreground_trees = pygame.image.load('BACKGROUND\parallax-mountain-foreground-trees.png').convert_alpha()
background_screen_farmountain = pygame.image.load('BACKGROUND\parallax-mountain-montain-far.png').convert_alpha()
land = pygame.image.load('BACKGROUND\land.png').convert_alpha()

background_screen_sky = pygame.transform.scale(background_screen_sky, (screen_width, screen_height))
background_screen_smallmountains = pygame.transform.scale(background_screen_smallmountains, (screen_width, screen_height))
background_screen_montaintrees = pygame.transform.scale(background_screen_montaintrees, (screen_width, screen_height))
background_screen_foreground_trees = pygame.transform.scale(background_screen_foreground_trees, (screen_width, screen_height))
background_screen_farmountain = pygame.transform.scale(background_screen_farmountain, (screen_width, screen_height))


smallmountains1 = background_screen_smallmountains.copy()
smallmountains2 = background_screen_smallmountains.copy()
montaintrees1 = background_screen_montaintrees.copy()
montaintrees2 = background_screen_montaintrees.copy()
foreground_trees1 = background_screen_foreground_trees.copy()
foreground_trees2 = background_screen_foreground_trees.copy()


land1 = pygame.transform.scale(land, (screen_width, 100))
land2 = pygame.transform.scale(land, (screen_width, 100))


land_speed = 5
smallmountains_speed = 3 
montaintrees_speed = 4  
foreground_trees_speed = 5  

land_y = screen_height - 100
land1_x = 0
land2_x = screen_width

smallmountains1_x = 0
smallmountains2_x = screen_width
montaintrees1_x = 0
montaintrees2_x = screen_width
foreground_trees1_x = 0
foreground_trees2_x = screen_width

#player run

player_run_surface_1 = pygame.transform.scale( pygame.image.load('PLAYER\Run (1).png').convert_alpha(), (100, 100))
player_run_surface_2 = pygame.transform.scale( pygame.image.load('PLAYER\Run (2).png').convert_alpha(), (100, 100))
player_run_surface_3 = pygame.transform.scale( pygame.image.load('PLAYER\Run (3).png').convert_alpha(), (100, 100))
player_run_surface_4 = pygame.transform.scale( pygame.image.load('PLAYER\Run (4).png').convert_alpha(), (100, 100))
player_run_surface_5 = pygame.transform.scale( pygame.image.load('PLAYER\Run (5).png').convert_alpha(), (100, 100))
player_run_surface_6 = pygame.transform.scale( pygame.image.load('PLAYER\Run (6).png').convert_alpha(), (100, 100))
player_run_surface_7 = pygame.transform.scale( pygame.image.load('PLAYER\Run (7).png').convert_alpha(), (100, 100))
player_run_surface_8 = pygame.transform.scale( pygame.image.load('PLAYER\Run (8).png').convert_alpha(), (100, 100))
player_run_surface_9 = pygame.transform.scale( pygame.image.load('PLAYER\Run (9).png').convert_alpha(), (100, 100))
player_run_surface_10 = pygame.transform.scale( pygame.image.load('PLAYER\Run (10).png').convert_alpha(), (100, 100))

player_run_frames = [
    player_run_surface_1, player_run_surface_2, player_run_surface_3, 
    player_run_surface_4, player_run_surface_5, player_run_surface_6,
    player_run_surface_7, player_run_surface_8, player_run_surface_9, 
    player_run_surface_10
]

player_rect = player_run_surface_1.get_rect(midbottom = (80, land_y+50))
run_frame_index = 0

player_jump_surface = pygame.transform.scale( pygame.image.load('PLAYER\Jump (7).png').convert_alpha(), (100, 100))


# enimies
enemy_surface1 = pygame.transform.scale( pygame.image.load('enemies\Enemies\enemyFloating_1.png').convert_alpha(), (80, 80))
enemy_surface2 = pygame.transform.scale( pygame.image.load('enemies\Enemies\enemyWalking_1.png').convert_alpha(), (80, 80))
enemy_surface3 = pygame.transform.scale( pygame.image.load('enemies\Enemies\enemySpikey_1.png').convert_alpha(), (80, 80))
enemy_surface4 = pygame.transform.scale( pygame.image.load('enemies\Enemies\enemySwimming_1.png').convert_alpha(), (80, 80))
enemy_surface5 = pygame.transform.scale( pygame.image.load('enemies\Enemies\enemyFlying_1.png').convert_alpha(), (80, 80))
enemy_surfaces=[enemy_surface1, enemy_surface2, enemy_surface5, enemy_surface3, enemy_surface4]
enemy_surface = enemy_surfaces[randint(0,4)]
enemy_rect = enemy_surface.get_rect(midbottom = (randint(1400, 1800), land_y + 50))
frame_speed = 0
run_frame_index = 0
# ememy attack

# enemy_surface_a/ttack = pygame.transform.scale( pygame.image.load('enemies\Items\redJewel.png').convert_alpha(), (80, 80))
# enemy_surface_attack_rect = enemy_surface_attack.get_rect(midbottom = (randint(1400

enemy_attack = False


# text
score_font = pygame.font.Font(None, 50)
score = 0
score_surface = score_font.render('Score: ' + str(score), True, (255, 255, 255))
score_rect = score_surface.get_rect(topleft = (10, 10))
game_name_font = pygame.font.Font(None, 100)
game_name_surface = game_name_font.render('forest runner', True, (255, 255,255))
game_name_rect = game_name_surface.get_rect(center = (screen_width//2, 100))
restart_game_font = pygame.font.Font(None, 50)
restart_game_surface = restart_game_font.render('Press SPACE to restart', True, (255, 255, 255))
restart_game_rect = restart_game_surface.get_rect(center = (screen_width//2, 700))
welcome_font = pygame.font.Font(None, 50)
welcome_surface = welcome_font.render('Press SPACE to start', True, (255,0,0))
welcome_rect = welcome_surface.get_rect(center = (screen_width//2, screen_height//2 + 100))

# HEART
heart_surface = pygame.transform.scale(pygame.image.load('EQUIPABLES\heart.png').convert_alpha(), (80, 80))
heart_rect = heart_surface.get_rect(topleft = (screen_width - 80, 10))
heart_count = 3

welcome_screen = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    if welcome_screen:
        screen.fill((0,0,0))
        screen.blit(game_name_surface, game_name_rect)
        screen.blit(welcome_surface, welcome_rect)
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            welcome_screen = False
            playing = True
            score = 0
        pygame.display.update()
        clock.tick(60)
        continue
    
    frame_speed +=1
    if frame_speed == 10:
        run_frame_index += 1
        if run_frame_index >= len(player_run_frames):
            run_frame_index = 0
        frame_speed = 0
    
    
    screen.blit(background_screen_sky,(0,0))
    screen.blit(background_screen_farmountain,(0,-150))
    screen.blit(smallmountains1, (smallmountains1_x, 0))
    screen.blit(smallmountains2, (smallmountains2_x, 0))
    screen.blit(montaintrees1, (montaintrees1_x, 0))
    screen.blit(montaintrees2, (montaintrees2_x, 0))
    screen.blit(foreground_trees1, (foreground_trees1_x, 0))
    screen.blit(foreground_trees2, (foreground_trees2_x, 0))
    draw_floor()
    if heart_count > 0:
        screen.blit(heart_surface, heart_rect)
    if heart_count > 1:
        screen.blit(heart_surface, (screen_width - 160, 10))
    if heart_count > 2:
        screen.blit(heart_surface, (screen_width - 240, 10))
    
    if player_rect.bottom < land_y + 50:
        jump()
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        screen_run()
        player_run()
        if( pygame.key.get_pressed()[pygame.K_SPACE] or pygame.key.get_pressed()[pygame.K_UP] ) and (player_rect.bottom == land_y + 50):
            jump()
            screen.blit(player_jump_surface, (player_rect.x, player_rect.y))
        else:
            screen.blit(player_run_frames[run_frame_index], player_rect)
            
    elif( pygame.key.get_pressed()[pygame.K_SPACE] or pygame.key.get_pressed()[pygame.K_UP] ) or (player_rect.bottom < land_y + 50):
        # screen_run()
        screen.blit(player_jump_surface, (player_rect.x, player_rect.y))
        
        
        jump()
    elif pygame.key.get_pressed()[pygame.K_RIGHT] and ( pygame.key.get_pressed()[pygame.K_SPACE] or pygame.key.get_pressed()[pygame.K_UP]  or (player_rect.bottom < land_y + 50)) :
        screen_run()
        screen.blit(player_jump_surface, (player_rect.x, player_rect.y))
        jump()
        player_run()
    else:
        screen.blit(player_run_frames[run_frame_index], player_rect)
        
    if not enemy_surface == enemy_surface5 :
        screen.blit(enemy_surface, enemy_rect)
        
    else:
        if playing:
            screen.blit(enemy_surface, (enemy_rect.x-randint(200,300), enemy_rect.y - 890))
            trajectry_attack()
            if player_rect.colliderect(enemy_rect.x-randint(200,300), enemy_rect.y - 890,80,80):
               
                enemy_rect = enemy_surface.get_rect(midbottom = (-1, land_y + 50))
                heart_count -= 1
                if heart_count == 0:
                    playing = False
                
    if enemy_rect.right <= 0 and playing:
        score += 1
        if score % 5 == 0:
            enemy_speed += 1
            land_speed += 1
            smallmountains_speed += 1
            montaintrees_speed += 1
            foreground_trees_speed += 1
            trajectry_attack_count+=1
        enemy_surface = enemy_surfaces[randint(0,4)]
        enemy_rect = enemy_surface.get_rect(midbottom=(randint(1400, 1800),land_y + 50))
        
    score_surface = score_font.render('Score: ' + str(score), True, (255, 255, 255))
    screen.blit(score_surface, score_rect)
    if player_rect.colliderect(enemy_rect):
        enemy_rect = enemy_surface.get_rect(midbottom = (-1, land_y + 50))
        heart_count -= 1
        if heart_count == 0:
            playing = False
        
       
    

        
    game_over_score_surface = score_font.render('Game Over! Your Score: ' + str(score), True, (255, 0, 0))
    game_over_score_rect = game_over_score_surface.get_rect(center = (screen_width//2, screen_height//2))
    draw_floor()
    if playing == False:
        screen.fill((0,0,0))
        screen.blit(game_name_surface, game_name_rect)
        screen.blit(game_over_score_surface, game_over_score_rect)
        screen.blit(restart_game_surface, restart_game_rect)
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            playing = True
            score = 0
            heart_count = 3
            jump_status = True
            frame_speed = 0
            enemy_speed =5
            land_speed =5
            smallmountains_speed =3
            montaintrees_speed =4
            foreground_trees_speed =5
            trajectry_attack_count=15
            enemy_surface = enemy_surfaces[randint(0,4)]
            enemy_rect = enemy_surface.get_rect(midbottom = (randint(1400, 1800), land_y + 50))
            player_rect.midbottom = (80, land_y+50)
    
    player_run()
    screen_run()
    pygame.display.update()
    clock.tick(60)


