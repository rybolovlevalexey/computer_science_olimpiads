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
    text = font.render("Введите имя пользователя", True, (100, 255, 100))
    text_x = w // 2 - text.get_width() // 2
    text_y = h // 2 - text.get_height() // 2 - 250
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (0, 255, 0), (text_x - 10, text_y - 10,
                                           text_w + 20, text_h + 20), 1)

    text1 = font.render("", True, (100, 255, 100))
    text1_x = w // 2 - text.get_width() // 2
    text1_y = h // 2 - text.get_height() // 2 - 150
    screen.blit(text1, (text1_x, text1_y))

    button1 = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((50, 300), (250, 50)),
        text='Приветствие пользователя',
        manager=manager
    )
    button2 = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((450, 300), (250, 50)),
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

                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if len(line_with_name.get_text()) == 0:
                        screen.fill((0, 0, 0))
                        text1 = font.render(f"Вы ничего не ввели", True,
                                            (100, 255, 100))
                        screen.blit(text1, (text1_x, text1_y - 100))
                    else:
                        if event.ui_element == button1:
                            screen.fill((0, 0, 0))
                            text1 = font.render(f"Приветствую, {line_with_name.get_text()}", True, (100, 255, 100))
                            screen.blit(text1, (text1_x, text1_y - 100))
                        else:
                            screen.fill((0, 0, 0))
                            text1 = font.render(f"Всего хорошего, {line_with_name.get_text()}", True, (100, 255, 100))
                            screen.blit(text1, (text1_x, text1_y- 100))

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
