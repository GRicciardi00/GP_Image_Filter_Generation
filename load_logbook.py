import  pickle, sys, os

# USAGE: python load_logbook.py checkpoint_name.pkl

if len(sys.argv) != 3:
    print (" USAGE: python load_logbook.py checkpoint_name.pkl output_folder")
    sys.exit()
    
    

with open(sys.argv[1], "rb") as cp_file:
    cp = pickle.load(cp_file)
    logbook = cp["logbook"]
    
gen = logbook.select("gen")
fit_mins = logbook.chapters["fitness"].select("min")
size_avgs = logbook.chapters["size"].select("avg")

import matplotlib.pyplot as plt

fig, ax1 = plt.subplots()
line1 = ax1.plot(gen, fit_mins, "b-", label="Minimum Fitness")
ax1.set_xlabel("Generation")
ax1.set_ylabel("Fitness", color="b")
for tl in ax1.get_yticklabels():
    tl.set_color("b")

ax2 = ax1.twinx()
line2 = ax2.plot(gen, size_avgs, "r-", label="Average Size")
ax2.set_ylabel("Size", color="r")
for tl in ax2.get_yticklabels():
    tl.set_color("r")

lns = line1 + line2
labs = [l.get_label() for l in lns]
ax1.legend(lns, labs, loc="center right")
fig_name = sys.argv[2] + "/results/" + os.path.splitext(sys.argv[1].split("/")[-1])[0] + "_fitness.png"
print(fig_name)
plt.savefig(fig_name)

