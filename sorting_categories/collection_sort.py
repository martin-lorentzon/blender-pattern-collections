from .. import gui


class PATTERN_COLLECTIONS_UL_included_collections(gui.BaseItemUIList):
    pass


class PATTERN_COLLECTIONS_UL_excluded_collections(gui.BaseItemUIList):
    pass


class PATTERN_COLLECTIONS_PT_included_collections(gui.PATTERN_COLLECTIONS_PT_uilist):
    custom_label = "Included Collections"
    uilist_class = "PATTERN_COLLECTIONS_UL_included_collections"
    category = "included_collections"
    active_index = "active_included_collection_index"
    default_name = "Collection"


class PATTERN_COLLECTIONS_PT_excluded_collections(gui.PATTERN_COLLECTIONS_PT_uilist):
    custom_label = "Excluded Collections"
    uilist_class = "PATTERN_COLLECTIONS_UL_excluded_collections"
    category = "excluded_collections"
    active_index = "active_excluded_collection_index"
    default_name = "Collection"