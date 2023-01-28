import tracks
from PAO import PAO
from PAO_2 import PAO_2


cars = [PAO(), PAO_2()]

cars_models = [model.get_actor_model() for model in cars]

scoreboard = tracks.newrun(cars_models)

completion_codes = [
    "", "finished", "off track", "wrong direction", "under speed limit"
]

for car in scoreboard:
    if car["completion"] == 1:
        print(
            f"car {car['car']} ({cars[car['car']-1].get_name()}) finished in {car['place']} position."
        )
    else:
        print(
            f"car {car['car']} ({cars[car['car']-1].get_name()}) did not finish with completion code {car['completion']} ({completion_codes[car['completion']]})."
        )

print(scoreboard)  