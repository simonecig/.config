const char *colorname[] = {

  /* 8 normal colors */
  [0] = "#292929", /* black   */
  [1] = "#CF6A4C", /* red     */
  [2] = "#19CB00", /* green   */
  [3] = "#FAD07A", /* yellow  */
  [4] = "#8197BF", /* blue    */
  [5] = "#8787AF", /* magenta */
  [6] = "#668799", /* cyan    */
  [7] = "#888888", /* white   */

  /* 8 bright colors */
  [8]  = "#525252",  /* black   */
  [9]  = "#CF6A4C",  /* red     */
  [10] = "#19CB00", /* green   */
  [11] = "#FAD07A", /* yellow  */
  [12] = "#8197BF", /* blue    */
  [13] = "#8787AF", /* magenta */
  [14] = "#668799", /* cyan    */
  [15] = "#888888", /* white   */

  /* special colors */
  [256] = "#151515", /* background */
  [257] = "#888888", /* foreground */
  [258] = "#FF9D80",     /* cursor */
};

/* Default colors (colorname index)
 * foreground, background, cursor */
 unsigned int defaultbg = 0;
 unsigned int defaultfg = 257;
 unsigned int defaultcs = 258;
 unsigned int defaultrcs= 258;
