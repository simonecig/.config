const char *colorname[] = {

  /* 8 normal colors */
  [0] = "#07060c", /* black   */
  [1] = "#56345c", /* red     */
  [2] = "#7a2d4b", /* green   */
  [3] = "#5c4c58", /* yellow  */
  [4] = "#ae3c5f", /* blue    */
  [5] = "#94818c", /* magenta */
  [6] = "#948c94", /* cyan    */
  [7] = "#a8a6b1", /* white   */

  /* 8 bright colors */
  [8]  = "#524d63",  /* black   */
  [9]  = "#56345c",  /* red     */
  [10] = "#7a2d4b", /* green   */
  [11] = "#5c4c58", /* yellow  */
  [12] = "#ae3c5f", /* blue    */
  [13] = "#94818c", /* magenta */
  [14] = "#948c94", /* cyan    */
  [15] = "#a8a6b1", /* white   */

  /* special colors */
  [256] = "#07060c", /* background */
  [257] = "#a8a6b1", /* foreground */
  [258] = "#a8a6b1",     /* cursor */
};

/* Default colors (colorname index)
 * foreground, background, cursor */
 unsigned int defaultbg = 0;
 unsigned int defaultfg = 257;
 unsigned int defaultcs = 258;
 unsigned int defaultrcs= 258;
