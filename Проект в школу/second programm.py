import pygame
import pygame_gui


def start_window():
    # функция в которой находится стартовое окно
    manager = pygame_gui.UIManager((750, 750))
    clock = pygame.time.Clock()
    run = True
    flag_game_start_pushed = False

    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render("Выберите цвет персонажа и кубиков", True, (100, 255, 100))
    text_x = w // 2 - text.get_width() // 2
    text_y = h // 2 - text.get_height() // 2 - 250
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (0, 255, 0), (text_x - 10, text_y - 10,
                                           text_w + 20, text_h + 20), 1)

    button1 = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((50, 300 - 75), (250, 50)),
        text='Приветствие пользователя',
        manager=manager
    )
    button2 = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((450, 300 - 75), (250, 50)),
        text='Прощание с пользователем',
        manager=manager
    )

    line_with_name = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((275, 600 - 75), (200, 50)),
        manager=manager
    )

    while run:
        time_delta = clock.tick(60) / 1000
        for event in pygame.event.get():

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_element == line_with_name:
                    global PLAYER_NAME
                    PLAYER_NAME = event.text



                # при нажатии на кнопку "Начало игры" появляется надпись "Игра начинается"
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == button1:
                        return True
                        # можно запускать окно игры

                # при наведении на кнопку "Начало игры" появляется надпись "Игра готовится к запуску..."
                if event.user_type == pygame_gui.UI_BUTTON_ON_HOVERED and not flag_game_start_pushed:
                    if event.ui_element == button1:
                        screen.fill((0, 0, 0))
                        font = pygame.font.Font(None, 50)
                        text = font.render("Игра готовится к запуску...", True, (100, 255, 100))
                        text_x = w // 2 - text.get_width() // 2
                        text_y = h // 2 - text.get_height() // 2 - 250
                        text_w = text.get_width()
                        text_h = text.get_height()
                        screen.blit(text, (text_x, text_y))
                        pygame.draw.rect(screen, (0, 255, 0), (text_x - 10, text_y - 10,
                                                               text_w + 20, text_h + 20), 1)

                if event.user_type == pygame_gui.UI_BUTTON_ON_UNHOVERED and not flag_game_start_pushed:
                    if event.ui_element == button1:
                        screen.fill((0, 0, 0))
                        font = pygame.font.Font(None, 50)
                        text = font.render("Выберите цвет персонажа и кубиков", True, (100, 255, 100))
                        text_x = w // 2 - text.get_width() // 2
                        text_y = h // 2 - text.get_height() // 2 - 250
                        text_w = text.get_width()
                        text_h = text.get_height()
                        screen.blit(text, (text_x, text_y))
                        pygame.draw.rect(screen, (0, 255, 0), (text_x - 10, text_y - 10,
                                                               text_w + 20, text_h + 20), 1)

            manager.process_events(event)
        manager.update(time_delta)
        manager.draw_ui(screen)
        pygame.display.update()
    return False


if __name__ == '__main__':
    pygame.init()
    size = w, h = 750, 750
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Тестовое окно')
    start_one_more_time = False

    while True:
        screen.fill((0, 0, 0))
        flag = start_window()
        if not start_one_more_time:
            break
        start_one_more_time = False

    pygame.quit()
