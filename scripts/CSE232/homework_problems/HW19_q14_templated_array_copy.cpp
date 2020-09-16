/*
Write a function (named "templated_array_copy") that takes two parameters (two arrays of the same type). 
It copies the first array into the second. Note, it the arrays are different sizes, only copy what fits.
*/

#include <algorithm>
#include <iterator>

template<typename Type, size_t Size1, size_t Size2>
void templated_array_copy(Type (&ary1)[Size1], Type (&ary2)[Size2]){
  if (Size2 < Size1){
  std::copy(ary1, ary1+Size2,ary2);
  } else {
  std::copy(ary1, ary1+Size1,ary2);
  }
}

// solution code
/*
template<typename Type, size_t size_source, size_t size_dest>
void templated_array_copy(
    const Type(&source)[size_source],
    Type(&dest)[size_dest]) {
  int i;
  for (i = 0; i < size_source && i < size_dest; ++i) {
    dest[i] = source[i];
  }
}
*/
