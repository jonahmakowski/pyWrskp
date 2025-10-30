#include <stdio.h>
#include <allegro5/allegro.h>
#include <allegro5/allegro_image.h>
#include <allegro5/allegro_primitives.h>

//create pointer to allegro display and initialize using al_create_display
ALLEGRO_DISPLAY *display = nullptr;

//reserve color variables (define)
ALLEGRO_COLOR light_blue;
ALLEGRO_COLOR green;

//define bitmaps
ALLEGRO_BITMAP *sun = nullptr;
ALLEGRO_BITMAP *character = nullptr;

bool initialize_allegro(int w, int h) {
    if(!al_init() || !al_init_image_addon() || !al_init_primitives_addon()) {
        printf("failed to initalize libraries\n");
        return false;
    }

    //exit program if program fails to create display
    display = al_create_display(w, h);
    if(!display) {
        printf("Display failed\n");
        return false;
    }

    al_set_window_title(display, "ALLEGRO Tutorial 2");//set window title
    return true;
}

void drawWindow(int i) {
    al_clear_to_color(light_blue);//draw background blue color

    //draw house
    al_draw_filled_rectangle(0, 450, 1080, 720, green);
    al_draw_filled_rectangle(600, 250, 900, 450, al_map_rgb_f(.79, .25, .32));
    al_draw_filled_rectangle(750, 275, 800, 325, light_blue);
    al_draw_filled_triangle(550, 250, 950, 250, 750, 150, al_map_rgb_f(.79, .25, .32));

    //draw grass
    for(int j = 50; j < 1020; j += 25)
    {
        al_draw_line(j, 425, j, 450, green, 3.5);
    }

    al_draw_bitmap(sun, 50, 25, 0);//draw sun

    al_draw_bitmap_region(character, i*184, 0, 184, 325, 300, 150, 0);//draw one specific sprite from sprite sheet

    al_flip_display();//show buffer to screen
}

int main(int argc, char *argv[])
{
    //initialize and check working correctly
    if(!initialize_allegro(1080, 720))
    {
        return -1;
    }

    //initialize colors
    light_blue = al_map_rgb(128,200,225);
    green = al_map_rgb_f(.48,.98,0);

    //load sun image
    sun = al_load_bitmap("images/sun.png");
    if(!sun) {
        printf("no bitmap\n");
        return -1;
    }

    //load sprite sheet
    character = al_load_bitmap("images/sprite_sheet.png");
    if(!character) {
        printf("no bitmap\n");
        return -1;
    }

    //draw frames at 10fps
    int i = 0;
    while(true)
    {
        drawWindow(i);
        al_rest(0.1);//delay

        //iterate through sprite frames and reset at 8
        i++;
        i %= 8;
    }


    //free memory and end program
    al_destroy_display(display);
    return 0;
}
