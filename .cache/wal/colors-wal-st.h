const char *colorname[] = {

  /* 8 normal colors */
  [0] = "#0A0E16", /* black   */
  [1] = "#6F6659", /* red     */
  [2] = "#924F2F", /* green   */
  [3] = "#947357", /* yellow  */
  [4] = "#7E817B", /* blue    */
  [5] = "#9C8973", /* magenta */
  [6] = "#C7956C", /* cyan    */
  [7] = "#cbc7bf", /* white   */

  /* 8 bright colors */
  [8]  = "#8e8b85",  /* black   */
  [9]  = "#6F6659",  /* red     */
  [10] = "#924F2F", /* green   */
  [11] = "#947357", /* yellow  */
  [12] = "#7E817B", /* blue    */
  [13] = "#9C8973", /* magenta */
  [14] = "#C7956C", /* cyan    */
  [15] = "#cbc7bf", /* white   */

  /* special colors */
  [256] = "#0A0E16", /* background */
  [257] = "#cbc7bf", /* foreground */
  [258] = "#cbc7bf",     /* cursor */
};

/* Default colors (colorname index)
 * foreground, background, cursor */
 unsigned int defaultbg = 0;
 unsigned int defaultfg = 257;
 unsigned int defaultcs = 258;
 unsigned int defaultrcs= 258;
