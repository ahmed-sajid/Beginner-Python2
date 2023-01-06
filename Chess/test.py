import pygame

# Initialize Pygame
pygame.init()

# Set the screen size
screen = pygame.display.set_mode((400, 400))

# Create a white circle at the center of the screen
# with a radius of 50 pixels
radius = 50
x = 200
y = 200
color = (255, 255, 255)  # White
pygame.draw.circle(screen, color, (x, y), radius)

# Update the screen
pygame.display.flip()

# Wait for the user to close the window
done = False
while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
oxｐェｘ