static const char norm_fg[] = "#888888";
static const char norm_bg[] = "#292929";
static const char norm_border[] = "#525252";

static const char sel_fg[] = "#888888";
static const char sel_bg[] = "#19CB00";
static const char sel_border[] = "#888888";

static const char urg_fg[] = "#888888";
static const char urg_bg[] = "#CF6A4C";
static const char urg_border[] = "#CF6A4C";

static const char *colors[][3]      = {
    /*               fg           bg         border                         */
    [SchemeNorm] = { norm_fg,     norm_bg,   norm_border }, // unfocused wins
    [SchemeSel]  = { sel_fg,      sel_bg,    sel_border },  // the focused win
    [SchemeUrg] =  { urg_fg,      urg_bg,    urg_border },
};
