# rbits
This exists for two reasons-- _One_; I want to compel animation tech directors who work in Maya AWAY
from dangerously bringing PIP into their Maya installs-- a recipe for disaster, so things missing 
from a Maya scripting world I want to make alternatives to.  (If I ship another script to an 
animation studio that breaks due to a numpy dependency a co-worker stuck in there I'll scream.)

_Secondly_; I had a student working on Advent of Code who was solving the puzzles in Python 
exclusively-- a strong contender for many puzzles, but kinda dead in the water when it came to ones
involving bits.  This module was to keep up with C++'s bitset, which solved the same problem
trivially.

Todo:
- Might be nice to add bitwise arithmetic stuff automatically if added/subtracted from other
instances of the same.
- Might be nice to do bitmasking too!  BUT if this gets too feature rich it just becomes a worse
version of bitarray instead of a lighter-weight thing.
