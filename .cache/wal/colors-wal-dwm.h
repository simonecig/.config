static const char norm_fg[] = "#cbc7bf";
static const char norm_bg[] = "#0A0E16";
static const char norm_border[] = "#8e8b85";

static const char sel_fg[] = "#cbc7bf";
static const char sel_bg[] = "#924F2F";
static const char sel_border[] = "#cbc7bf";

static const char urg_fg[] = "#cbc7bf";
static const char urg_bg[] = "#6F6659";
static const char urg_border[] = "#6F6659";

static const char *colors[][3]      = {
    /*               fg           bg         border                         */
    [SchemeNorm] = { norm_fg,     norm_bg,   norm_border }, // unfocused wins
    [SchemeSel]  = { sel_fg,      sel_bg,    sel_border },  // the focused win
    [SchemeUrg] =  { urg_fg,      urg_bg,    urg_border },
};
