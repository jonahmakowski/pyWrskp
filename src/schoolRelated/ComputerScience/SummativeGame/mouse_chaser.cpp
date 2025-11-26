// to run:
// clang++ mouse_chaser.cpp -o ./target/mouse_chaser $(pkg-config allegro-5 allegro_main-5 allegro_font-5 allegro_primitives-5 allegro_image-5 --libs --cflags); ./target/mouse_chaser

#include <allegro5/allegro.h>
#include <allegro5/allegro_image.h>
#include <allegro5/allegro_primitives.h>

#include <stdio.h>

#include "helpers/structs.cpp"
#include "helpers/globals.cpp"
#include "helpers/rewritten_allegro_crap.cpp"
#include "helpers/colors.cpp"
#include "helpers/functions.cpp"
#include "helpers/keybinds.cpp"

Object sun;

int speed = 5;

void frame_logic() {
    // Update camera position based on velocity
    update_camera_position();

    sun.velocity.x += (int)(speed * get_direction_to(sun.position, get_mouse_pos()).x);
    sun.velocity.y += (int)(speed * get_direction_to(sun.position, get_mouse_pos()).y);

    sun.velocity.x *= 0.9;
    sun.velocity.y *= 0.9;

    if (is_within(sun, get_mouse_pos())) {
        printf("Got hit!\n");
        exit(0);
    }

    update_position(sun);

    fill_screen(WHITE);
    draw(sun);
}

// Handling the keyboard input ev is the allegro event
void handle_keyboard_input_down(ALLEGRO_EVENT ev) {
    if (pressing_keybind(move_up, ev)) {
        camera.velocity.y = 10;
    } else if (pressing_keybind(move_down, ev)) {
        camera.velocity.y = -10;
    } else if (pressing_keybind(move_left, ev)) {
        camera.velocity.x = 10;
    } else if (pressing_keybind(move_right, ev)) {
        camera.velocity.x = -10;
    } else if (pressing_keybind(kill_keybind, ev)) {
        printf("Exiting due to kill keybind\n");
        exit(0);
    }
}

void handle_keyboard_input_up(ALLEGRO_EVENT ev) {
    if (pressing_keybind(move_up, ev) || pressing_keybind(move_down, ev)) {
        camera.velocity.y = 0;
    } else if (pressing_keybind(move_left, ev) || pressing_keybind(move_right, ev)) {
        camera.velocity.x = 0;
    }
}

void handle_mouse_input(ALLEGRO_EVENT ev) {
    printf("Mouse clicked at (%d, %d)\n", mouse_pos.x, mouse_pos.y);
    sun.scale.x += 0.1;
}

int main(int argc, char *argv[]) {    
    if (!init_allegro()) {
        return -1;
    }

    long frames = 0;

    load_image_with_checks("images/sun.png", sun.image);
    sun.position = {0, 0};
    sun.scale = {0.5, 0.5};

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
            frames += 1;
        }

        if (frames % (FPS * 3) == 0) {
            speed += 1;
        }
    }

    al_destroy_display(display);
    return 0;
}
