#include <gtk/gtk.h>

// callback function
void hello(GtkWindget *widget, gpointer data)
{
	g_print("hello!");
}

gint delete_event(GtkWidget *widget, GdkEvent *event, gpointer data)
{
	g_print("Delete event was raised");
	return FALSE;
}

void destroy(GtkWindget *widget, gpointer data)
{
	gtk_main_quit();
}

int main(int argc, char* argv[])
{
	// Main window
	GtkWiindget *win; 
	GtkWiindget *button; 

	// Init
	gtk_init(&argc, &argv);

	// Create window
	win = gtk_window_new(GTK_WINDOW_TOPLEVEL);

	g_signal_connect(mainwindow, "dele_event", (GCallback)delete_event, NULL);
	g_signal_connect(mainwindow, "destroy", (GCallback)delete_event, NULL);

	// Set window border
	gtk_container_set_border_width(GTK_CONTAINER(win), 50);

	button = gtk_button_new_with_label("Hello!");
	g_signal_connect(button, "clicked", (GCallback)hello, NULL);

	gtk_container_add(GTK_CONTAINER(win), button);

	gtk_windget_show(button);
	gtk_windget_show(win);
	
	// Main loop
	gtk_main();
	return 0;
}