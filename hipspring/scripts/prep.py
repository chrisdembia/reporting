

# Copy over the required data.
data = HamnerXX()

# Organize the data using my own naming conventions.
data.transfer('/media/Elements/hamnerxx/', '~/hamnerxx/', runtypes='cmc')
#data.move()

# Develop the simulations that I want to run.
hsa.metabolics_probe_name_is('Umberger2010')
hsa.metabolics_probe_fullbody_state_is('on')
hsa.metabolics_probe_permuscle_state_is('on')

# Set up the output format.
hsa.output_path_is()

# Run the simulations.
hsa.run()

# Calculate desired results data.

# Generate graphs, etc.

hsa = HipSpringAnalysis()
hsa.run()
hsa.report(hsrep.path())
hsa.reported()
hsa.simulationCompleted(True)
hsa.sas_vs_stiffness()
hsa.cot_vs_stiffness()
hsa.joint_torque_comparision()
hsa.audit()
hsa.reserves()
hsa.check_reserves()
hsa.reserves_below_threshold()
