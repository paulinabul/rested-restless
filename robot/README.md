# Robot files

| File | What it is |
| --- | --- |
| `basic_ur_setup_rested.gh` | Grasshopper file for RESTED |
| `basic_ur_setup_restless.gh` | Grasshopper file for RESTLESS |
| Rhino files (`.3dm`) | The curves for the two words |
| `06_rested.script` | Robot program for RESTED (calm) |
| `06_restless.script` | Robot program for RESTLESS (restless) |

The two words use different values for acceleration, speed and blend radius. You can see
them in every `movel(...)` line of the `.script` files: `a=` is acceleration, `v=` is speed
and `r=` is the blend radius.
