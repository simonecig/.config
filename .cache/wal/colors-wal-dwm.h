static const char norm_fg[] = "#a5bca9";
static const char norm_bg[] = "#0f1314";
static const char norm_border[] = "#738376";

static const char sel_fg[] = "#a5bca9";
static const char sel_bg[] = "#35685C";
static const char sel_border[] = "#a5bca9";

static const char urg_fg[] = "#a5bca9";
static const char urg_bg[] = "#39664C";
static const char urg_border[] = "#39664C";

static const char *colors[][3]      = {
    /*               fg           bg         border                         */
    [SchemeNorm] = { norm_fg,     norm_bg,   norm_border }, // unfocused wins
    [SchemeSel]  = { sel_fg,      sel_bg,    sel_border },  // the focused win
    [SchemeUrg] =  { urg_fg,      urg_bg,    urg_border },
};
