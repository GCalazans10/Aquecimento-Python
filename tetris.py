import pygame
import random

# Inicializa o pygame
pygame.init()

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
COLORS = [
    (0, 255, 255),  # I - ciano
    (0, 0, 255),     # J - azul
    (255, 165, 0),   # L - laranja
    (255, 255, 0),   # O - amarelo
    (0, 255, 0),     # S - verde
    (128, 0, 128),   # T - roxo
    (255, 0, 0)      # Z - vermelho
]

# Configurações do jogo
CELL_SIZE = 30
GRID_WIDTH = 10
GRID_HEIGHT = 20
SCREEN_WIDTH = CELL_SIZE * (GRID_WIDTH + 6)
SCREEN_HEIGHT = CELL_SIZE * GRID_HEIGHT

# Formatos das peças (tetrominós)
SHAPES = [
    [[1, 1, 1, 1]],  # I
    
    [[1, 0, 0],
     [1, 1, 1]],     # J
     
    [[0, 0, 1],
     [1, 1, 1]],     # L
     
    [[1, 1],
     [1, 1]],        # O
     
    [[0, 1, 1],
     [1, 1, 0]],     # S
     
    [[0, 1, 0],
     [1, 1, 1]],     # T
     
    [[1, 1, 0],
     [0, 1, 1]]      # Z
]

# Cria a tela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

class Tetris:
    def __init__(self):
        self.grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.current_piece = self.new_piece()
        self.game_over = False
        self.score = 0
        
    def new_piece(self):
        # Escolhe uma peça aleatória
        shape = random.choice(SHAPES)
        color = COLORS[SHAPES.index(shape)]
        
        # Posição inicial (centro no topo)
        x = GRID_WIDTH // 2 - len(shape[0]) // 2
        y = 0
        
        return {"shape": shape, "color": color, "x": x, "y": y}
    
    def valid_move(self, piece, x_offset=0, y_offset=0):
        for y, row in enumerate(piece["shape"]):
            for x, cell in enumerate(row):
                if cell:
                    new_x = piece["x"] + x + x_offset
                    new_y = piece["y"] + y + y_offset
                    
                    if (new_x < 0 or new_x >= GRID_WIDTH or 
                        new_y >= GRID_HEIGHT or 
                        (new_y >= 0 and self.grid[new_y][new_x])):
                        return False
        return True
    
    def lock_piece(self, piece):
        for y, row in enumerate(piece["shape"]):
            for x, cell in enumerate(row):
                if cell:
                    self.grid[piece["y"] + y][piece["x"] + x] = piece["color"]
        
        # Verifica linhas completas
        self.clear_lines()
        
        # Cria nova peça
        self.current_piece = self.new_piece()
        
        # Verifica game over
        if not self.valid_move(self.current_piece):
            self.game_over = True
    
    def clear_lines(self):
        lines_cleared = 0
        for y in range(GRID_HEIGHT):
            if all(self.grid[y]):
                lines_cleared += 1
                # Move todas as linhas acima para baixo
                for y2 in range(y, 0, -1):
                    self.grid[y2] = self.grid[y2-1][:]
                self.grid[0] = [0 for _ in range(GRID_WIDTH)]
        
        # Atualiza pontuação
        if lines_cleared == 1:
            self.score += 100
        elif lines_cleared == 2:
            self.score += 300
        elif lines_cleared == 3:
            self.score += 500
        elif lines_cleared == 4:
            self.score += 800
    
    def rotate_piece(self):
        # Transpõe a matriz da peça
        rotated = [[self.current_piece["shape"][x][y] 
                   for x in range(len(self.current_piece["shape"]))] 
                   for y in range(len(self.current_piece["shape"][0])-1, -1, -1)]
        
        old_shape = self.current_piece["shape"]
        self.current_piece["shape"] = rotated
        
        # Se a rotação não for válida, volta para a forma original
        if not self.valid_move(self.current_piece):
            self.current_piece["shape"] = old_shape
    
    def update(self):
        if not self.game_over:
            if self.valid_move(self.current_piece, 0, 1):
                self.current_piece["y"] += 1
            else:
                self.lock_piece(self.current_piece)
    
    def draw(self):
        # Desenha o grid
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                pygame.draw.rect(screen, GRAY, 
                                (x * CELL_SIZE, y * CELL_SIZE, 
                                 CELL_SIZE, CELL_SIZE), 1)
                if self.grid[y][x]:
                    pygame.draw.rect(screen, self.grid[y][x], 
                                   (x * CELL_SIZE, y * CELL_SIZE, 
                                    CELL_SIZE, CELL_SIZE))
        
        # Desenha a peça atual
        if not self.game_over:
            for y, row in enumerate(self.current_piece["shape"]):
                for x, cell in enumerate(row):
                    if cell:
                        pygame.draw.rect(screen, self.current_piece["color"], 
                                       ((self.current_piece["x"] + x) * CELL_SIZE, 
                                        (self.current_piece["y"] + y) * CELL_SIZE, 
                                        CELL_SIZE, CELL_SIZE))
        
        # Desenha a pontuação
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Score: {self.score}", True, WHITE)
        screen.blit(score_text, (CELL_SIZE * GRID_WIDTH + 10, 20))
        
        if self.game_over:
            game_over_font = pygame.font.SysFont(None, 48)
            game_over_text = game_over_font.render("GAME OVER!", True, (255, 0, 0))
            screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 120, SCREEN_HEIGHT // 2 - 30))

# Cria o jogo
game = Tetris()

# Loop principal
running = True
fall_time = 0
fall_speed = 0.5  # segundos

while running:
    # Tempo delta
    dt = clock.tick(60) / 1000  # Converte para segundos
    fall_time += dt
    
    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if not game.game_over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if game.valid_move(game.current_piece, -1, 0):
                        game.current_piece["x"] -= 1
                elif event.key == pygame.K_RIGHT:
                    if game.valid_move(game.current_piece, 1, 0):
                        game.current_piece["x"] += 1
                elif event.key == pygame.K_DOWN:
                    if game.valid_move(game.current_piece, 0, 1):
                        game.current_piece["y"] += 1
                elif event.key == pygame.K_UP:
                    game.rotate_piece()
                elif event.key == pygame.K_SPACE:
                    # Hard drop
                    while game.valid_move(game.current_piece, 0, 1):
                        game.current_piece["y"] += 1
                    game.lock_piece(game.current_piece)
    
    # Atualização automática (queda da peça)
    if fall_time >= fall_speed and not game.game_over:
        game.update()
        fall_time = 0
    
    # Desenho
    screen.fill(BLACK)
    game.draw()
    pygame.display.update()

pygame.quit()