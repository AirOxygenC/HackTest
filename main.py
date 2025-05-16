import pygame
import asyncio

async def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Paint")

    background = pygame.Surface(screen.get_size())
    background.fill((255, 255, 255))

    clock = pygame.time.Clock()
    keepGoing = True
    lineStart = (0, 0)
    drawColor = (0, 0, 0)
    lineWidth = 3

    def status_surface(color, width):
        myFont = pygame.font.Font(None, 20)  # ✅ Web-safe font
        return myFont.render(f"color: {color}, width: {width}", True, color)

    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                lineStart = pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pressed()[0]:
                    lineEnd = pygame.mouse.get_pos()
                    pygame.draw.line(background, drawColor, lineStart, lineEnd, lineWidth)
                    lineStart = lineEnd
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    keepGoing = False
                elif event.key == pygame.K_c:
                    background.fill((255, 255, 255))
                elif event.key == pygame.K_w:
                    drawColor = (255, 255, 255)
                elif event.key == pygame.K_k:
                    drawColor = (0, 0, 0)
                elif event.key == pygame.K_r:
                    drawColor = (255, 0, 0)
                elif event.key == pygame.K_g:
                    drawColor = (0, 255, 0)
                elif event.key == pygame.K_b:
                    drawColor = (0, 0, 255)
                elif pygame.K_1 <= event.key <= pygame.K_9:
                    lineWidth = event.key - pygame.K_0

        screen.blit(background, (0, 0))
        screen.blit(status_surface(drawColor, lineWidth), (10, 10))
        pygame.display.flip()
        await asyncio.sleep(0)

asyncio.run(main())
