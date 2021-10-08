import pygame

def main():
    pygame.init()

    pygame.display.set_caption("Lab2")
    WIDTH = 800
    HEIGHT = 480

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.update()

    #WALLS
    wcolor = pygame.Color("blue")
    THICKNESS = 20
    #top wall  Surface, color, rectangular objext
    #Rect((left, top), (width, height)) -> Rect
    pygame.draw.rect(screen, wcolor, pygame.Rect((0,0), (WIDTH, THICKNESS)) )
    pygame.draw.rect(screen, wcolor, pygame.Rect((0,0), (THICKNESS, HEIGHT)) )
    pygame.draw.rect(screen, wcolor, pygame.Rect((0, HEIGHT - THICKNESS), (WIDTH, THICKNESS)) )
    pygame.display.update()

    # define a variable to control the main loop
    running = True
        
    # main loop
    while running:
        # event handling, gets all event from the event queue 
        for event in pygame.event.get(): #Polling: We are constantly checking into that queue, if somebody hit quit, we set running to false and we exit the for loop
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

                #1 player three walls and a padde and ball bouncing
                #Ai player
                #Today: walls
                #Later: paddle, ball, OOP
                #After: AI
                #Wall thickness is border, 0,0 is coords of top left corner, goes to width
                #Physics will go up and down
if __name__=="__main__":
    # call the main function
    main()