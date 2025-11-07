%%----------------------------------------
%%  Core Module Data Flow (ai_core package)
%%  Color Legend:
%%    🟧 Orange = Core Module
%%    🟩 Green  = Supporting Package Folder
%%    🟦 Cyan   = Input/Output Interface
%%----------------------------------------

flowchart LR
    %% INPUT AND OUTPUT
    U[🟦 User Input / CLI]:::cli --> WF[🟧 workflow_engine.py]:::module
    WF --> GE[🟧 graph_engine.py]:::module
    GE --> RM[🟧 recursion_manager.py]:::module
    RM --> EE[🟧 evaluation_engine.py]:::module
    EE --> VF[🟧 visualizer.py]:::module
    VF --> IO[🟧 io_manager.py]:::module
    IO --> UO[🟦 User Output (Markdown / JSON / Graphviz)]:::cli

    %% BACKFLOW (Evaluation Feedback Loop)
    EE -. feedback .-> WF
    RM -. recursion_control .-> WF

    %% STYLING
    classDef module fill:#FFB347,stroke:#CC7000,color:black;
    classDef cli fill:#00CED1,stroke:#007C80,color:black;
