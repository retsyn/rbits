# bits.py
# Contains one class; Bitfield, allowing for light weight bitfields to be defined by strings.

class Bitfield:
    '''
    A class that masks a list as a bitfield.  Can convert to decimal easily, flip bits.
    '''
    def __init__(self, bit_string = ""):
        
        self.bits = []
        
        for char in bit_string:
            if(char == '0'):
                self.bits.append(False)
            elif(char == '1'):
                self.bits.append(True)
            else:
                print("Warning: Skipping char {}-- only recording 1s and 0s.".format(char))
        
        return
        
        
    def _as_string(self):
        '''
        Returns self.bits as a string.
        '''
        
        string = ""
        
        for bit in self.bits:
            if(bit):
                string += '1'
            else:
                string += '0'
        
        return string
                
           
    def flip(self, i=None):
        '''
        flips any bit in the sequence to it's opposing value.  If an index 'i' isn't specified, then
        flip them all.

        Usage:
        instance.flip(i)
        i - int value of index of bit to flip.
        '''

        if(i is not None):
            self.bits[i] = not self.bits[i]
        else:
            for b in range(len(self.bits)):
                self.bits[b] = not self.bits[b]
        
        return


    def as_dec(self):
        '''
        Decimal value quickly calcuated by casting the "as string" as an int, with a base of 2.
        '''
        
        num = int(self._as_string(), 2)

        return num


    def __getitem__(self, i):
        '''
        We just wrap self.bits and return it's elements
        '''

        return self.bits[i]


    def __len__(self):
        '''
        We just return the length of self.bits
        '''

        return len(self.bits)


    def __str__(self):
        '''
        We re-use the as_string() method, which is abstracted away from __str__.
        '''

        return self._as_string()


    def __trunc__(self):
        '''
        Wrap .as_dec() whenever we cast this as an in, providing the decimal value.
        '''

        return self.as_dec()