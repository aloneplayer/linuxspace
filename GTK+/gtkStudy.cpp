#include <gtk/gtk.h>

int main(int argc, char* argv[])
{
	// Main window
	GtkWiindget *win; 
	 
	// Init
	gtk_init(&argc, &argv);

	// Create window
	win = gtk_window_new(GTK_WINDOW_TOPLEVEL);

	//gtk_windget_show(win);
	
	// Main loop
	gtk_main();
	return 0;
}