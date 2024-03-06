#Import libraries
import pygame
import pygame.locals

#Set up game, screen, grid
pygame.init()

line_width = 6
screen_width = 300
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("TicTacToe")

def draw_grid():
  background = (255, 255, 255)
  grid = (50, 50, 50)
  screen.fill(background)
  for i in range(1, 3):
    pygame.draw.line(screen, grid, (0, i*100), (screen_width, i*100), line_width)
    pygame.draw.line(screen, grid, (i*100, 0), (i*100, screen_width), line_width)

markers = []
for i in range(3):
  row = [0]*3
  markers.append(row)

#Colours
blue = (0, 0, 255)
red = (255, 0, 0)
def draw_markers():
  x_pos = 0
  for x in markers:
    y_pos = 0
    for y in x:
      if y == 1: #Draw X for player 1
        pygame.draw.line(screen, red, (x_pos*100 + 15, y_pos*100 + 15), (x_pos*100 + 85, y_pos*100 + 85), line_width)
        pygame.draw.line(screen, red, (x_pos*100 + 85, y_pos*100 + 15), (x_pos*100 + 15, y_pos*100 + 85), line_width)
      if y == -1: #Draw O for player -1
        pygame.draw.circle(screen, blue, (x_pos*100 + 50, y_pos*100 + 50), 35, line_width)
      y_pos += 1
    x_pos += 1

#Check win, draw
# Checking win
winner = None
def CheckHorizontal(Board):
  global winner
  if Board[0][0] == Board[0][1] == Board[0][2] and Board[0][0] != 0:
    winner = Board[0][0]
    return True
  elif Board[1][0] == Board[1][1] == Board[1][2] and Board[1][0] != 0:
    winner = Board[1][0]
    return True
  elif Board[2][0] == Board[2][1] == Board[2][2] and Board[2][0] != 0:
    winner = Board[2][0]
    return True

def CheckVertical(Board):
  global winner
  if Board[0][0] == Board[1][0] == Board[2][0] and Board[0][0] != 0:
    winner = Board[0][0]
    return True
  elif Board[0][1] == Board[1][1] == Board[2][1] and Board[0][1] != 0:
    winner = Board[0][1]
    return True
  elif Board[0][2] == Board[1][2] == Board[2][2] and Board[0][2] != 0:
    winner = Board[0][2]
    return True

def CheckDiag(Board):
  global winner
  if Board[0][0] == Board[1][1] == Board[2][2] and Board[0][0] != 0:
    winner = Board[0][0]
    return True
  elif Board[2][0] == Board[1][1] == Board[0][2] and Board[2][0] != 0:
    winner = Board[2][0]
    return True

# Checking win or draw
GameRunning = True
def CheckWin(Board):
  global GameRunning
  if CheckHorizontal(Board) or CheckVertical(Board) or CheckDiag(Board):
    GameRunning = False
    DrawWinner(winner)

def CheckDraw(Board):
  global GameRunning
  if 0 not in [cell for row in Board for cell in row]:
    GameRunning = False
    DrawDraw()

font = pygame.font.SysFont("Arial", 40)
def DrawWinner(winner):
  draw_markers()  
  win_text = "Player " + str(winner) + " wins!"
  win_img = font.render(win_text, True, blue)
  text_rect = win_img.get_rect(center=(screen_width // 2, screen_height // 2))
  pygame.draw.rect(screen, red, text_rect, 0)
  screen.blit(win_img, text_rect.topleft)
  global run
  run = False
def DrawDraw():
  draw_markers()  
  draw_text = "It's a draw"
  draw_img = font.render(draw_text, True, blue)
  text_rect = draw_img.get_rect(center=(screen_width // 2, screen_height // 2))
  pygame.draw.rect(screen, red, text_rect, 0)
  screen.blit(draw_img, text_rect.topleft)
  global run
  run = False
  
#Game running switch
run = True
click = False
pos = []
player = 1
while run:
  draw_grid()
  draw_markers()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
    if GameRunning:
      #Take user's input: mouse down
      if event.type == pygame.MOUSEBUTTONDOWN and not click:
        click = True
      #Check if user has lifted mouse button up
      if event.type == pygame.MOUSEBUTTONUP and click:
        click = False
        #Get mouse's position
        pos = pygame.mouse.get_pos()
        pos_x = pos[0] // 100
        pos_y = pos[1] // 100

        #Check if the square is still unmarked
        if markers[pos_x][pos_y] == 0:
          markers[pos_x][pos_y] = player
          player *= -1 #Players: 1 and -1
          CheckWin(markers)
          CheckDraw(markers)
    pygame.display.update()
pygame.time.delay(5000)
pygame.quit()