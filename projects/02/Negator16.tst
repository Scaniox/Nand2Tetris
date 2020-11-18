load Negator16.hdl,
output-file Negator16.out,
compare-to Negator16.cmp,
output-list in%B1.16.1 out%B1.16.1;

set in %B0000000000000001,  // in = 1
eval,
output;

set in %B1111111111111111,  // in = -1
eval,
output;

set in %B0000000000000101,  // in = 5
eval,
output;

set in %B1111111111111011,  // in = -5
eval,
output;
