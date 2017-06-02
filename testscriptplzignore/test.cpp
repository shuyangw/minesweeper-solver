#include <windows.h>

int main()
{
	COLORREF color = RGB(255,0,0); // COLORREF to hold the color info

	SetConsoleTitle("Pixel In Console?"); // Set text of the console so you can find the window

	HWND hwnd = FindWindow(NULL, "Minewsweeper X"); // Get the HWND
	HDC hdc = GetDC(hwnd); // Get the DC from that HWND

	SetPixel(hdc, 30, 30, color); // SetPixel(HDC hdc, int x, int y, COLORREF color)
    
        ReleaseDC(hwnd, hdc); // Release the DC
	DeleteDC(hdc); // Delete the DC
	return(0);
}