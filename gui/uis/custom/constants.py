tree_structure = {
    "Execute": {
        "Execution Plans": ("Execution Plans", "executionplans"),
        "Settings": ("Settings", "settings")
    },
    "Settings": {
        "Competition": ("Competition", "competition"),
        "Diagnostics": ("Diagnostic", "diagnostics"),
        "Performance": ("Performance", "performance"),
        "Production": ("Production", "production"),
        "Stochastics": ("Stochastic", "stochastics"),
        "Transmission": ("Transmission", "transmission")
    },
    "Simulation": {
        "ST Schedule": ("Short Term Schedule", "stschedule"),
        "MT Schedule": ("Medium Term Schedule", "mtschedule"),
        "LRMC Models": ("LRMC Models", "lrmcmodels"),
        "Horizons": ("Horizon", "horizons"),
        "PASA": ("PASA", "pasa"),
        "Reports": ("Report", "reports")
    },
    "Extra": {
        "Feature Binning Properties": ("Feature Binning Properties", "featurebinningproperties"),
    }
}

execution_priorities = [("Low", 25), ("Normal", 50), ("High", 75), ("Urgent", 100)]

plot_colors = [
    (234, 85, 69),
    (244, 106, 155),
    (239, 155, 32),
    (237, 191, 51),
    (237, 225, 91),
    (189, 207, 50),
    (135, 188, 69),
    (39, 174, 239),
    (179, 61, 198)
]