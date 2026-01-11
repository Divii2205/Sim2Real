import genesis as gs
import time

gs.init(backend=gs.cpu)

# Create screen with viewer
scene = gs.Scene(show_viewer=True)

scene.add_entity(
    gs.morphs.Plane()
)

# scene.build()   # prepares physics
# scene.step()    # advances time by Δt

scene.build()

while True:
    scene.step()
    time.sleep(1/60)
