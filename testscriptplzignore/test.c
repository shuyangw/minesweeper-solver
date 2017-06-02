#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
 
/* Image parameters */
#define W 320
#define H 256
#define M 255
 
/* This is where we'll store the pixels */
uint8_t r[H][W], g[H][W], b[H][W];
 
/* Draw a full 2*pi period of the sine */
void
create_image ( void )
{
    /* Run the width of the image */
    for ( int x=0; x<W; x++ )
    {
        /* Scale the wave to the image height */
        int y = (H/2) +
            (H/2) * sin ( 2 * 3.141593 * (x/(double)W) );
        r[y][x] = 255, g[y][x] = 255, b[y][x] = 255;
    }
}
 
/* Write the ppm-formatted file */
void
write_ppm ( const char *filename )
{
    FILE *out = fopen ( filename, "w" );
    /* Header:
     * Magic number, width, height, maxvalue
     */
    fprintf ( out, "P6 %d %d %d\n", W, H, M );
    /* Rows. 2-byte values if max > 255, 1-byte otherwise.
     * These loops explicitly show where every single byte
     * goes; in practice, it would be faster and shorter to
     * interleave the arrays and write bigger blocks of
     * contiguous data.
     */
    for ( size_t i=0; i<H; i++ )
        for ( size_t j=0; j<W; j++ )
        {
            fwrite ( &r[i][j], sizeof(uint8_t), 1, out ); /* Red */
            fwrite ( &g[i][j], sizeof(uint8_t), 1, out ); /* Green */
            fwrite ( &b[i][j], sizeof(uint8_t), 1, out ); /* Blue */
        }
    fclose ( out );
}
 
/* Make the picture, store it, and go home */
int
main ()
{
    create_image();
    write_ppm ( "sine.ppm" );
    exit ( EXIT_SUCCESS );
}