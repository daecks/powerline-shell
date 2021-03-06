# Basic theme which only uses colors in 0-15 range

class Color(DefaultColor):
    USERNAME_FG = 8
    USERNAME_BG = 15
    USERNAME_ROOT_BG = 1

    HOSTNAME_FG = 8
    HOSTNAME_BG = 7

    HOME_SPECIAL_DISPLAY = True
    HOME_BG = 31  # blueish, only if HOME_SPECIAL_DISPLAY is True
    PATH_BG = 8 # dark grey
    PATH_FG = 7 # light grey
    CWD_FG = 15 # white
    SEPARATOR_FG = 7

    READONLY_BG = 1
    READONLY_FG = 15

    REPO_CLEAN_BG = 148  # a light green color
    REPO_CLEAN_FG = 0  # black
    REPO_DIRTY_BG = 148  # a light green color
    REPO_DIRTY_FG = 0 # black

    JOBS_FG = 14
    JOBS_BG = 8

    CMD_PASSED_BG = 8
    CMD_PASSED_FG = 15
    CMD_FAILED_BG = 11
    CMD_FAILED_FG = 0

    SVN_CHANGES_BG = REPO_DIRTY_BG
    SVN_CHANGES_FG = REPO_DIRTY_FG

    VIRTUAL_ENV_BG = 2
    VIRTUAL_ENV_FG = 0

    GIT_UNTRACKED_BG = 1
    GIT_NOTSTAGED_BG = 166
