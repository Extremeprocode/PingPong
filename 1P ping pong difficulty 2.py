import pygame, sys, random

player_points = 0
AI_points = 0



def ball_animate():
    global ball_speed_x, ball_speed_y, player_points, AI_points
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0:
        ball_restart()
        player_points += 1
        points()
    if ball.right >= screen_width:
        ball_restart()
        AI_points += 1
        points()

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def player_animate():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opponent_ai():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width/2, screen_height/2)
    ball_speed_y *= random.choice((1,-1))
    ball_speed_x *= random.choice((1,-1))

def points():
    fontType = pygame.font.Font(None, 30)
    printpoint = fontType.render(f'AI: {AI_points} | Player: {player_points}', False, (255,187,255))
    printpointRect = printpoint.get_rect(center = (screen_width/2, 50))
    screen.blit(printpoint, printpointRect)
    if AI_points == 10 and player_points < 10:
        AI_win = fontType.render('AI has won, you have lost', False, (255,187,255))
        AI_winRect = AI_win.get_rect(center = (screen_width/2, screen_height/2))
        screen.blit(AI_win, AI_winRect)
        pygame.time.delay(1000)
        pygame.quit()
        sys.exit()
    if player_points == 10 and AI_points < 10:
        playerWin = fontType.render('You have won, AI has lost',  False, (255,187,255))
        playerWinRect = AI_win.get_rect(center = (screen_width/2, screen_height/2))
        screen.blit(playerWin, playerWinRect)
        pygame.time.delay(1000)
        pygame.quit()
        sys.exit()

pygame.init()
# pygame.mixer.init()
# pygame.mixer.music.load()
# pygame.mixer.music.play()
clock = pygame.time.Clock()

screen_width = 1060
screen_height = 740
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('pingpong')

ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15,30,30)
player = pygame.Rect(screen_width - 20,screen_height/2 - 70, 10,140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)

bg_color = pygame.Color('grey12')
light_grey = (200,200,200)

ball_speed_x = 10 * random.choice((1,-1))
ball_speed_y = 10 * random.choice((1,-1))
player_speed = 0
opponent_speed = 12

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

    ball_animate()
    player_animate()
    opponent_ai()
    
    font = pygame.font.Font(None, 32)
    text = font.render(f'AI: {AI_points} | player_points: {player_points}', True, (0, 255, 0), (0,0,128))
    textRect = text.get_rect(center = (530,50))
    screen.blit(text,textRect)

    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2,0), (screen_width/2,screen_height))
    

    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)
