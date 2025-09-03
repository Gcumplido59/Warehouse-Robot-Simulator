import pygame

# Colors
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
BLUE = (0, 100, 255)
GREEN = (50, 205, 50)
RED = (220, 20, 60)
BROWN = (139, 69, 19)
YELLOW = (255, 215, 0)

class Visualizer:
    def __init__(self, almacen):
        self.almacen = almacen
        self.path = None # The path starts as None
        self.cell_size = 60
        
        # Make window taller for the reset button
        self.width = self.almacen.ancho * self.cell_size
        self.height = self.almacen.alto * self.cell_size + 80 # Extra 80 pixels for button
        
        # Button setup
        self.button_rect = pygame.Rect(20, self.height - 70, 150, 50)
        self.button_color = (100, 100, 100)

        pygame.init()
        self.font = pygame.font.SysFont("Arial", 24)

        self.font_small = pygame.font.SysFont("Arial", 18)
        self.instructions = [
            "- Left Click: Place Obstacles",
            "- Right Click: Place Package",
            "- SPACE Key: Find Path"
        ]
        self.text_surfaces = []
        # Calculate position for the first line of text
        start_x = self.button_rect.right + 20
        start_y = self.button_rect.top + 5
        
        # Create a surface for each line of text
        for i, line in enumerate(self.instructions):
            surface = self.font_small.render(line, True, BLACK)
            rect = surface.get_rect(topleft=(start_x, start_y + i * 22)) # 22 pixels for line spacing
            self.text_surfaces.append((surface, rect))

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Warehouse Robot Simulator - Setup Mode")
        self.clock = pygame.time.Clock()

    def get_grid_pos(self, mouse_pos):
        # Converts pixel coordinates to grid coordinates
        mx, my = mouse_pos
        if my < self.almacen.alto * self.cell_size: # Make sure click is on the grid
                row = my // self.cell_size
                col = mx // self.cell_size
                return row, col
        return None, None # Click was outside the grid   

    # In visualizer.py, replace draw_button with this new draw_ui method

    def draw_ui(self):
        # Draw the reset button (same as before)
        pygame.draw.rect(self.screen, self.button_color, self.button_rect)
        text_surf = self.font.render("Reset", True, WHITE)
        text_rect = text_surf.get_rect(center=self.button_rect.center)
        self.screen.blit(text_surf, text_rect)

        # Draw the instruction text surfaces
        for surface, rect in self.text_surfaces:
            self.screen.blit(surface, rect)

    def draw_grid(self):
        grid_height = self.almacen.alto * self.cell_size
        
        # Draw vertical lines
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, BLACK, (x, 0), (x, grid_height))
            
        # Draw horizontal lines
        # This is the corrected loop that stops at the right height
        for y in range(0, grid_height + 1, self.cell_size):
            pygame.draw.line(self.screen, BLACK, (0, y), (self.width, y))

    def draw_objects(self):
        # Map symbols to colors
        color_map = {'R': RED, '📦': BROWN, '1': BLACK}

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
            # --- 1. Event Handling ---
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # Handle mouse clicks
                if event.type == pygame.MOUSEBUTTONDOWN:
                    row, col = self.get_grid_pos(event.pos)
                    
                    # Check if the reset button was clicked
                    if self.button_rect.collidepoint(event.pos):
                        self.almacen.reset()
                        self.path = None # Clear the path
                        print("Warehouse has been reset.")
                    
                    elif row is not None: # Ensure the click was on the grid
                        # Left Click to place obstacles
                        if event.button == 1:
                            if self.almacen.cuadricula[row][col] == '0':
                                self.almacen.cuadricula[row][col] = '1'
                                self.path = None # Placing objects invalidates old path

                        # Right Click to place the package
                        elif event.button == 3:
                            # If a package already exists, remove its old spot
                            if self.almacen.package:
                                old_r, old_c = self.almacen.package.fila, self.almacen.package.columna
                                self.almacen.cuadricula[old_r][old_c] = '0'

                            if self.almacen.cuadricula[row][col] == '0':
                                self.almacen.add_package(fila=row, col=col)
                                self.path = None # Placing objects invalidates old path
                
                # Handle key presses
                if event.type == pygame.KEYDOWN:
                    # Press SPACE to find the path
                    if event.key == pygame.K_SPACE:
                        if self.almacen.package:
                            print("Searching for a path...")
                            self.path = self.almacen.find_path()
                            if self.path:
                                print("Path Found!")
                            else:
                                print("No path could be found.")
                        else:
                            print("Cannot find path: Please place a package first.")

            # --- 2. Drawing ---
            self.screen.fill(WHITE)
            if self.path: self.draw_path()
            self.draw_objects()
            self.draw_grid()
            self.draw_ui() # Draw the reset button

            # --- 3. Update Display ---
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()