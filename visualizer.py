import pygame

# Constants
# Colors
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
BLUE = (0, 100, 255)
GREEN = (50, 205, 50)
RED = (220, 20, 60)
BROWN = (139, 69, 19)
YELLOW = (255, 215, 0)

class Visualizer:
    def __init__(self, almacen, path):
        self.almacen = almacen
        self.path = path
        self.cell_size = 60 # Size of each grid square in pixels
        self.width = self.almacen.ancho * self.cell_size
        self.height = self.almacen.alto * self.cell_size

        # Initialize Pygame
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Warehouse Robot Simulator")
        self.clock = pygame.time.Clock()

    def draw_grid(self):
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, BLACK, (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, BLACK, (0, y), (self.width, y))

    def draw_objects(self):
        # Map symbols to colors
        color_map = {'R': RED, '📦': BROWN, '🧱': BLACK}

        for fila in range(self.almacen.alto):
            for col in range(self.almacen.ancho):
                symbol = self.almacen.cuadricula[fila][col]
                if symbol in color_map:
                    color = color_map[symbol]
                    # The rect is (left, top, width, height)
                    rect = pygame.Rect(col * self.cell_size, fila * self.cell_size, self.cell_size, self.cell_size)
                    pygame.draw.rect(self.screen, color, rect)

    def draw_path(self):
        if not self.path:
            return
        
        # Draw small circles for each step in the path
        for i, pos in enumerate(self.path):
            fila, col = pos
            center_x = col * self.cell_size + self.cell_size // 2
            center_y = fila * self.cell_size + self.cell_size // 2
            
            # Make the path yellow, but the start (robot) and end (package) green
            color = YELLOW
            if i == 0 or i == len(self.path) - 1:
                color = GREEN
                
            pygame.draw.circle(self.screen, color, (center_x, center_y), self.cell_size // 6)

    def run(self):
        running = True
        while running:
            # 1. Event Handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # 2. Drawing
            self.screen.fill(WHITE) # White background
            self.draw_path()
            self.draw_objects()
            self.draw_grid()

            # 3. Update the display
            pygame.display.flip()
            self.clock.tick(60) # Limit to 60 frames per second

        pygame.quit()