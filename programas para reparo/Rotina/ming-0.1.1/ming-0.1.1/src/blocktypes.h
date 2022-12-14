
#ifndef SWF_BLOCKTYPES_H_INCLUDED
#define SWF_BLOCKTYPES_H_INCLUDED

typedef enum
{
  SWF_DEFINESHAPE		=  2,
  SWF_DEFINESHAPE2		= 22,
  SWF_DEFINESHAPE3		= 32,
  SWF_DEFINEMORPHSHAPE	        = 46,
  SWF_DEFINEBITS		=  6,
  SWF_DEFINEBITSJPEG2		= 21,
  SWF_DEFINEBITSJPEG3		= 35,
  SWF_DEFINELOSSLESS		= 20,
  SWF_DEFINELOSSLESS2		= 36,
  SWF_JPEGTABLES		=  8,
  SWF_DEFINEBUTTON		=  7,
  SWF_DEFINEBUTTON2		= 34,
  SWF_DEFINEBUTTONCXFORM	= 23,
  SWF_DEFINEBUTTONSOUND	        = 17,
  SWF_DEFINEFONT		= 10,
  SWF_DEFINEFONT2		= 48,
  SWF_DEFINEFONTINFO		= 13,
  SWF_DEFINETEXT		= 11,
  SWF_DEFINETEXT2		= 33,
  SWF_DEFINESOUND		= 14,
  SWF_SOUNDSTREAMBLOCK	        = 19,
  SWF_SOUNDSTREAMHEAD		= 18,
  SWF_SOUNDSTREAMHEAD2	        = 45,
  SWF_DEFINESPRITE		= 39,
  SWF_PLACEOBJECT		=  4,
  SWF_PLACEOBJECT2		= 26,
  SWF_REMOVEOBJECT		=  5,
  SWF_REMOVEOBJECT2		= 28,
  SWF_SHOWFRAME			=  1,
  SWF_SETBACKGROUNDCOLOR	=  9,
  SWF_FRAMELABEL		= 43,
  SWF_PROTECT			= 24,
  SWF_STARTSOUND		= 15,
  SWF_END			=  0,
  SWF_DOACTION		        = 12
} SWFBlocktype;

#endif /* SWF_BLOCKTYPES_H_INCLUDED */
