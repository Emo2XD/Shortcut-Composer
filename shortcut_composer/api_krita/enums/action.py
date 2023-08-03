# SPDX-FileCopyrightText: © 2022 Wojciech Trybus <wojtryb@gmail.com>
# SPDX-License-Identifier: GPL-3.0-or-later

from krita import Krita as Api

from PyQt5.QtGui import QIcon
from .helpers import EnumGroup, Group


class Action(EnumGroup):
    """
    Contains actions of Krita exposed to the plugin.

    Example usage: `Action.UNDO`
    """

    _file = Group("File")
    NEW = "file_new"
    OPEN = "file_open"
    QUIT = "file_quit"
    SAVE = "file_save"
    SAVE_AS = "file_save_as"
    UNDO = "edit_undo"
    REDO = "edit_redo"
    FULL_SCREEN_MODE = "fullscreen"
    IMPORT_ANIMATION_FRAMES = "file_import_animation"
    IMPORT_VIDEO_ANIMATION = "file_import_video_animation"
    RENDER_ANIMATION = "render_animation"
    RENDER_ANIMATION_AGAIN = "render_animation_again"
    CLOSE_ALL = "file_close_all"
    OPEN_EXISTING_DOCUMENT_AS_UNTITLED_DOCUMENT = "file_import_file"
    EXPORT = "file_export_file"
    EXPORT_ADVANCED = "file_export_advanced"
    DOCUMENT_INFORMATION = "file_documentinfo"
    SAVE_INCREMENTAL_VERSION = "save_incremental_version"
    SAVE_INCREMENTAL_BACKUP = "save_incremental_backup"
    CREATE_TEMPLATE_FROM_IMAGE = "create_template"
    CREATE_COPY_FROM_CURRENT_IMAGE = "create_copy"

    _canvas_navigation = Group("Canvas navigation")
    ROTATE_CANVAS_RIGHT = "rotate_canvas_right"
    ROTATE_CANVAS_LEFT = "rotate_canvas_left"
    RESET_CANVAS_ROTATION = "reset_canvas_rotation"
    INSTANT_PREVIEW_MODE = "level_of_detail_mode"
    SHOW_STATUS_BAR = "showStatusBar"
    SHOW_CANVAS_ONLY = "view_show_canvas_only"
    RULERS_TRACK_POINTER = "rulers_track_mouse"
    RESET_ZOOM = "zoom_to_100pct"
    ZOOM_IN = "view_zoom_in"
    ZOOM_OUT = "view_zoom_out"
    TOGGLE_ZOOM_FIT_TO_PAGE = "toggle_zoom_to_fit"
    MIRROR_VIEW_AROUND_CURSOR = "mirror_canvas_around_cursor"

    _canvas_toggles = Group("Canvas toggles")
    TOGGLE_BRUSH_OUTLINE = "toggle_brush_outline"
    SHOW_GUIDES = "view_show_guides"
    LOCK_GUIDES = "view_lock_guides"
    SHOW_PIXEL_GRID = "view_pixel_grid"
    SNAP_TO_GUIDES = "view_snap_to_guides"
    SNAP_ORTHOGONAL = "view_snap_orthogonal"
    SNAP_NODE = "view_snap_node"
    SNAP_EXTENSION = "view_snap_extension"
    SNAP_INTERSECTION = "view_snap_intersection"
    SNAP_BOUNDING_BOX = "view_snap_bounding_box"
    SNAP_IMAGE_BOUNDS = "view_snap_image_bounds"
    SNAP_IMAGE_CENTRE = "view_snap_image_center"
    SNAP_PIXEL = "view_snap_to_pixel"

    _filters_shortcuts = Group("Filters shortcuts")
    APPLY_FILTER_AGAIN = "filter_apply_again"
    APPLY_FILTER_AGAIN_REPROMPT = "filter_apply_reprompt"
    FILTER_ASC_CDL = "krita_filter_asc-cdl"
    AUTO_CONTRAST = "krita_filter_autocontrast"
    BLUR = "krita_filter_blur"
    BURN = "krita_filter_burn"
    COLOUR_BALANCE = "krita_filter_colorbalance"
    COLOUR_TO_ALPHA = "krita_filter_colortoalpha"
    COLOUR_TRANSFER = "krita_filter_colortransfer"
    CROSS_CHANNEL_ADJUSTMENT_CURVES = "krita_filter_crosschannel"
    DESATURATE = "krita_filter_desaturate"
    DODGE = "krita_filter_dodge"
    EDGE_DETECTION = "krita_filter_edge detection"
    EMBOSS_WITH_VARIABLE_DEPTH = "krita_filter_emboss"
    EMBOSS_IN_ALL_DIRECTIONS = "krita_filter_emboss all directions"
    EMBOSS_HORIZONTAL_VERTICAL = "krita_filter_emboss horizontal and vertical"
    EMBOSS_HORIZONTAL_ONLY = "krita_filter_emboss horizontal only"
    EMBOSS_LAPLACIAN = "krita_filter_emboss laplascian"
    EMBOSS_VERTICAL_ONLY = "krita_filter_emboss vertical only"
    GAUSSIAN_BLUR = "krita_filter_gaussian blur"
    GAUSSIAN_HIGH_PASS = "krita_filter_gaussianhighpass"
    GAUSSIAN_NOISE_REDUCTION = "krita_filter_gaussiannoisereducer"
    GRADIENT_MAP = "krita_filter_gradientmap"
    HALFTONE = "krita_filter_halftone"
    HEIGHT_TO_NORMAL_MAP = "krita_filter_height to normal"
    HSV_ADJUSTMENT = "krita_filter_hsvadjustment"
    INDEX_COLOURS = "krita_filter_indexcolors"
    INVERT = "krita_filter_invert"
    LENS_BLUR = "krita_filter_lens blur"
    LEVELS = "krita_filter_levels"
    MAXIMISE_CHANNEL = "krita_filter_maximize"
    MEAN_REMOVAL = "krita_filter_mean removal"
    MINIMISE_CHANNEL = "krita_filter_minimize"
    MOTION_BLUR = "krita_filter_motion blur"
    RANDOM_NOISE = "krita_filter_noise"
    NORMALISE = "krita_filter_normalize"
    OILPAINT = "krita_filter_oilpaint"
    PALETTISE = "krita_filter_palettize"
    COLOUR_ADJUSTMENT_CURVES = "krita_filter_perchannel"
    PHONG_BUMPMAP = "krita_filter_phongbumpmap"
    PIXELISE = "krita_filter_pixelize"
    POSTERISE = "krita_filter_posterize"
    RAINDROPS = "krita_filter_raindrops"
    RANDOM_PICK = "krita_filter_randompick"
    ROUND_CORNERS = "krita_filter_roundcorners"
    SHARPEN = "krita_filter_sharpen"
    SMALL_TILES = "krita_filter_smalltiles"
    THRESHOLD = "krita_filter_threshold"
    UNSHARP_MASK = "krita_filter_unsharp"
    WAVE = "krita_filter_wave"
    WAVELET_NOISE_REDUCER = "krita_filter_waveletnoisereducer"

    _edit_document = Group("Edit document")
    CUT = "edit_cut"
    COPY = "edit_copy"
    PASTE = "edit_paste"
    COPY_SHARP = "copy_sharp"
    CUT_SHARP = "cut_sharp"
    PASTE_INTO_NEW_IMAGE = "paste_new"
    PASTE_AT_CURSOR = "paste_at"
    PASTE_INTO_ACTIVE_LAYER = "paste_into"
    PASTE_AS_REFERENCE_IMAGE = "paste_as_reference"
    PASTE_SHAPE_STYLE = "paste_shape_style"
    COPY_MERGED = "copy_merged"
    FLATTEN_IMAGE = "flatten_image"
    MERGE_WITH_LAYER_BELOW = "merge_layer"
    FLATTEN_LAYER = "flatten_layer"

    _filling = Group("Filling")
    FILL_WITH_FOREGROUND_COLOUR = "fill_selection_foreground_color"
    FILL_WITH_BACKGROUND_COLOUR = "fill_selection_background_color"
    FILL_WITH_PATTERN = "fill_selection_pattern"
    FILL_WITH_FOREGROUND_COLOUR_OPACITY = \
        "fill_selection_foreground_color_opacity"
    FILL_WITH_BACKGROUND_COLOUR_OPACITY = \
        "fill_selection_background_color_opacity"
    FILL_WITH_PATTERN_OPACITY = "fill_selection_pattern_opacity"
    STROKE_SELECTED_SHAPES = "stroke_shapes"

    _selection = Group("Selection")
    SELECT_ALL = "select_all"
    DESELECT = "deselect"
    CLEAR = "clear"
    RESELECT = "reselect"
    INVERT_SELECTION = "invert_selection"
    SELECTION_MODE_ADD = "selection_tool_mode_add"
    SELECTION_MODE_REPLACE = "selection_tool_mode_replace"
    SELECTION_MODE_SUBTRACT = "selection_tool_mode_subtract"
    SELECTION_MODE_INTERSECT = "selection_tool_mode_intersect"
    DISPLAY_SELECTION = "toggle_display_selection"
    TRIM_TO_SELECTION = "resizeimagetoselection"
    EDIT_SELECTION = "edit_selection"
    CONVERT_TO_VECTOR_SELECTION = "convert_to_vector_selection"
    CONVERT_TO_RASTER_SELECTION = "convert_to_raster_selection"
    CONVERT_SHAPES_TO_VECTOR_SELECTION = "convert_shapes_to_vector_selection"
    CONVERT_TO_SHAPE = "convert_selection_to_shape"
    TOGGLE_SELECTION_DISPLAY_MODE = "toggle-selection-overlay-mode"
    STROKE_SELECTION = "stroke_selection"
    COPY_SELECTION_TO_NEW_LAYER = "copy_selection_to_new_layer"
    CUT_SELECTION_TO_NEW_LAYER = "cut_selection_to_new_layer"
    SELECT_FROM_COLOUR_RANGE = "colorrange"
    SELECT_OPAQUE_REPLACE = "selectopaque"
    SELECT_OPAQUE_ADD = "selectopaque_add"
    SELECT_OPAQUE_SUBTRACT = "selectopaque_subtract"
    SELECT_OPAQUE_INTERSECT = "selectopaque_intersect"
    GROW_SELECTION = "growselection"
    SHRINK_SELECTION = "shrinkselection"
    BORDER_SELECTION = "borderselection"
    FEATHER_SELECTION = "featherselection"
    SMOOTH = "smoothselection"

    _layer_stack = Group("Layer stack")
    LAYER_PROPERTIES = "layer_properties"
    COPY_LAYER = "copy_layer_clipboard"
    CUT_LAYER = "cut_layer_clipboard"
    PASTE_LAYER = "paste_layer_from_clipboard"
    DUPLICATE_LAYER_OR_MASK = "duplicatelayer"
    RENAME_CURRENT_LAYER = "RenameCurrentLayer"
    REMOVE_LAYER = "remove_layer"
    QUICK_GROUP = "create_quick_group"
    QUICK_CLIPPING_GROUP = "create_quick_clipping_group"
    QUICK_UNGROUP = "quick_ungroup"
    MIRROR_LAYER_HORIZONTALLY = "mirrorNodeX"
    MIRROR_LAYER_VERTICALLY = "mirrorNodeY"
    MIRROR_ALL_LAYERS_HORIZONTALLY = "mirrorAllNodesX"
    MIRROR_ALL_LAYERS_VERTICALLY = "mirrorAllNodesY"
    PIN_TO_TIMELINE = "pin_to_timeline"
    TOGGLE_LAYER_SOLOING = "toggle_layer_soloing"
    SAVE_GROUP_LAYERS = "save_groups_as_images"
    MOVE_LAYER_OR_MASK_UP = "move_layer_up"
    MOVE_LAYER_OR_MASK_DOWN = "move_layer_down"
    SELECT_ALL_LAYERS = "select_all_layers"
    SELECT_VISIBLE_LAYERS = "select_visible_layers"
    SELECT_LOCKED_LAYERS = "select_locked_layers"
    SELECT_INVISIBLE_LAYERS = "select_invisible_layers"
    SELECT_UNLOCKED_LAYERS = "select_unlocked_layers"
    ACTIVATE_NEXT_LAYER = "activateNextLayer"
    ACTIVATE_NEXT_SIBLING_LAYER = \
        "activateNextSiblingLayer"
    ACTIVATE_PREVIOUS_LAYER = "activatePreviousLayer"
    ACTIVATE_PREVIOUS_SIBLING_LAYER = \
        "activatePreviousSiblingLayer"
    CONVERT_GROUP_TO_ANIMATED_LAYER = "convert_group_to_animated"
    TRIM_TO_CURRENT_LAYER = "resizeimagetolayer"
    TRIM_TO_IMAGE_SIZE = "trim_to_image"
    LAYER_STYLE = "layer_style"
    COPY_LAYER_STYLE = "copy_layer_style"
    PASTE_LAYER_STYLE = "paste_layer_style"
    ACTIVATE_PREVIOUSLY_SELECTED_LAYER = "switchToPreviouslyActiveNode"
    SAVE_LAYER_MASK = "save_node_as_image"
    SAVE_VECTOR_LAYER_AS_SVG = "save_vector_node_to_svg"
    TO_FILE_LAYER = "convert_to_file_layer"

    _layer_creation = Group("Layer creation")
    ADD_PAINT_LAYER = "add_new_paint_layer"
    ADD_GROUP_LAYER = "add_new_group_layer"
    ADD_CLONE_LAYER = "add_new_clone_layer"
    ADD_VECTOR_LAYER = "add_new_shape_layer"
    ADD_FILTER_LAYER = "add_new_adjustment_layer"
    ADD_FILL_LAYER = "add_new_fill_layer"
    ADD_FILE_LAYER = "add_new_file_layer"
    ADD_TRANSPARENCY_MASK = "add_new_transparency_mask"
    ADD_FILTER_MASK = "add_new_filter_mask"
    ADD_COLOURISE_MASK = "add_new_colorize_mask"
    ADD_TRANSFORM_MASK = "add_new_transform_mask"
    ADD_LOCAL_SELECTION = "add_new_selection_mask"
    CONVERT_TO_PAINT_LAYER = "convert_to_paint_layer"
    CONVERT_TO_SELECTION_MASK = "convert_to_selection_mask"
    CONVERT_TO_FILTER_MASK = "convert_to_filter_mask"
    CONVERT_TO_TRANSPARENCY_MASK = "convert_to_transparency_mask"
    CONVERT_TO_ANIMATED_LAYER = "convert_to_animated"
    IMPORT_LAYER = "import_layer_from_file"
    AS_PAINT_LAYER = "import_layer_as_paint_layer"
    AS_TRANSPARENCY_MASK = "import_layer_as_transparency_mask"
    AS_FILTER_MASK = "import_layer_as_filter_mask"
    AS_SELECTION_MASK = "import_layer_as_selection_mask"
    NEW_LAYER_FROM_VISIBLE = "new_from_visible"

    _layer_handling = Group("Layer handling")
    ISOLATE_ACTIVE_GROUP = "isolate_active_group"
    TOGGLE_LAYER_VISIBILITY = "toggle_layer_visibility"
    TOGGLE_LAYER_LOCK = "toggle_layer_lock"
    TOGGLE_LAYER_ALPHA_INHERITANCE = "toggle_layer_inherit_alpha"
    TOGGLE_LAYER_ALPHA = "toggle_layer_alpha_lock"
    ALPHA_INTO_MASK = "split_alpha_into_mask"
    WRITE_AS_ALPHA = "split_alpha_write"

    _brush_property_editing = Group("Brush property editing")
    NEXT_FAVOURITE_PRESET = "next_favorite_preset"
    PREVIOUS_FAVOURITE_PRESET = "previous_favorite_preset"
    SWITCH_TO_PREVIOUS_PRESET = "previous_preset"
    RELOAD_ORIGINAL_PRESET = "reload_preset_action"
    INCREASE_BRUSH_SIZE = "increase_brush_size"
    DECREASE_BRUSH_SIZE = "decrease_brush_size"
    MAKE_BRUSH_COLOUR_LIGHTER = "make_brush_color_lighter"
    MAKE_BRUSH_COLOUR_DARKER = "make_brush_color_darker"
    MAKE_BRUSH_COLOUR_MORE_SATURATED = "make_brush_color_saturated"
    MAKE_BRUSH_COLOUR_MORE_DESATURATED = "make_brush_color_desaturated"
    SHIFT_BRUSH_COLOUR_HUE_CLOCKWISE = "shift_brush_color_clockwise"
    SHIFT_BRUSH_COLOUR_HUE_COUNTER_CLOCKWISE = \
        "shift_brush_color_counter_clockwise"
    MAKE_BRUSH_COLOUR_MORE_RED = "make_brush_color_redder"
    MAKE_BRUSH_COLOUR_MORE_GREEN = "make_brush_color_greener"
    MAKE_BRUSH_COLOUR_MORE_BLUE = "make_brush_color_bluer"
    MAKE_BRUSH_COLOUR_MORE_YELLOW = "make_brush_color_yellower"
    INCREASE_OPACITY = "increase_opacity"
    DECREASE_OPACITY = "decrease_opacity"
    INCREASE_FLOW = "increase_flow"
    DECREASE_FLOW = "decrease_flow"
    INCREASE_FADE = "increase_fade"
    DECREASE_FADE = "decrease_fade"
    INCREASE_SCATTER = "increase_scatter"
    DECREASE_SCATTER = "decrease_scatter"
    BRUSH_SMOOTHING_DISABLED = "set_no_brush_smoothing"
    BRUSH_SMOOTHING_BASIC = "set_simple_brush_smoothing"
    BRUSH_SMOOTHING_WEIGHTED = "set_weighted_brush_smoothing"
    BRUSH_SMOOTHING_STABILISER = "set_stabilizer_brush_smoothing"

    _opening_menus = Group("Opening menus")
    CONFIGURE_KRITA = "options_configure"
    SHOW_BRUSH_EDITOR = "show_brush_editor"
    CONFIGURE_TOOLBARS = "options_configure_toolbars"
    CONFIGURE_SHORTCUT_COMPOSER = "Configure Shortcut Composer"
    MANAGE_RESOURCE_LIBRARIES = "manage_bundles"
    MANAGE_RESOURCES = "manage_resources"
    START_GMIC_QT = "QMic"
    REAPPLY_THE_LAST_GMIC_FILTER = "QMicAgain"
    THEMES = "theme_menu"
    SHOW_DOCKERS = "view_toggledockers"
    RESET_ALL_SETTINGS = "reset_configurations"
    PATTERNS = "patterns"
    GRADIENTS = "gradients"
    CHOOSE_FOREGROUND_AND_BACKGROUND_COLOURS = "dual"
    PROPERTIES = "image_properties"
    SHOW_SNAP_OPTIONS_POPUP = "show_snap_options_popup"
    SHOW_BRUSH_PRESETS = "show_brush_presets"
    OPEN_RESOURCES_FOLDER = "open_resources_directory"

    _tool_bars = Group("Tool bars")
    HIDE_MIRROR_X_LINE = "mirrorX-hideDecorations"
    LOCK_X_LINE = "mirrorX-lock"
    MOVE_TO_CANVAS_CENTRE_X = "mirrorX-moveToCenter"
    HIDE_MIRROR_Y_LINE = "mirrorY-hideDecorations"
    LOCK_Y_LINE = "mirrorY-lock"
    MOVE_TO_CANVAS_CENTRE_Y = "mirrorY-moveToCenter"
    HORIZONTAL_MIRROR_TOOL = "hmirror_action"
    VERTICAL_MIRROR_TOOL = "vmirror_action"
    NEXT_BLENDING_MODE = "Next Blending Mode"
    PREVIOUS_BLENDING_MODE = "Previous Blending Mode"
    BRUSH_COMPOSITE = "composite_actions"
    BRUSH_OPTION_SLIDER_1 = "brushslider1"
    BRUSH_OPTION_SLIDER_2 = "brushslider2"
    BRUSH_OPTION_SLIDER_3 = "brushslider3"
    BRUSH_OPTION_SLIDER_4 = "brushslider4"
    SHOW_GLOBAL_SELECTION_MASK = "show-global-selection-mask"
    WRAP_AROUND_MODE = "wrap_around_mode"
    MIRROR = "mirror_actions"
    WORKSPACES = "workspaces"
    USE_PEN_PRESSURE = "disable_pressure"
    OPEN_FOREGROUND_COLOUR_SELECTOR = "chooseForegroundColor"
    OPEN_BACKGROUND_COLOUR_SELECTOR = "chooseBackgroundColor"
    SWAP_FOREGROUND_AND_BACKGROUND_COLOURS = "toggle_fg_bg"
    SET_FOREGROUND_AND_BACKGROUND_COLOURS_TO_BLACK_AND_WHITE = "reset_fg_bg"

    _image_operations = Group("Image operations")
    SCALE_IMAGE_TO_NEW_SIZE = "imagesize"
    RESIZE_CANVAS = "canvassize"
    ROTATE_IMAGE = "rotateimage"
    ROTATE_IMAGE_90_TO_THE_RIGHT = "rotateImageCW90"
    ROTATE_IMAGE_180 = "rotateImage180"
    ROTATE_IMAGE_90_TO_THE_LEFT = "rotateImageCCW90"
    MIRROR_IMAGE_HORIZONTALLY = "mirrorImageHorizontal"
    MIRROR_IMAGE_VERTICALLY = "mirrorImageVertical"
    IMAGE_BACKGROUND_COLOUR_AND_TRANSPARENCY = "image_color"
    SEPARATE_IMAGE = "separate"
    SHEAR_IMAGE = "shearimage"
    OFFSET_IMAGE = "offsetimage"

    _layer_operations = Group("Layer operations")
    SCALE_LAYER_TO_NEW_SIZE = "layersize"
    SCALE_ALL_LAYERS_TO_NEW_SIZE = "scaleAllLayers"
    SHEAR_LAYER = "shearlayer"
    SHEAR_ALL_LAYERS = "shearAllLayers"
    SPLIT_LAYER = "layersplit"
    ROTATE_LAYER = "rotatelayer"
    ROTATE_LAYER_180 = "rotateLayer180"
    ROTATE_LAYER_90_TO_THE_RIGHT = "rotateLayerCW90"
    ROTATE_LAYER_90_TO_THE_LEFT = "rotateLayerCCW90"
    ROTATE_ALL_LAYERS = "rotateAllLayers"
    ROTATE_ALL_LAYERS_90_TO_THE_RIGHT = "rotateAllLayersCW90"
    ROTATE_ALL_LAYERS_90_TO_THE_LEFT = "rotateAllLayersCCW90"
    ROTATE_ALL_LAYERS_180 = "rotateAllLayers180"
    OFFSET_LAYER = "offsetlayer"

    _tool_specific_actions = Group("Tool specific actions")
    MOVE_UP = "movetool-move-up"
    MOVE_DOWN = "movetool-move-down"
    MOVE_LEFT = "movetool-move-left"
    MOVE_RIGHT = "movetool-move-right"
    MOVE_UP_MORE = "movetool-move-up-more"
    MOVE_DOWN_MORE = "movetool-move-down-more"
    MOVE_LEFT_MORE = "movetool-move-left-more"
    MOVE_RIGHT_MORE = "movetool-move-right-more"
    SHOW_COORDINATES = "movetool-show-coordinates"
    SCALE = "selectionscale"
    CALLIGRAPHY = "KarbonCalligraphyTool"
    CALLIGRAPHY_INCREASE_WIDTH = "calligraphy_increase_width"
    CALLIGRAPHY_DECREASE_WIDTH = "calligraphy_decrease_width"
    CALLIGRAPHY_INCREASE_ANGLE = "calligraphy_increase_angle"
    CALLIGRAPHY_DECREASE_ANGLE = "calligraphy_decrease_angle"
    WAVELET_DECOMPOSE = "waveletdecompose"
    UNDO_POLYGON_SELECTION_POINTS = "undo_polygon_selection"
    CORNER_POINT = "pathpoint-corner"
    SMOOTH_POINT = "pathpoint-smooth"
    SYMMETRIC_POINT = "pathpoint-symmetric"
    MAKE_CURVE_POINT = "pathpoint-curve"
    MAKE_LINE_POINT = "pathpoint-line"
    SEGMENT_TO_LINE = "pathsegment-line"
    SEGMENT_TO_CURVE = "pathsegment-curve"
    INSERT_POINT = "pathpoint-insert"
    REMOVE_POINT = "pathpoint-remove"
    BREAK_AT_POINT = "path-break-point"
    BREAK_AT_SEGMENT = "path-break-segment"
    JOIN_WITH_SEGMENT = "pathpoint-join"
    MERGE_POINTS = "pathpoint-merge"
    TO_PATH = "convert-to-path"
    BRING_TO_FRONT = "object_order_front"
    RAISE = "object_order_raise"
    LOWER = "object_order_lower"
    SEND_TO_BACK = "object_order_back"
    ALIGN_LEFT = "object_align_horizontal_left"
    HORIZONTALLY_CENTRE = "object_align_horizontal_center"
    ALIGN_RIGHT = "object_align_horizontal_right"
    ALIGN_TOP = "object_align_vertical_top"
    VERTICALLY_CENTRE = "object_align_vertical_center"
    ALIGN_BOTTOM = "object_align_vertical_bottom"
    DISTRIBUTE_LEFT = "object_distribute_horizontal_left"
    DISTRIBUTE_CENTRES_HORIZONTALLY = "object_distribute_horizontal_center"
    DISTRIBUTE_RIGHT = "object_distribute_horizontal_right"
    DISTRIBUTE_HORIZONTAL_GAP = "object_distribute_horizontal_gaps"
    DISTRIBUTE_TOP = "object_distribute_vertical_top"
    DISTRIBUTE_CENTRES_VERTICALLY = "object_distribute_vertical_center"
    DISTRIBUTE_BOTTOM = "object_distribute_vertical_bottom"
    DISTRIBUTE_VERTICAL_GAP = "object_distribute_vertical_gaps"
    GROUP = "object_group"
    UNGROUP = "object_ungroup"
    ROTATE_90_C_W = "object_transform_rotate_90_cw"
    ROTATE_90_A_C_W = "object_transform_rotate_90_ccw"
    ROTATE_180 = "object_transform_rotate_180"
    MIRROR_HORIZONTALLY = "object_transform_mirror_horizontally"
    MIRROR_VERTICALLY = "object_transform_mirror_vertically"
    RESET_TRANSFORMATIONS = "object_transform_reset"
    UNITE = "object_unite"
    INTERSECT = "object_intersect"
    SUBTRACT = "object_subtract"
    SPLIT = "object_split"

    _animation = Group("Animation")
    CREATE_BLANK_FRAME = "add_blank_frame"
    CREATE_DUPLICATE_FRAME = "add_duplicate_frame"
    INSERT_KEYFRAME_LEFT = "insert_keyframe_left"
    INSERT_KEYFRAME_RIGHT = "insert_keyframe_right"
    INSERT_MULTIPLE_KEYFRAMES = "insert_multiple_keyframes"
    REMOVE_FRAME_AND_PULL = "remove_frames_and_pull"
    REMOVE_KEYFRAME = "remove_frames"
    INSERT_HOLD_FRAME = "insert_hold_frame"
    INSERT_MULTIPLE_HOLD_FRAMES = "insert_multiple_hold_frames"
    REMOVE_HOLD_FRAME = "remove_hold_frame"
    REMOVE_MULTIPLE_HOLD_FRAMES = "remove_multiple_hold_frames"
    MIRROR_FRAMES = "mirror_frames"
    COPY_KEYFRAMES = "copy_frames"
    CLONE_KEYFRAMES = "copy_frames_as_clones"
    MAKE_UNIQUE = "make_clones_unique"
    CUT_KEYFRAMES = "cut_frames"
    PASTE_KEYFRAMES = "paste_frames"
    SET_START_TIME = "set_start_time"
    SET_END_TIME = "set_end_time"
    UPDATE_PLAYBACK_RANGE = "update_playback_range"
    PLAY_PAUSE_ANIMATION = "toggle_playback"
    STOP_ANIMATION = "stop_playback"
    PREVIOUS_FRAME = "previous_frame"
    NEXT_FRAME = "next_frame"
    PREVIOUS_KEYFRAME = "previous_keyframe"
    NEXT_KEYFRAME = "next_keyframe"
    PREVIOUS_MATCHING_KEYFRAME = "previous_matching_keyframe"
    NEXT_MATCHING_KEYFRAME = "next_matching_keyframe"
    PREVIOUS_UNFILTERED_KEYFRAME = "previous_unfiltered_keyframe"
    NEXT_UNFILTERED_KEYFRAME = "next_unfiltered_keyframe"
    AUTO_FRAME_MODE = "auto_key"
    ADD_SCALAR_KEYFRAMES = "add_scalar_keyframes"
    REMOVE_SCALAR_KEYFRAME = "remove_scalar_keyframe"
    HOLD_CONSTANT_VALUE_NO_INTERPOLATION = "interpolation_constant"
    LINEAR_INTERPOLATION = "interpolation_linear"
    BEZIER_CURVE_INTERPOLATION = "interpolation_bezier"
    SHARP_INTERPOLATION_TANGENTS = "tangents_sharp"
    SMOOTH_INTERPOLATION_TANGENTS = "tangents_smooth"
    ZOOM_VIEW_TO_FIT_CHANNEL_RANGE = "zoom_to_fit_range"
    ZOOM_VIEW_TO_FIT_CURVE = "zoom_to_fit_curve"
    DROP_FRAMES = "drop_frames"

    _krita_window = Group("Krita window")
    DETACH_CANVAS = "view_detached_canvas"
    SHOW_DOCKER_TITLEBARS = "view_toggledockertitlebars"
    DOCKERS = "settings_dockers_menu"
    WINDOW = "window"
    STYLES = "style_menu"
    CASCADE = "windows_cascade"
    TILE = "windows_tile"
    NEXT = "windows_next"
    PREVIOUS = "windows_previous"
    NEW_WINDOW = "view_newwindow"
    CLOSE = "file_close"
    SESSIONS = "file_sessions"
    SEARCH_ACTIONS = "command_bar_open"

    _python_scripts = Group("Python scripts")
    IMPORT_PYTHON_PLUGIN_FROM_FILE = "plugin_importer_file"
    IMPORT_PYTHON_PLUGIN_FROM_WEB = "plugin_importer_web"
    SCRIPTER = "python_scripter"
    TEN_SCRIPTS = "ten_scripts"
    EXECUTE_SCRIPT_1 = "execute_script_1"
    EXECUTE_SCRIPT_2 = "execute_script_2"
    EXECUTE_SCRIPT_3 = "execute_script_3"
    EXECUTE_SCRIPT_4 = "execute_script_4"
    EXECUTE_SCRIPT_5 = "execute_script_5"
    EXECUTE_SCRIPT_6 = "execute_script_6"
    EXECUTE_SCRIPT_7 = "execute_script_7"
    EXECUTE_SCRIPT_8 = "execute_script_8"
    EXECUTE_SCRIPT_9 = "execute_script_9"
    EXECUTE_SCRIPT_10 = "execute_script_10"
    EXPORT_LAYERS = "export_layers"
    RECORD_TIMELAPSE = "recorder_record_toggle"
    EXPORT_TIMELAPSE = "recorder_export"
    HIDE_FILE_TOOLBAR = "mainToolBar"
    HIDE_BRUSHES_AND_STUFF_TOOLBAR = "BrushesAndStuff"
    ZOOM = "view_zoom"
    SHOW_COLOUR_SELECTOR = "show_color_selector"
    SHOW_MY_PAINT_SHADE_SELECTOR = "show_mypaint_shade_selector"
    SHOW_MINIMAL_SHADE_SELECTOR = "show_minimal_shade_selector"
    SHOW_COLOUR_HISTORY = "show_color_history"
    SHOW_COMMON_COLOURS = "show_common_colors"
    UPDATE_COMPOSITION = "update_composition"
    RENAME_COMPOSITION = "rename_composition"
    RELOAD_SHORTCUT_COMPOSER = "Reload Shortcut Composer"

    _other = Group("Other")
    CONVERT_IMAGE_COLOUR_SPACE = "imagecolorspaceconversion"
    CONVERT_LAYER_COLOUR_SPACE = "layercolorspaceconversion"
    EXPLORE_RESOURCES_CACHE_DATABASE = "dbexplorer"
    IMAGE_SPLIT = "imagesplit"
    MOVE_INTO_PREVIOUS_GROUP = "LayerGroupSwitcher/previous"
    MOVE_INTO_NEXT_GROUP = "LayerGroupSwitcher/next"
    # --- #
    SET_COPY_FROM = "set-copy-from"
    CREATE_SNAPSHOT = "create_snapshot"
    SWITCH_TO_SELECTED_SNAPSHOT = "switchto_snapshot"
    REMOVE_SELECTED_SNAPSHOT = "remove_snapshot"
    INSERT_COLUMN_LEFT = "insert_column_left"
    INSERT_COLUMN_RIGHT = "insert_column_right"
    INSERT_MULTIPLE_COLUMNS = "insert_multiple_columns"
    REMOVE_COLUMN_AND_PULL = "remove_columns_and_pull"
    REMOVE_COLUMN = "remove_columns"
    INSERT_HOLD_COLUMN = "insert_hold_column"
    INSERT_MULTIPLE_HOLD_COLUMNS = "insert_multiple_hold_columns"
    REMOVE_HOLD_COLUMN = "remove_hold_column"
    REMOVE_MULTIPLE_HOLD_COLUMNS = "remove_multiple_hold_columns"
    MIRROR_COLUMNS = "mirror_columns"
    CLEAR_CACHE = "clear_animation_cache"
    COPY_COLUMNS = "copy_columns_to_clipboard"
    CUT_COLUMNS = "cut_columns_to_clipboard"
    PASTE_COLUMNS = "paste_columns_from_clipboard"

    def activate(self):
        """Activate the action."""
        try:
            Api.instance().action(self.value).trigger()
        except AttributeError:
            print(self.value)

    @property
    def icon(self) -> QIcon:
        """Return the icon of this action."""
        try:
            return Api.instance().action(self.value).icon()
        except AttributeError:
            return QIcon()

    @property
    def pretty_name(self) -> str:
        """Return the name of this action."""
        try:
            return Api.instance().action(self.value).text().replace("&", "")
        except AttributeError:
            return "---"
