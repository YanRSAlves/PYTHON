
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <gif_lib.h>
#include <zlib.h>

#define max(a,b,c) (((a)>(b))?(((c)>(a))?(c):(a)):(((c)>(b))?(c):(b)))

void error(char *msg)
{
  printf("%s:\n\n", msg);
  PrintGifError();
  exit(-1);
}

unsigned char *readGif(char *fileName, int *length)
{
  GifFileType *file;
  char *bits;
  unsigned char colorMap[256];
  unsigned char *data;
  int i, nColors, size;

  if((file = DGifOpenFileName(fileName)) == NULL)
    error("Error opening file");

  if(DGifSlurp(file) != GIF_OK)
    error("Error slurping file");

  /* data should now be available */

  nColors = file->SColorMap->ColorCount;

  for(i=0; i<nColors; ++i)
  {
    GifColorType c = file->SColorMap->Colors[i];

    colorMap[i] = max(c.Blue, c.Red, c.Green);
  }

  bits = file->SavedImages[0].RasterBits;

  size = file->SWidth * file->SHeight;
  data = malloc(size);

  for(i=0; i<size; ++i)
    data[i] = colorMap[(unsigned char)bits[i]];

  *length = size;

  return data;
}

void usage()
{
  printf("gif2mask - convert a gif image to an alpha mask\n");
  printf("\nusage: gif2mask <file.gif>\n");

  exit(0);
}

int main(int argc, char *argv[])
{
  int len, size;
  long outsize;
  char *outfile;
  unsigned char *data, *outdata;
  FILE *mask;

  if(argc < 1)
    usage();

  len = strlen(argv[1]);

  if(strcmp(argv[1]+len-4, ".gif") != 0)
    usage();

  outfile = strdup(argv[1]);

  outfile[len-3] = 'm';
  outfile[len-2] = 's';
  outfile[len-1] = 'k';

  data = readGif(argv[1], &size);

  outdata = malloc(outsize = (int)floor(size*1.01+12));

  /* zlib-compress the gif data */

  compress2(outdata, &outsize, data, size, 9);

  /* dump to outfile */

  mask = fopen(outfile, "wb");

  if(fwrite(outdata, sizeof(char), outsize, mask) != outsize)
  {
    printf("Didn't write all of the file!");
    exit(-1);
  }

  exit(0);
}
