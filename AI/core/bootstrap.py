def run_phases(workflow):
    for phase_class in load_phases_from_registry():
        phase = phase_class(workflow)
        phase.run()

