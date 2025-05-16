"""
Name: Jessica Chen
Date: December 5, 2024
Description: A drawing program which you can draw with lines, and colours of white, black, red, blue, green, and
different line widths. There are also options to save images or load previously saves.
"""

# I - Import and Initialize
import pygame, asyncio

pygame.init()


def statusSurface(drawColor, lineWidth):
    """ creates a Surface object for status text """
    myFont = pygame.font.SysFont("Courier", 20)
    status_string = "color: %s, width: %d" % (drawColor, lineWidth)
    status = myFont.render(status_string, 1, (drawColor))
    return status


async def main():
    '''This function defines the 'mainline logic' for our paint program.'''
    # D - Display configuration
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Paint: (w)hite, blac(k), (c)lear, (q)uit")

    # E - Entities
    background = pygame.Surface(screen.get_size())
    background.fill((255, 255, 255))

    # A - Action (broken into ALTER steps)

    # A - Assign values to key variables
    clock = pygame.time.Clock()
    keepGoing = True
    lineStart = (0, 0)
    drawColor = (0, 0, 0)
    lineWidth = 3

    # L - Loop
    while keepGoing:

        # T - Timer to set frame rate
        clock.tick(30)

        # E - Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.MOUSEMOTION:
                lineEnd = pygame.mouse.get_pos()
                # Check if a left mouse button is down
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    pygame.draw.line(background, drawColor, lineStart, lineEnd, lineWidth)
                    lineStart = lineEnd
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    # quit
                    keepGoing = False
                elif event.key == pygame.K_c:
                    # clear screen
                    background.fill((255, 255, 255))
                elif event.key == pygame.K_w:
                    # white
                    drawColor = (255, 255, 255)
                elif event.key == pygame.K_k:
                    # black
                    drawColor = (0, 0, 0)

                elif event.key == pygame.K_r:
                    # red
                    drawColor = (255, 0, 0)

                elif event.key == pygame.K_g:
                    # green
                    drawColor = (0, 255, 0)

                elif event.key == pygame.K_b:
                    # blue
                    drawColor = (0, 0, 255)

                elif event.key == pygame.K_1:
                    lineWidth = 1

                elif event.key == pygame.K_2:
                    lineWidth = 2

                elif event.key == pygame.K_3:
                    lineWidth = 3

                elif event.key == pygame.K_4:
                    lineWidth = 4

                elif event.key == pygame.K_5:
                    lineWidth = 5

                elif event.key == pygame.K_6:
                    lineWidth = 6

                elif event.key == pygame.K_7:
                    lineWidth = 7

                elif event.key == pygame.K_8:
                    lineWidth = 8

                elif event.key == pygame.K_9:
                    lineWidth = 9

                elif event.key == pygame.K_s:
                    pygame.image.save(background, "painting.bmp")

                elif event.key == pygame.K_l:
                    drawing = pygame.image.load("painting.bmp")
                    drawings = drawing.convert()
                    background.blit(drawings, (0, 0))

        # R - Refresh display
        screen.blit(background, (0, 0))
        myLabel = statusSurface(drawColor, lineWidth)
        screen.blit(myLabel, (450, 450))
        pygame.display.flip()

    await asyncio.sleep(0)

    # Close the game window
    pygame.quit()


# Call the main function
asyncio.run(main())