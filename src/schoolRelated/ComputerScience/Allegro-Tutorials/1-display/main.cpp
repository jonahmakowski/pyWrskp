#include <allegro5/allegro.h>
#include <stdio.h>


int main(int argc, char *argv[]) {
    al_init(); //initialize allegro

    //create pointer to allegro display and initialize using al_create_display
    ALLEGRO_DISPLAY *display = nullptr;
    display = al_create_display(1080, 720);

    //exit program if program fails to create display
    if(!display) {
        printf("Display failed\n");
        return -1;
    }

    al_set_window_title(display, "ALLEGRO Tutorial 1");//set window title

    //define allegro colors white and grey
    ALLEGRO_COLOR white = al_map_rgb(255,255,255);
    ALLEGRO_COLOR grey = al_map_rgb(128,128,128);

    //set screen to white and wait 5 seconds
    al_clear_to_color(white);//set buffer to white
    al_flip_display();//show buffer to screen
    al_rest(5);//delay

    //set screen to grey and wait 5 seconds
    al_clear_to_color(grey);
    al_flip_display();
    al_rest(5);

    //free memory and end program
    al_destroy_display(display);
    return 0;
}
