static const char norm_fg[] = "#a8a6b1";
static const char norm_bg[] = "#07060c";
static const char norm_border[] = "#524d63";

static const char sel_fg[] = "#a8a6b1";
static const char sel_bg[] = "#7a2d4b";
static const char sel_border[] = "#a8a6b1";

static const char urg_fg[] = "#a8a6b1";
static const char urg_bg[] = "#56345c";
static const char urg_border[] = "#56345c";

static const char *colors[][3]      = {
    /*               fg           bg         border                         */
    [SchemeNorm] = { norm_fg,     norm_bg,   norm_border }, // unfocused wins
    [SchemeSel]  = { sel_fg,      sel_bg,    sel_border },  // the focused win
    [SchemeUrg] =  { urg_fg,      urg_bg,    urg_border },
};
