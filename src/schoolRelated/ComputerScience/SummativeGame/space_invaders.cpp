// to run:
// clang++ space_invaders.cpp -o ./target/space_invaders $(pkg-config allegro-5 allegro_main-5 allegro_font-5 allegro_primitives-5 allegro_image-5 --libs --cflags); ./target/space_invaders

#include <allegro5/allegro.h>
#include <allegro5/allegro_image.h>
#include <allegro5/allegro_primitives.h>

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#include "helpers/structs.cpp"
#include "helpers/globals.cpp"
#include "helpers/rewritten_allegro_crap.cpp"
#include "helpers/colors.cpp"
#include "helpers/functions.cpp"
#include "helpers/keybinds.cpp"

#define projectile_speed 30
#define enemy_speed 5

Object player;

Object projectile_template;
Object projectiles[100];

Object enemy_template;
Object enemies[100];

//Panel test_panel;

void frame_logic() {
    player.position.x = get_mouse_pos().x;

    fill_screen(WHITE);
    draw(player);

    //draw(test_panel);

    for (int i = 0; i < 100; i++) {
        if (projectiles[i].exists) {
            update_position(projectiles[i]);
            draw(projectiles[i]);
            if (projectiles[i].position.y < 0) {
                projectiles[i].exists = false;
            }
        }
    }

    if (rand() % 50 == 0) {
        Object new_enemy = enemy_template;
        new_enemy.position = {(rand() % get_display_width()), 0};
        
        for (int i = 0; i < 100; i++) {
            if (enemies[i].image == NULL || !enemies[i].exists) {
                enemies[i] = new_enemy;
                enemies[i].velocity.y = enemy_speed;
                break;
            }
        }
    }

    for (int i = 0; i < 100; i++) {
        if (enemies[i].exists) {
            update_position(enemies[i]);
            draw(enemies[i]);
            if (enemies[i].position.y > get_display_height()) {
                enemies[i].exists = false;
            }
        }
    }

    for (int i = 0; i < 100; i++) {
        for (int j = 0; j < 100; j++) {
            if (projectiles[i].exists && enemies[j].exists && is_colliding(projectiles[i], enemies[j])) {
                projectiles[i].exists = false;
                enemies[j].exists = false;
            }
        }
    }
}

// Handling the keyboard input ev is the allegro event
void handle_keyboard_input_down(ALLEGRO_EVENT ev) {
    if (pressing_keybind(kill_keybind, ev)) {
        printf("Exiting due to kill keybind\n");
        al_destroy_display(display);
        exit(0);
    }
}

void handle_keyboard_input_up(ALLEGRO_EVENT ev) {
    // Currently not used
}

void handle_mouse_input(ALLEGRO_EVENT ev) {
    //if (is_within(test_panel, get_camera_mouse_pos())) {
    //    printf("Clicked within panel\n");
    //}

    Object new_projectile = projectile_template;
    new_projectile.position = player.position;
    new_projectile.velocity.y = -projectile_speed;
    
    for (int i = 0; i < 100; i++) {
        if (projectiles[i].image == NULL || !projectiles[i].exists) {
            projectiles[i] = new_projectile;
            break;
        }
    }
}

int main(int argc, char *argv[]) {    
    if (!init_allegro()) {
        return -1;
    }

    srand(time(0));

    load_image_with_checks("images/sun.png", player.image);
    player.position = {0, (int)(get_display_height() * 0.9)};
    player.scale = {0.5, 0.5};
    player.exists = true;

    load_image_with_checks("images/sun.png", projectile_template.image);
    projectile_template.scale = {0.2, 0.2};
    projectile_template.exists = true;

    load_image_with_checks("images/earth.png", enemy_template.image);
    enemy_template.scale = {0.3, 0.3};
    enemy_template.exists = true;

    //test_panel.top_left = {10, 10};
    //test_panel.bottom_right = {get_window_size().x / 2, get_window_size().y / 2};
    //test_panel.color = BLUE;

    al_start_timer(timer);
    al_get_mouse_cursor_position(&mouse_pos.x, &mouse_pos.y);
    while(true) {
        ALLEGRO_EVENT ev;

        al_wait_for_event(event_queue, &ev);

        if (ev.type == ALLEGRO_EVENT_MOUSE_AXES) {
            mouse_pos = {ev.mouse.x, ev.mouse.y};
        }

        // Handling Input
        if (ev.type == ALLEGRO_EVENT_MOUSE_BUTTON_DOWN) {
            handle_mouse_input(ev);
        }

        if (ev.type == ALLEGRO_EVENT_KEY_DOWN) {
            handle_keyboard_input_down(ev);
        }

        if (ev.type == ALLEGRO_EVENT_KEY_UP) {
            handle_keyboard_input_up(ev);
        }

        // Run frame logic
        if(ev.type == ALLEGRO_EVENT_TIMER) {
            frame_logic();
            update();
        }
    }

    al_destroy_display(display);
    return 0;
}
