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
    """Handles the graphical visualization of the warehouse using Pygame.

    This class is responsible for drawing the grid, objects (robot, package,
    obstacles), and the final path. It also handles all user input, such
    as mouse clicks for placing objects and key presses for running the
    pathfinding algorithm.

    Attributes:
        warehouse (Warehouse): The warehouse instance to visualize.
        path (list[tuple[int, int]]): The calculated path to draw.
        cell_size (int): The size of each grid cell in pixels.
        width (int): The total width of the Pygame window.
        height (int): The total height of the Pygame window.
        screen (pygame.Surface): The main display surface.
        clock (pygame.time.Clock): Pygame clock for controlling the frame rate.
    """
    def __init__(self, warehouse):
        """Initializes the Visualizer and sets up the Pygame window.

        Args:
            warehouse (Warehouse): The warehouse object to be visualized.
        """
        self.warehouse = warehouse
        self.path = None
        self.cell_size = 60
        
        # Make window taller for the UI elements
        self.width = self.warehouse.width * self.cell_size
        self.height = self.warehouse.height * self.cell_size + 80
        
        # UI Button setup
        self.button_rect = pygame.Rect(20, self.height - 70, 150, 50)
        self.button_color = (100, 100, 100)

        pygame.init()
        self.font = pygame.font.SysFont("Arial", 24)
        self.font_small = pygame.font.SysFont("Arial", 18)

        # Instructions text setup
        self.instructions = [
            "- Left Click: Place Obstacles",
            "- Right Click: Place Package",
            "- SPACE Key: Find Path"
        ]
        self.text_surfaces = []
        start_x = self.button_rect.right + 20
        start_y = self.button_rect.top + 5
        for i, line in enumerate(self.instructions):
            surface = self.font_small.render(line, True, BLACK)
            rect = surface.get_rect(topleft=(start_x, start_y + i * 22))
            self.text_surfaces.append((surface, rect))

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Warehouse Robot Simulator")
        self.clock = pygame.time.Clock()

    def get_grid_pos(self, mouse_pos):
        """Converts pixel screen coordinates to grid coordinates.

        Args:
            mouse_pos (tuple[int, int]): The (x, y) coordinates of the mouse click.

        Returns:
            tuple[int, int] or tuple[None, None]: The (row, col) of the grid cell
            that was clicked, or (None, None) if the click was outside the grid.
        """
        mx, my = mouse_pos
        if my < self.warehouse.height * self.cell_size:
            row = my // self.cell_size
            col = mx // self.cell_size
            return row, col
        return None, None

    def draw_ui(self):
        """Draws all user interface elements, including the reset button and instructions."""
        # Draw the reset button
        pygame.draw.rect(self.screen, self.button_color, self.button_rect)
        text_surf = self.font.render("Reset", True, WHITE)
        text_rect = text_surf.get_rect(center=self.button_rect.center)
        self.screen.blit(text_surf, text_rect)

        # Draw the instruction text
        for surface, rect in self.text_surfaces:
            self.screen.blit(surface, rect)

    def draw_grid(self):
        """Draws the grid lines on the screen."""
        grid_height = self.warehouse.height * self.cell_size
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, BLACK, (x, 0), (x, grid_height))
        for y in range(0, grid_height + 1, self.cell_size):
            pygame.draw.line(self.screen, BLACK, (0, y), (self.width, y))

    def draw_objects(self):
        """Draws all objects (robot, package, obstacles) onto the grid."""
        color_map = {'R': RED, '📦': BROWN, '1': BLACK}
        for row in range(self.warehouse.height):
            for col in range(self.warehouse.width):
                symbol = self.warehouse.grid[row][col]
                if symbol in color_map:
                    color = color_map[symbol]
                    rect = pygame.Rect(col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size)
                    pygame.draw.rect(self.screen, color, rect)

    def draw_path(self):
        """Draws the calculated path on the grid if it exists."""
        if not self.path:
            return
        
        for i, pos in enumerate(self.path):
            row, col = pos
            center_x = col * self.cell_size + self.cell_size // 2
            center_y = row * self.cell_size + self.cell_size // 2
            
            color = YELLOW
            if i == 0 or i == len(self.path) - 1:
                color = GREEN
                
            pygame.draw.circle(self.screen, color, (center_x, center_y), self.cell_size // 6)

    def run(self):
        """Starts the main application loop.

        This loop handles event processing (mouse, keyboard), updates the
        application state, and redraws the screen on each frame.
        """
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    row, col = self.get_grid_pos(event.pos)
                    
                    if self.button_rect.collidepoint(event.pos):
                        self.warehouse.reset()
                        self.path = None
                        print("Warehouse has been reset.")
                    
                    elif row is not None:
                        # Left Click: Place obstacles
                        if event.button == 1:
                            if self.warehouse.grid[row][col] == '0':
                                self.warehouse.grid[row][col] = '1'
                                self.path = None

                        # Right Click: Place/move the package
                        elif event.button == 3:
                            if self.warehouse.package:
                                old_r, old_c = self.warehouse.package.row, self.warehouse.package.column
                                self.warehouse.grid[old_r][old_c] = '0'

                            if self.warehouse.grid[row][col] == '0':
                                self.warehouse.add_package(row=row, col=col)
                                self.path = None
                
                if event.type == pygame.KEYDOWN:
                    # Press SPACE to find the path
                    if event.key == pygame.K_SPACE:
                        if self.warehouse.package:
                            print("Searching for a path...")
                            self.path = self.warehouse.find_path()
                            if self.path:
                                print("Path Found!")
                            else:
                                print("No path could be found.")
                        else:
                            print("Cannot find path: Please place a package first.")

            # Drawing
            self.screen.fill(WHITE)
            if self.path:
                self.draw_path()
            self.draw_objects()
            self.draw_grid()
            self.draw_ui()

            # Update Display
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()