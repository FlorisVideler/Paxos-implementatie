from classes.simulation import Simulation

if __name__ == '__main__':
    # Runs all the simulation examples.
    inputs = ['input/example1.txt', 'input/example2.txt', 'input/example3.txt']  # input files

    for inp in inputs:
        print('EXAMPLE:', inp, '\n')
        sim = Simulation(inp)  # create simulation with input example
        sim.start()
        print('\n\n')
