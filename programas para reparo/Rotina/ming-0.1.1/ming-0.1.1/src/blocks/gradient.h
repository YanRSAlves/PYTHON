/*
    Ming, an SWF output library
    Copyright (C) 2001  Opaque Industries - http://www.opaque.net/

    This library is free software; you can redistribute it and/or
    modify it under the terms of the GNU Lesser General Public
    License as published by the Free Software Foundation; either
    version 2.1 of the License, or (at your option) any later version.

    This library is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
    Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public
    License along with this library; if not, write to the Free Software
    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
*/

/* gradient.h */

#ifndef SWF_GRADIENT_H_INCLUDED
#define SWF_GRADIENT_H_INCLUDED

#include "output.h"
#include "matrix.h"
#include "bitmap.h"

struct _gradientEntry
{
  byte ratio;
  byte r;
  byte g;
  byte b;
  byte a;
};

struct _gradient
{
  struct _gradientEntry entries[8];
  int nGrads;
};
typedef struct _gradient *SWFGradient;

#define GRADIENT_SIZE sizeof(struct _gradient)

SWFGradient newSWFGradient();
void destroySWFGradient(SWFGradient gradient);

void SWFGradient_addEntry(SWFGradient gradient,
			  float ratio, byte r, byte g, byte b, byte a);

void SWFOutput_writeGradient(SWFOutput out, SWFGradient gradient,
			    SWFBlocktype shapeType);

void SWFOutput_writeMorphGradient(SWFOutput out,
				  SWFGradient gradient1, SWFGradient gradient2);

#endif /* SWF_GRADIENT_H_INCLUDED */
