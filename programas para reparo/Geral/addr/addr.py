# addr.py

def addr():
  retval = []
  addrs = palmdm.open( "AddressDB" )
  recs = addrs.listrecords()
  print "Processing:",
  for index in recs:
    rec = addrs.queryrecord( index)
    buf = rec.getbuffer()
    code = str( buf )
    print index,
    temp = AddrRec( code )
    retval.append( temp )
    rec.release()
  addrs.close()
  return retval

fields ={
  1<<0:"last",
  1<<1:"first",
  1<<2:"company",
  1<<3:"phone 1",
  1<<4:"phone 2",
  1<<5:"phone 3",
  1<<6:"phone 4",
  1<<7:"phone 5",
  1<<8:"address",
  1<<9:"city",
  1<<10:"province",
  1<<11:"zip",
  1<<12:"country",
  1<<13:"title",
  1<<14:"custom 1",
  1<<15:"custom 2",
  1<<16:"custom 3",
  1<<17:"custom 4",
  1<<18:"note"}

class AddrRec:
  def __init__( self, data ):
    flags = self.parse( data[5:8] )
    keys = fields.keys()
    keys.sort()
    self.data={}
    i = 0
    temp = data[9:].split("\0")
    for key in keys:
      if flags & key:
        self.data[fields[key]] = temp[i]
        i = i + 1

  def parse( self, data ):
    flags = 0
    for char in data:
      flags = flags<<8
      flags = flags | ord(char)
    return flags

  def __str__( self ):
    return str(self.data)

x = addr()