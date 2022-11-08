tree_structure = {
    "Execute": {
        "Models": ("Model", "models"),
        "Projects": ("Project", "projects")
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
        "LT Plan": ("Long Term Plan", "ltplan"),
        "Horizons": ("Horizaon", "horizons"),
        "PASA": ("PASA", "pasa"),
        "Reports": ("Report", "reports")
    }
}

execution_priorities = [("Low", 25), ("Normal", 50), ("High", 75), ("Urgent", 100)]