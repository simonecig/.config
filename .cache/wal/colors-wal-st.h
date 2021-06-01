const char *colorname[] = {

  /* 8 normal colors */
  [0] = "#0f1314", /* black   */
  [1] = "#39664C", /* red     */
  [2] = "#35685C", /* green   */
  [3] = "#424A4A", /* yellow  */
  [4] = "#487354", /* blue    */
  [5] = "#4E7964", /* magenta */
  [6] = "#58853D", /* cyan    */
  [7] = "#a5bca9", /* white   */

  /* 8 bright colors */
  [8]  = "#738376",  /* black   */
  [9]  = "#39664C",  /* red     */
  [10] = "#35685C", /* green   */
  [11] = "#424A4A", /* yellow  */
  [12] = "#487354", /* blue    */
  [13] = "#4E7964", /* magenta */
  [14] = "#58853D", /* cyan    */
  [15] = "#a5bca9", /* white   */

  /* special colors */
  [256] = "#0f1314", /* background */
  [257] = "#a5bca9", /* foreground */
  [258] = "#a5bca9",     /* cursor */
};

/* Default colors (colorname index)
 * foreground, background, cursor */
 unsigned int defaultbg = 0;
 unsigned int defaultfg = 257;
 unsigned int defaultcs = 258;
 unsigned int defaultrcs= 258;
