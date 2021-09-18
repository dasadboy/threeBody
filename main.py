import os, sys
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import sim, body


if len(sys.argv) < 2:
    raise Exception("No data file given")
elif len(sys.argv) > 2:
    raise Exception("Only 1 data file required.")

bodies = []
with open(sys.argv[1], 'r') as f:
    # print(f.readlines())
    for line in f.readlines():
        name, m,  x0, y0, vx, vy, color  = line.strip().split()
        bodies.append(body.Body(name, float(m), (float(x0), float(y0)), (float(vx), float(vy)), color))


G = 6.673e-11
ani = sim.Simulation(G, bodies)
inp = None
convert = {
    "minutes": 60,
    "hours": 3600,
    "days": 86400,
    "months": 2592000,
    "years": 31536000
}
while inp != "quit":
    inp = input("calculate points (cp) / animate / plot / help / quit? : ").strip()
    if inp.startswith("calculate points") or inp.startswith("cp"):
        inp = inp.split()
        if inp[0] == "cp" and len(inp) == 3 or len(inp) == 4:
            try:
                dur, dt = float(inp[-2]), float(inp[-1])
            except ValueError as e:
                print(e, "Arguments must be 2 numbers (floats).")
        elif inp[0] == "cp" and len(inp) != 1 or len(inp) != 2:
            raise ValueError("Incorrect number of arguments given")
        else:
            try:
                dur = float(input("duration (seconds): "))
            except ValueError as e:
                print(e, "Input must be a float.")
                continue
            try:
                dt = float(input("dt (resolution of the simulation): "))
            except ValueError as e:
                print(e, "Input must be a float.")
                continue
        ani.reset()
        ani.createPoints(dur, dt)
    elif inp == "animate":
        print("Has not been implemented yet.")
    elif inp == "plot":
        ani.plot()
    elif inp == "help":
        print(
            "calculate points [float float]:\n" +
            "  Builds a set of points that each body traces.\n" +
            "  Can give 2 arguments along with command to set duration (length of time of the simulation) and dt (resolution in time of the simulation).\n" +
            "  Will be asked for duration, dt if not previously entered as arguments.\n" +
            "  Rerun to set new duration and dt.\n" +
            "animate:\n" +
            "  Requires you to run calculate points first as animations use data generated from it.\n" +
            "  **Not currently implemented**\n" +
            "plot:\n" +
            "  Requires you to run calculate points first as plots use data generated from it.\n" +
            "  Plots points in a graph using matplotlip.pyplot.\n" +
            "help: this\n" +
            "quit:\n" +
            "  End the program.\n"
        )
    elif inp != "quit":
        print("Invalid query")
sys.exit()